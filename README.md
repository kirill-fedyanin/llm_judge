# LLM Judge quick repo
This is lightweight repack for mt-bench by lmsys. I've left only the files relevant to lm juding.


## How to use
```bash
pip install fschat[model_worker,llm_judge] # install
git clone git@github.com:kirill-fedyanin/llm_judge.git  # get this repo
export OPENAI_API_KEY=XXXXXX  # set the OpenAI API key
MODEL_NAME='tiiuae/falcon2-11b-chat-v2' # add model
MODEL_ID='falcon2-chat' # add any name to display locally

# Adjut number gpu
python gen_model_answer.py --model-path $MODEL_NAME  --model-id $MODEL_ID   --num-gpus-total 4
python gen_judgment.py --model-list $MODEL_ID --parallel 2
python show_result.py
```


## Original sources
| [Paper](https://arxiv.org/abs/2306.05685) | [Leaderboard](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard) | [Repo](https://github.com/lm-sys/FastChat/) | [Chatbot Arena Conversation Dataset](https://huggingface.co/datasets/lmsys/chatbot_arena_conversations) | [MT-bench Human Annotation Dataset](https://huggingface.co/datasets/lmsys/mt_bench_human_judgments)


## Citation
Please cite the original paper if you find the code or datasets helpful.
```
@misc{zheng2023judging,
      title={Judging LLM-as-a-judge with MT-Bench and Chatbot Arena}, 
      author={Lianmin Zheng and Wei-Lin Chiang and Ying Sheng and Siyuan Zhuang and Zhanghao Wu and Yonghao Zhuang and Zi Lin and Zhuohan Li and Dacheng Li and Eric. P Xing and Hao Zhang and Joseph E. Gonzalez and Ion Stoica},
      year={2023},
      eprint={2306.05685},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
