import pandas as pd
from io import StringIO


data = """Sample   Animal   Intelligence
1 Dog Dumb
2 Dog Dumb
3 Cat  Smart
4 Cat    Smart
5 Dog Smart
6 Cat Smart"""

dframe = pd.read_table(StringIO(data), sep="\s+")
# dframe = pd.read_csv(StringIO(data), sep='\s+')
print(dframe)
print("\n")

crosstab_result = pd.crosstab(
    dframe.Animal, dframe.Intelligence, margins=True
)  # margins=Trueで合計を表示
print(crosstab_result)
