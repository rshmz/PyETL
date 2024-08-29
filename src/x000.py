import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

obj = Series([4, 7, -5, 3])

print("index", obj.index)
print(obj)
print("values", obj.values)

data = {
    "COL1": ["A", "B", "C", "D"],
    "COL2": ["E", "F", "G", "H"],
    "COL3": ["I", "J", "K", "L"],
}

df = DataFrame(data, index=["ONE", "TWO", "THREE", "FOUR"])
print(df)
