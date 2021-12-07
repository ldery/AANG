

primtaskid=$1
mainfldr='/home/ldery/internship/dsp/datasets/'$primtaskid
trainfile=$mainfldr'/train.jsonl'
devfile=$mainfldr'/dev.jsonl'
testfile=$mainfldr'/test.jsonl'
taskdata=$mainfldr'/train.txt'
domaindata=$mainfldr'/domain.10xTAPT.txt'

gpuid=$2
start=$3
end=$4
ext=$5
soptlr=$6
classflr=$7
classfdp=$8 # 0.3
totalbsz=$9
gradAccumSteps=${10}
metric=${11}
devbsz=${12}
wfrac=${13}

auxlr=1.0

pergpubsz=$(($totalbsz / $gradAccumSteps))
iterbsz=$(($totalbsz / $gradAccumSteps))
echo 'These are the pergpu and iter bszs = ' $pergpubsz ' and ' $iterbsz

lr=1e-4
patience=20
devlr=1e-2
iters=150
devftiters=10


cfwd=0.1
temp=0.5
basewd=0.01
devWd=0.1
mstep=3
nconfigsamples=1

spconfig='tapt'
evalevery=50


for k in $(seq $start $end)
do
	echo $k
	base='nconfigsamples='$nconfigsamples'.classfdp='$classfdp'.basewd='$basewd'.prim-aux-lr='$soptlr'.auxiliaries-lr='$auxlr'.lr='$lr'.classflr='$classflr'.seed='$k'.iterbsz='$iterbsz'.spconfig='$spconfig'.warmupfrac='$wfrac'.devlr='$devlr'.metastepevery'$mstep'.pergpubsz='$pergpubsz'.devftiters='$devftiters'.temp'$temp'.'$ext
	echo $base
	CUDA_VISIBLE_DEVICES=$gpuid python -u -m scripts.autoaux --prim-task-id $primtaskid --train_data_file $trainfile --dev_data_file $devfile --test_data_file $testfile --output_dir autoaux_outputs/$primtaskid/$base --model_type roberta-base --model_name_or_path roberta-base  --tokenizer_name roberta-base --per_gpu_train_batch_size $pergpubsz  --gradient_accumulation_steps $gradAccumSteps  --learning_rate $lr --block_size 512 --logging_steps 5000 --classf_lr $classflr --classf_patience $patience --num_train_epochs $iters  --classifier_dropout $classfdp --overwrite_output_dir --classf_iter_batchsz  $iterbsz --classf_ft_lr 1e-6 --classf_max_seq_len 512 --seed $k  --classf_dev_wd $devWd --classf_dev_lr $devlr -searchspace-config $spconfig -task-data $taskdata -in-domain-data $domaindata -num-config-samples $nconfigsamples --dev_batch_sz $devbsz --eval_every $evalevery -prim-aux-lr $soptlr -auxiliaries-lr $auxlr --classf_warmup_frac $wfrac --classf_wd $cfwd --base_wd $basewd --dev_fit_iters $devftiters -step-meta-every $mstep -token_temp $temp --share-output-heads --classf-metric $metric --do_train &> logfldrs/$base'.txt'
	# -use-factored-model 
done


