'''
Author: callus
Date: 2023-07-19 18:53:34
LastEditors: callus
Description: some description
FilePath: /drug-shortage-forecast/demoRossmann.py
'''

#导入需要的库
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#读取Rossmann数据,选择相关特征
dataframe = pd.read_csv('rossmann.csv')
features = ['store', 'day_of_week', 'promo', 'school_holiday'] 
label = ['sales']

#分割训练测试数据
X_train, X_test, y_train, y_test = train_test_split(dataframe[features], dataframe[label], test_size=0.2, random_state=0)

#定义模型参数
params = {
    'eta': 0.1,
    'max_depth': 5,
    'objective': 'reg:squarederror'
}

#初始化模型
model = XGBRegressor(**params)

#训练模型
model.fit(X_train, y_train)

#进行预测
predictions = model.predict(X_test)

#计算RMSE
rmse = mean_squared_error(y_test, predictions, squared=False)

print("药品销售预测RMSE:", rmse)