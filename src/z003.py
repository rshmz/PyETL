import pandas as pd
import json
from typing import Set

# CSVファイルの読み込み
df = pd.read_csv("./data/raw/customer_info.csv")

# seriesの各要素をdictに変換しPythonで扱えるようにparse
df["customer_info_dict"] = df["customer_info"].apply(lambda x: json.loads(x))


# var_id が数値かどうかを確認
def contains_numeric_var_id(json_array):
    return any(isinstance(item.get("var_id"), int) for item in json_array)


# var_id が数字のものを含む行をフィルタリング
df = df[df["customer_info_dict"].apply(contains_numeric_var_id)]


def extract_swatch_ids(customer_info_dict: pd.Series) -> Set:
    swatch_ids = set()
    for sublist in customer_info_dict:
        for item in sublist:
            swatch_ids.add(item["swatch_id"])
    return swatch_ids


# swatch_idを抽出
swatch_ids = extract_swatch_ids(df["customer_info_dict"])

SWATCH_NAMES = {5: "テキストボックス", 10: "テキストエリア", 20: "ドロップダウン"}

# swatch_idごとに列を作成
for swatch_id in swatch_ids:
    col_name = SWATCH_NAMES.get(swatch_id, f"swatch_id_{swatch_id}")
    df[col_name] = df["customer_info_dict"].apply(
        lambda x: [item for item in x if item["swatch_id"] == swatch_id]
    )

# select
cols = ["salon_id"] + list(SWATCH_NAMES.values())

# 結果を出力
df[cols].to_csv("./data/processed/customer_info.csv", index=False)
