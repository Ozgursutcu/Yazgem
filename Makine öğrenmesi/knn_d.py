#modülleri import ediyoruz.
from sklearn import datasets
from sklearn.cluster import KMeans

#data setini yüklüyoruz.
iris_df = datasets.load_iris()

#modelimizi bildiriyoruz.
model = KMeans(n_clusters=3)

model.fit(iris_df.data)

predicted_label = model.predict([[7.2, 3.5, 0.8, 1.6]])

all_predictions = model.predict(iris_df.data)

#tahminleri yazdırıyoruz.
print(predicted_label)
print(all_predictions)

from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans
from matplotlib import pyplot
X, _ = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)
model = KMeans(n_clusters=2)
model.fit(X)
yhat = model.predict(X)
clusters = unique(yhat)
for cluster in clusters:
    row_ix = where(yhat == cluster)
pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
pyplot.show()