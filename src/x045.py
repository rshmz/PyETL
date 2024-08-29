import numpy as np
from numpy.random import randn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dframe_wine = pd.read_csv("./data/raw/winequality-red.csv", sep=";")


def ranker(df):
    df["alc_content_rank"] = np.arange(len(df)) + 1
    return df


# アルコール度数で並べ替える
dframe_alc_rank = dframe_wine.sort_values("alcohol", ascending=False, inplace=False)

dframe_alc_rank.head()


# groupbyのあとrankerを適用
# <stdin>:1: DeprecationWarning: DataFrameGroupBy.apply operated on the grouping columns. This behavior is deprecated, and in a future version of pandas the grouping columns will be excluded from the operation. Either pass `include_groups=False` to exclude the groupings or explicitly select the grouping columns after groupby to silence this warning.
# dframe_alc_rank = dframe_alc_rank.groupby('quality').apply(ranker)
dframe_alc_rank = dframe_alc_rank.groupby("quality")[["alcohol"]].apply(ranker)

dframe_alc_rank.to_csv("./data/processed/temp.csv", sep=";")
# dframe_alc_rank.to_csv('./data/raw/winequality-red_ranked.csv', sep=';')
