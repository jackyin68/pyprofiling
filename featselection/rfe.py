from sklearn.feature_selection import RFE
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import datasets

iris = datasets.load_iris()

gbdt_RFE = RFE(estimator=GradientBoostingClassifier(random_state= 123),n_features_to_select=2)
gbdt_RFE.fit(iris.data, iris.target)

#特征选择输出结果
print(gbdt_RFE.support_)