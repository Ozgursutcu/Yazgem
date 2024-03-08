
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#datamızı yükleyip kontrol ediyoruz.
df = pd.read_csv('Salary.csv')
#df.head()
df
#girdi değişkenleri ve hedef değişkenleri ayırıyoruz.
X = df.iloc[:, :-1].values
y = df.iloc[:, 1].values
#verileri eğitim ve test seti olarak ayırıyoruz.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1)
# Doğrusal Regresyon Modelini Eğitim Setine aktarıyoruz.
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None)
# Test Seti Sonuçlarını Tahmin Ediyor.
y_pred = lr.predict(X_test)
#Eğitim ve Test setlerinde Model Puanını Kontrol Edelim.
print('Train set score ',lr.score(X_train, y_train ))
print('Test  set score ',lr.score(X_test, y_test ))

# Eğitim seti sonuçlarını görselleştiriyoruz.
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, lr.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
# Test seti sonuçlarını görselleştiriyoruz.
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, lr.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()