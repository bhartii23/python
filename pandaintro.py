import pandas as pd

X = pd.read_csv("covid_19_clean_complete.csv")
# print(X)
# print(X.dtypes)
# print(X.info())
y = X["Deaths"]
# print(y)
# print(y.shape)
above_1000=X[X["Deaths"]>1000]
print(above_1000) 


