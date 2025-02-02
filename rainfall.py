import pandas as pd import numpy as np
from sklearn.model_selection import train_test_splitfrom sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressorfrom sklearn.linear_model import LinearRegression from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt

df = pd.read_csv("rainfall in india 1901-2015.csv") df.head()
df.fillna(value = 0,inplace =True) df.loc[21]
grouped = df.groupby(df.SUBDIVISION) TN = grouped.get_group("TAMIL NADU")

TN.head() TN.hist(figsize=(12,12))
data = np.asarray(TN[['FEB', 'MAR', 'APR','MAY']])


print(np.shape(data)
 


X = data[:,0:3]

y = data[:,3]

data = np.asarray(TN[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP','OCT', 'NOV', 'DEC']])
print(np.shape(data))
X = None; y = None

for i in range(data.shape[1]-3):if X is None:
X = data[:, i:i+3]

y = data[:, i+3] else:
X = np.concatenate((X, data[:, i:i+3]), axis=0)y = np.concatenate((y, data[:, i+3]), axis=0))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) np.shape(X_test)
rf = RandomForestRegressor(n_estimators = 100, max_depth=10, n_jobs=1) rf.fit(X_train, y_train)
y_pred = rf.predict(X_test) mean_absolute_error(y_test, y_pred)
xx = np.arange(start=0,stop=len(y_pred),step=1)

plt.vlines(x=xx, ymin=y_pred, ymax=y_test, color='black', alpha=0.4)plt.scatter(xx,y_pred,color='navy', alpha=1, label='pred')
plt.scatter( xx,y_test, color='green', alpha=0.8 , label='test')
plt.scatter(xx,np.abs(y_pred-y_test),color='gold',label='abs_error',marker='x')plt.legend() linear_regressor
= LinearRegression() linear_regressor.fit(X_train, y_train) Y_pred = linear_regressor.predict(X_test)
mean_absolute_error(y_test, Y_pred)
 
plt.vlines(x=xx, ymin=y_pred, ymax=y_test, color='black', alpha=0.4) plt.scatter(xx,y_pred,color='navy', alpha=1, label='pred')
plt.scatter( xx,y_test, color='green', alpha=0.8 , label='test') plt.scatter(xx,np.abs(y_pred- y_test),color='gold',label='abs_error',marker='x') plt.legend()
rf = RandomForestRegressor(n_estimators = 100, max_depth=10, n_jobs=1)rf.fit(X, y) y_pred = rf.predict(X) mean_absolute_error(y,
y_pred)
x_tot =np.arange(start=0,stop=len(y_pred),step=1) plt.plot(x_tot,y_pred)plt.plot(x_tot,y,
"r--")
rf = RandomForestRegressor(n_estimators = 100, max_depth=10, n_jobs=1)rf.fit(X, y) y_pred = rf.predict(X)
print("The Final Prediction Value") 100 - mean_absolute_error(y, y_pred)
