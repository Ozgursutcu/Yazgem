from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split

from sklearn.datasets import load_iris

import numpy as np

import matplotlib.pyplot as plt

irisData = load_iris()

# hedef diziler oluşturuyoruz.

X = irisData.data

y = irisData.target

# eğitim ve test setine bölüyoruz.

X_train, X_test, y_train, y_test = train_test_split(

X, y, test_size = 0.2, random_state=42)

neighbors = np.arange(1, 9)

train_accuracy = np.empty(len(neighbors))

test_accuracy = np.empty(len(neighbors))

# K değerini döngüye sokuyoruz.

for i, k in enumerate(neighbors):

    knn = KNeighborsClassifier(n_neighbors=k)

knn.fit(X_train, y_train)

# hesaplama eğitimi ve test verilerinin doğruluğu

train_accuracy[i] = knn.score(X_train, y_train)

test_accuracy[i] = knn.score(X_test, y_test)

# test sonuçlarına görsellik katıyoruz.

plt.plot(neighbors, test_accuracy, label = 'Testing dataset Accuracy')

plt.plot(neighbors, train_accuracy, label = 'Training dataset Accuracy')

plt.legend()

plt.xlabel('n_neighbors')

plt.ylabel('Accuracy')

plt.show()