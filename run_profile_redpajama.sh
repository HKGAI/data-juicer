log_dir='/export/project/lijiawei421/projects/innohk/data_juicer'
run_mode="1"
log_name="redpajama_arxiv"
if [ "$run_mode" = "1" ]; then
  nohup python tools/process_data.py --config configs/reproduced_redpajama/redpajama-arxiv.yaml \
        > ${log_dir}/${log_name}.log 2>&1 &
elif [ "$run_mode" = "2" ]; then
    python tools/process_data.py --config configs/reproduced_redpajama/redpajama-arxiv.yaml
fi
