import pandas as pd

reserve_tb = pd.read_csv("./data/raw/reserve.csv")

# pivot_table関数で、横持ち変換と集約処理を同時実行
# aggfuncに予約数をカウントする関数を指定
df = pd.pivot_table(
    reserve_tb,
    index="customer_id",
    columns="people_num",
    values="reserve_id",
    aggfunc=lambda x: len(x),
    fill_value=0,
)

print(df)
