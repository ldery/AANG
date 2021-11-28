# HYPER_CONFIG = {
# 		'auxlr': [1.0, 5e-1], # [2.0, 1.0, 5e-1],
# 		'soptlr': [1e-1, 5e-2],
# 		'classflr': [1e-3, 1e-4],
# 		'nconf_samp': [3, 6],
# 		'primbsz': [128, 256],
# 		'auxbsz': [256]
# }


HYPER_CONFIG_PARTIAL = {
		'auxlr': [0.1, 5e-1, 1.0],
		'soptlr': [1e-1],
		'classflr': [3e-3, 5e-3],
		'wfrac': [0.01, 0.06, 0.1],
		'nconf_samp': [3, 6],
		'primbsz': [128],
		'auxbsz': [256]
}

HYPER_CONFIG_FULL = {
		'auxlr': [0.1, 5e-1, 1.0],
		'soptlr': [1e-1],
		'classflr': [1e-3, 1e-4, 3e-3, 5e-3, 1e-2],
		'nconf_samp': [3, 6],
		'primbsz': [128],
		'auxbsz': [256]
}

HYPER_CONFIG_TEST = {
		'auxlr': [0.1],
		'soptlr': [1e-1],
		'classflr': [1e-3],
		'nconf_samp': [6],
		'primbsz': [128],
		'auxbsz': [256]
}


def get_hyper_config(config_name):
	if config_name == 'full':
		return HYPER_CONFIG_FULL
	elif config_name == 'partial':
		return HYPER_CONFIG_PARTIAL
	elif config_name == 'test':
		return HYPER_CONFIG_TEST

CITATION_INTENT = {
	'primtaskid': 'citation_intent',
	'trainfile':  '/home/ldery/internship/dsp/datasets/citation_intent/train.jsonl',
	'devfile':    '/home/ldery/internship/dsp/datasets/citation_intent/dev.jsonl',
	'testfile':   '/home/ldery/internship/dsp/datasets/citation_intent/test.jsonl',
	'taskdata':   '/home/ldery/internship/dsp/datasets/citation_intent/train.txt',
	'domaindata': '/home/ldery/internship/dsp/datasets/citation_intent/domain.10xTAPT.txt',
	'metric':     'f1',
}


SCIIE = {
	'primtaskid': 'sciie',
	'trainfile':  '/home/ldery/internship/dsp/datasets/sciie/train.jsonl',
	'devfile':    '/home/ldery/internship/dsp/datasets/sciie/dev.jsonl',
	'testfile':   '/home/ldery/internship/dsp/datasets/sciie/test.jsonl',
	'taskdata':   '/home/ldery/internship/dsp/datasets/sciie/train.txt',
	'domaindata': '/home/ldery/internship/dsp/datasets/sciie/domain.10xTAPT.txt',
	'metric':     'f1',
}

CHEMPROT = {
	'primtaskid': 'chemprot',
	'trainfile':  '/home/ldery/internship/dsp/datasets/chemprot/train.jsonl',
	'devfile':    '/home/ldery/internship/dsp/datasets/chemprot/dev.jsonl',
	'testfile':   '/home/ldery/internship/dsp/datasets/chemprot/test.jsonl',
	'taskdata':   '/home/ldery/internship/dsp/datasets/chemprot/train.txt',
	'domaindata': '/home/ldery/internship/dsp/datasets/chemprot/domain.10xTAPT.txt',
	'metric':     'accuracy',
}

