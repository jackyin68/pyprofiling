from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from lightgbm import LGBMClassifier, LGBMRegressor
from sklearn.metrics import roc_curve
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
from utils import gen_model_datum
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import profile

class Regressor:
    def __init__(self, step=10, feature_num=6):
        self.step = step
        self.feature_num = feature_num
        self.X, self.y = gen_model_datum(step=step, feature_num=6)

    def model_datum(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2,
                                                                                random_state=123)

    def model_train(self):
        self.model = LGBMRegressor(boosting_type='gbdt', objective='regression', num_leaves=25,
                                   learning_rate=0.2, n_estimators=70, max_depth=15,
                                   metric='rmse', bagging_fraction=0.8, feature_fraction=0.8, reg_lambda=0.9)

        self.model.fit(self.X_train, self.y_train)

    def model_predict(self):
        self.y_pred = self.model.predict(self.X_test, num_iteration=self.model.best_iteration_)

    def model_evaluate(self):
        print('预测结果的rmse是:')
        print(mean_squared_error(self.y_test, self.y_pred) ** 0.5)

    def plot_predict(self):
        a = pd.DataFrame()
        a['预测值'] = list(self.y_pred)
        a['实际值'] = list(self.y_test)
        plt.plot(a['实际值'], a['预测值'])

    @profile
    def model_param_search(self):
        parameters = {"boosting_type": 'gbdt', "objective": 'regression', "num_leaves": 1200,
                      "learning_rate": 0.1, "n_estimators": 200, "max_depth": 15,
                      "metric": 'rmse', "bagging_fraction": 0.8, "feature_fraction": 0.8, "reg_lambda": 0.9
                      }
        model = LGBMRegressor(**parameters)
        parameters_s = {'num_leaves': range(5, 30, 5), 'n_estimators': range(10, 200, 30),
                        'learning_rate': [0.01, 0.1, 0.2]}
        grid_search = GridSearchCV(model, param_grid=parameters_s, cv=5)
        grid_search.fit(self.X_train, np.array(self.y_train))
        grid_search.best_params_
        print(grid_search.best_params_)


if __name__ == '__main__':
    regressor = Regressor()
    regressor.model_datum()
    regressor.model_train()
    regressor.model_predict()
    regressor.model_evaluate()

    start = time.time()
    regressor.model_param_search()
    end = time.time()
    print("计算时间:{}".format(end - start))
