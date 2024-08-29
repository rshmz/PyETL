from numpy.random import randn
import matplotlib.pyplot as plt

dataset1 = randn(100)
# plt.hist(dataset1)
# plt.show()

# 色を変える
dataset2 = randn(80)
# _ = plt.hist(dataset2, color='indianred')
# plt.show()

# 確率密度で描画
# _ = plt.hist(dataset1, density=True)
# plt.show()


# サンプル数が違うつので、比較できるように確率密度で描画
# 透明度を調節して重なっても見えるように
plt.hist(dataset1, density=True, alpha=0.5, bins=20)
_ = plt.hist(dataset2, density=True, alpha=0.5, bins=20, color="indianred")
plt.show()
