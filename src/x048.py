import numpy as np
from numpy.random import randn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# サンプルデータを用意
data = pd.DataFrame({'data1':randn(1000), 'data2':randn(1000)})

# 同時分布(結合分布)
sns.jointplot(data,  x='data1', y='data2')
sns.jointplot(data,  x='data1', y='data2', kind='hex')

plt.show()