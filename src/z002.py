import numpy as np
from numpy.random import randn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./data/raw/logs-insights-results.csv", sep=",")

# Query_timeの抽出
df["Query_time"] = df["@message"].str.extract(r"Query_time:\s([0-9.]+)")
# SQL文の抽出
df["SQL"] = df["@message"].str.extract(r"(SELECT.*?;|select.*?;)", expand=False)

# カラムを絞ってQuery_timeでソート
df = df[["@timestamp", "Query_time", "SQL"]].sort_values(
    "Query_time", ascending=False, inplace=False
)

# CSV出力
df.to_csv(
    "./data/processed/logs-insights-results.csv", sep=",", index=False, encoding="utf-8"
)
