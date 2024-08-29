import pandas as pd
import sqlite3

df = pd.read_csv("./data/raw/reserve.csv")

# メモリ内にSQLiteデータベースを作成
conn = sqlite3.connect(":memory:")

# DataFrameをSQLiteデータベースに保存
df.to_sql("reserve_tb", conn, index=False, if_exists="replace")

query = """
WITH cnt_tb AS(
  SELECT
    customer_id, people_num,
    COUNT(reserve_id) AS rsv_cnt
  FROM reserve_tb
  GROUP BY customer_id, people_num
)
SELECT
  customer_id,
  max(CASE people_num WHEN 1 THEN rsv_cnt ELSE 0 END) AS people_num_1,
  max(CASE people_num WHEN 2 THEN rsv_cnt ELSE 0 END) AS people_num_2,
  max(CASE people_num WHEN 3 THEN rsv_cnt ELSE 0 END) AS people_num_3,
  max(CASE people_num WHEN 4 THEN rsv_cnt ELSE 0 END) AS people_num_4
FROM cnt_tb
GROUP BY customer_id
"""

result_df = pd.read_sql_query(query, conn)

# 抽出したデータを表示
print(result_df)

conn.close()
