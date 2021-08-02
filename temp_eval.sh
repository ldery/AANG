
taskid='sciie'
metric='+f1'
echo "Evaluating performance on "$taskid
datasz=(10)
for k in "${datasz[@]}"
do
	echo 'Evaluating DAPT for sz = '$datasz
	mkdir -p eval_logs/small_dapt/$taskid
	modelfldr='/home/ldery/internship/dsp/m4m_dsp/'$taskid'/small_dapt/'$k'xTapt/'
# 	mv $modelfldr/dapt_$k $modelfldr/roberta-dapt_$k 
# 	python -m scripts.train --config training_config/classifier.jsonnet  --serialization_dir  model_logs/'DAPT_'$taskid'_'$k'xTAPT' --hyperparameters ROBERTA_CLASSIFIER_SMALL  --dataset $taskid --model $modelfldr/roberta-dapt_$k --gpu_id 0  --perf $metric --evaluate_on_test &>  eval_logs/small_dapt/$taskid/dapt_$k.txt

	echo 'Evaluating DAPT+TAPT for sz = '$datasz
	python -m scripts.train --config training_config/classifier.jsonnet  --serialization_dir  model_logs/'DAPT-TAPT_'$taskid'_'$k'xTAPT' --hyperparameters ROBERTA_CLASSIFIER_SMALL  --dataset $taskid --model $modelfldr/roberta-dapt-tapt_$k --gpu_id 0  --perf $metric --evaluate_on_test &> eval_logs/small_dapt/$taskid/roberta-dapt-tapt_$k.txt
done

# python -m scripts.train --config training_config/classifier.jsonnet  --serialization_dir  model_logs/our_sciie_tapt1 --hyperparameters ROBERTA_CLASSIFIER_SMALL  --dataset sciie --model m4m_dsp/sciie/roberta_base_tapt_sciie_1 --gpu_id 1  --perf +f1 --evaluate_on_test &> eval_logs/sciie/our_tapt1.txt

# echo "Running Our TAPT on Chemprot"
# python -m scripts.train --config training_config/classifier.jsonnet  --serialization_dir  model_logs/our_chemprot_tapt --hyperparameters ROBERTA_CLASSIFIER_SMALL  --dataset chemprot --model m4m_dsp/chemprot/roberta_base_tapt_chemprot  --gpu_id 1  --perf +accuracy --evaluate_on_test  &> eval_logs/chemprot/our_tapt.txt


# python -m scripts.train --config training_config/classifier.jsonnet  --serialization_dir  model_logs/dapt_default.seed1.reinit --hyperparameters ROBERTA_CLASSIFIER_SMALL  --dataset citation_intent --model m4m_dsp/citation_intent/small_dapt/tapt_dapt.10x/default.config8.InnerConfig.0.classfbatchsz=6_1/roberta-checkpoint-best --gpu_id 0  --perf '+f1' --evaluate_on_test &> eval_logs/small_dapt/citation_intent/dapt_default.seed1.reinit.txt