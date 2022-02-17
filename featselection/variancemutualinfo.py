from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif as MIC
import numpy as np
import pandas as pd

data = pd.read_csv("mci_labelled_feature_gen.csv")
data = data.fillna(0)
X = data.iloc[:,:-2]
y = data.iloc[:,-2]

# 方差选择特征
X1 = VarianceThreshold().fit_transform(X)
selector = VarianceThreshold(np.median(X.var().values))
X_fsvar = selector.fit_transform(X)
all_name = X.columns.values.tolist()  # 获得所有的特征名称
select_name_index0 = selector.get_support(indices=True)  # 留下特征的索引值，list格式
select_name0 = []
for i in select_name_index0:
    select_name0.append(all_name[i])
print(X1.shape)
print(X_fsvar.shape)
print(select_name0)

# 互信息特征选择
mic = MIC(X_fsvar, y, random_state=0)
k = mic.shape[0] - sum(mic <= 0)   # 获得与标签列相关的特征列个数
skb = SelectKBest(MIC, k=k)  # 特征选择
x_train = skb.fit_transform(X_fsvar, y)
select_name_index = skb.get_support(indices=True)
select_name = []
for i in select_name_index:
    select_name.append(select_name0[i])
print(select_name)
print(len(select_name))


