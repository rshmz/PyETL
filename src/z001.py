import pandas as pd

df = pd.DataFrame(
    {
        "department": ["HR", "Engineering", "HR", "Engineering", "Sales"],
        "salary": [50000, 80000, 60000, 70000, 45000],
    }
)

print(df, "\n")

# グループ化して平均を計算
df_grouped = df.groupby("department")["salary"].mean()
print(df_grouped)
