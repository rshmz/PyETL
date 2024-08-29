import os
import pandas as pd

reserve_tb = pd.read_csv(os.path.dirname(__file__) + "/../data/raw/reserve.csv")

# 必要な列のみ抽出
df = reserve_tb[
    [
        "reserve_id",
        "hotel_id",
        "customer_id",
        "reserve_datetime",
        "checkin_date",
        "checkin_time",
        "checkout_date",
    ]
]
print(df)
