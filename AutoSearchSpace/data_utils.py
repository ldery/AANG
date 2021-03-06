import torch
import unicodedata
import numpy as np
from torch.nn.utils.rnn import pad_sequence as torch_pad_sequence


def pad_sequence(all_egs, pad_token_id):
	if pad_token_id is None:
		return torch_pad_sequence(all_egs, batch_first=True)
	else:
		return torch_pad_sequence(all_egs, batch_first=True, padding_value=pad_token_id)

def mask_tokens(inputs, tokenizer, proba, tform):
	""" Prepare masked tokens inputs/labels for masked language modeling: 80% MASK, 10% random, 10% original. """

	if tokenizer.mask_token is None:
		raise ValueError(
			"This tokenizer does not have a mask token which is necessary for masked language modeling. Remove the --mlm flag if you want to use this tokenizer."
		)
	labels = inputs.clone()
	# We sample a few tokens in each sequence for masked-LM training (with probability args.mlm_probability defaults to 0.15 in Bert/RoBERTa)
	probability_matrix = torch.full(labels.shape, proba)
	special_tokens_mask = [
		tokenizer.get_special_tokens_mask(val, already_has_special_tokens=True) for val in labels.tolist()
	]
	probability_matrix.masked_fill_(torch.tensor(special_tokens_mask, dtype=torch.bool), value=0.0)
	if tokenizer._pad_token is not None:
		padding_mask = labels.eq(tokenizer.pad_token_id)
		probability_matrix.masked_fill_(padding_mask, value=0.0)
	masked_indices = torch.bernoulli(probability_matrix).bool()
	labels[~masked_indices] = -100	# We only compute loss on masked tokens

	if tform == 'Mask':
		inputs[masked_indices] = tokenizer.convert_tokens_to_ids(tokenizer.mask_token)
	elif tform == 'Replace':
		random_words = torch.randint(len(tokenizer), labels.shape, dtype=torch.long)
		inputs[masked_indices] = random_words[masked_indices]
	elif tform == 'None':
		return inputs, labels, masked_indices
	else:
		raise ValueError('Transform not implemented Yet : {}'.format(tform_type))

	return inputs, labels, masked_indices


# code burrowed from : 
# https://github.com/msps9341012/olfmlm/blob/master/data_utils/datasets.py
def run_strip_accents(text):
	"""Strips accents from a piece of text."""
	text = unicodedata.normalize("NFD", text)
	output = []
	for char in text:
		cat = unicodedata.category(char)
		if cat == "Mn":
			continue
		output.append(char)
	return "".join(output)

# code burrowed from : 
# https://github.com/msps9341012/olfmlm/blob/master/data_utils/datasets.py
def get_caps(s, t):
	si = 0
	ti = 0
	tii = 0
	caps = [0] * len(t)
	while si < len(s) and ti < len(t):
		if t[ti][tii] == s[si]:
			if s[si].isupper():
				caps[ti] = 1
			si += 1
			tii += 1
		elif t[ti][tii] == "#" or ord(t[ti][tii]) >= 128:
			tii += 1
		elif s[si] in [" ", "#"] or ord(s[si]) >= 128:
			si += 1
		elif t[ti] == "<unk>":
			tii = 0
			ti += 1
			if ti >= len(t):
				break
		else:
			while s[si] != t[ti][tii]:
				si += 1
				if si >= len(s):
					break

		if tii == len(t[ti]):
			tii = 0
			ti += 1
	return caps

def scale(counter, min_=0, max_=10, smoothfactor=0):
	c_min = min(counter, key=counter.get)
	c_min = counter[c_min] - smoothfactor
	c_max = max(counter, key=counter.get)
	c_max = counter[c_max]
	new_counter = {}
	scaling = lambda x: ((max_ - min_) * (x - c_min) / (c_max - c_min + 1e-8)) + min_
	for k, v in counter.items():
		new_counter[k] = scaling(v)
	return new_counter