import json
import pandas as pd

CATEGORIES = ["Writing", "Roleplay", "Reasoning", "Math", "Coding", "Extraction", "STEM", "Humanities"]


def get_model_df():
    q2result = []
    fin = open("data/mt_bench/model_judgment/gpt-4_single.jsonl", "r")
    for line in fin:
        obj = json.loads(line)
        obj["category"] = CATEGORIES[(obj["question_id"]-81)//10]
        q2result.append(obj)
    df = pd.DataFrame(q2result)
    return df

df = get_model_df()

all_models = df["model"].unique()
benchmarks = {}
for model in all_models:
    benchmarks[model] = {}
    for cat in CATEGORIES:
        # filter category/model, and score format error (<1% case)
        res = df[(df["category"]==cat) & (df["model"]==model) & (df["score"] >= 0)]
        score = res["score"].mean()
        benchmarks[model][cat] = score
    benchmarks[model]['MT-bench'] = df[(df["model"] == model) & (df["score"] >= 0)]['score'].mean()

df = pd.DataFrame(benchmarks).T
print(df)
