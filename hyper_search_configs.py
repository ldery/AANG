from copy import deepcopy

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
		'classflr': [1e-3, 3e-3],
		'wfrac': [0.06],
		'nconf_samp': [3, 6],
		'primbsz': [128],
		'auxbsz': [256]
}

HYPER_CONFIG_HYPERPARTISAN = {
		'auxlr': [0.1, 5e-1],
		'soptlr': [1e-1],
		'classflr': [1e-4, 1e-3, 3e-3],
		'wfrac': [0.06],
		'nconf_samp': [1, 3],
		'primbsz': [64],
		'auxbsz': [128]
}

# LUCIO - REMEMBER TO RESET THIS ONCE YOU ARE DONE EXPLORING
HYPER_CONFIG_PARTIAL_BIG = {
		'auxlr': [0.1, 5e-1, 1.0],
		'soptlr': [1e-1, 1.0],
		'classflr': [5e-5, 1e-4, 1e-3],
		'wfrac': [0.06],
		'nconf_samp': [3],
		'primbsz': [128],
		'auxbsz': [256]
}


HYPER_CONFIG_PARTIAL_BIG_1 = {
		'auxlr': [0.1, 5e-1, 1.0],
		'soptlr': [1e-1],
		'classflr': [5e-5, 1e-4, 1e-3],
		'wfrac': [0.06],
		'nconf_samp': [12, 9],
		'primbsz': [128],
		'auxbsz': [256]
}


TEMP_RERUN = {
	'auxlr': [0.1, 5e-1, 1.0],
	'soptlr': [1e-1],
	'classflr': [1e-4],
	'wfrac': [0.06],
	'nconf_samp': [1, 3],
	'primbsz': [128],
	'auxbsz': [256]
}



HYPER_CONFIG_PARTIAL_ONETASK = {
		'auxlr': [0.1],
		'soptlr': [0.01, 0.1, 5e-1, 1.0],
		'wfrac': [0.06],
		'primbsz': [128],
		'auxbsz': [256]
}
# deepcopy(HYPER_CONFIG_PARTIAL_BIG)
HYPER_CONFIG_PARTIAL_ONETASK['nconf_samp'] = [1]
HYPER_CONFIG_PARTIAL_ONETASK['classflr'] = [5e-5, 1e-4, 1e-3]

HYPER_CONFIG_PARTIAL_ONETASK_TEMP = {
	'auxlr': [0.1],
	'soptlr': [0.01, 0.1, 5e-1, 1.0],
	'classflr': [5e-6, 5e-5],
	'nconf_samp': [1],
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
		'classflr': [3e-3],
		'wfrac': [0.06],
		'nconf_samp': [1],
		'primbsz': [128],
		'auxbsz': [256]
}

CONFIG_NAMES = [
	"full", "test", "partial",
	"partial_big", "partial_onetask",
	"partial_hyperpartisan", "partial_big_1", "temp_rerun",
	'partial_onetask_temp'
]

def get_hyper_config(config_name):
	if config_name == 'full':
		return HYPER_CONFIG_FULL
	elif config_name == 'partial':
		return HYPER_CONFIG_PARTIAL
	elif config_name == 'partial_big':
		return HYPER_CONFIG_PARTIAL_BIG
	elif config_name == 'partial_big_1':
		return HYPER_CONFIG_PARTIAL_BIG_1
	elif config_name == 'partial_onetask':
		return HYPER_CONFIG_PARTIAL_ONETASK
	elif config_name == 'partial_hyperpartisan':
		return HYPER_CONFIG_HYPERPARTISAN
	elif config_name == 'temp_rerun':
		return TEMP_RERUN
	elif config_name == 'partial_onetask_temp':
		return HYPER_CONFIG_PARTIAL_ONETASK_TEMP

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

HYPERPARTISAN = {
	'primtaskid': 'hyperpartisan',
	'trainfile':  '/home/ldery/internship/dsp/datasets/hyperpartisan/train.jsonl',
	'devfile':    '/home/ldery/internship/dsp/datasets/hyperpartisan/dev.jsonl',
	'testfile':   '/home/ldery/internship/dsp/datasets/hyperpartisan/test.jsonl',
	'taskdata':   '/home/ldery/internship/dsp/datasets/hyperpartisan/train.txt',
	'domaindata': '/home/ldery/internship/dsp/datasets/hyperpartisan/domain.10xTAPT.txt',
	'metric':     'f1',
}

RCT = {
	'primtaskid': 'rct',
	'trainfile':  '/home/ldery/internship/dsp/datasets/rct/train.jsonl',
	'devfile':    '/home/ldery/internship/dsp/datasets/rct/dev.jsonl',
	'testfile':   '/home/ldery/internship/dsp/datasets/rct/test.jsonl',
	'taskdata':   '/home/ldery/internship/dsp/datasets/rct/train.txt',
	'domaindata': '/home/ldery/internship/dsp/datasets/rct/domain.10xTAPT.txt',
	'metric':     'accuracy',
}

SemEval2016Task6 = {
	'primtaskid': 'SemEval2016Task6',
	'trainfile':  '/home/ldery/projects/ml-stance-detection/datasets/SemEval2016Task6/train.jsonl',
	'devfile':    '/home/ldery/projects/ml-stance-detection/datasets/SemEval2016Task6/dev.jsonl',
	'testfile':   '/home/ldery/projects/ml-stance-detection/datasets/SemEval2016Task6/test.jsonl',
	'taskdata':   '/home/ldery/projects/ml-stance-detection/datasets/SemEval2016Task6/train.txt',
	'domaindata': '/home/ldery/projects/ml-stance-detection/datasets/SemEval2016Task6/train.txt', # Todo [ldery] - change this up
	'metric':     'accuracy',
}

PERSPECTRUM = {
	'primtaskid': 'PERSPECTRUM',
	'trainfile':  '/home/ldery/projects/ml-stance-detection/datasets/PERSPECTRUM/perspectrum_train.jsonl',
	'devfile':    '/home/ldery/projects/ml-stance-detection/datasets/PERSPECTRUM/perspectrum_dev.jsonl',
	'testfile':   '/home/ldery/projects/ml-stance-detection/datasets/PERSPECTRUM/perspectrum_test.jsonl',
	'taskdata':   '/home/ldery/projects/ml-stance-detection/datasets/PERSPECTRUM/perspectrum_train.txt',
	'domaindata': '/home/ldery/projects/ml-stance-detection/datasets/PERSPECTRUM/perspectrum_train.txt', # Todo [ldery] - change this up
	'metric':     'accuracy',
}
