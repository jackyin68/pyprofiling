from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, SelectPercentile
from sklearn.feature_selection import f_classif

iris = load_iris()
X, y = iris.data, iris.target

# 特征选择
sp = SelectPercentile(f_classif, percentile=90)

# 返回至少含有90%特征信息的特征
X_result = sp.fit_transform(X, y)
print(X_result)

# 保留的特征
features = sp.get_support()
print(features)
