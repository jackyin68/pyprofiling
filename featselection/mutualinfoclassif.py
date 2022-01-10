import pandas as pd
from sklearn import  datasets
import numpy as np
import seaborn as sns
from sklearn.feature_selection import mutual_info_classif
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = iris.data
y = iris.target

new_y = [y[i:i+1] for i in range(len(y))]
data = np.hstack((X, new_y))
data_df = pd.DataFrame(data)

#0到3表示特征，4表示目标变量,画图查看相关性，如下图所示
# plt.figure(figsize=(30,20))
sns.set(font='SimHei',font_scale=1.0)
fig, ax = plt.subplots(figsize = (18,20))
sns.heatmap(data_df.corr(), annot=True, vmax=1,vmin = 0, xticklabels= True, yticklabels= True, square=True, cmap="YlGnBu")
plt.savefig("../log/attention_matrix.png")
plt.show()

mutual_info = mutual_info_classif(X, y, discrete_features= False)
print(mutual_info)