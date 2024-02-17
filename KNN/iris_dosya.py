from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from joblib import dump, load

# Iris veri setini yükle
iris = load_iris()
X = iris.data
Y = iris.target

# Veri setini eğitim ve test setlerine ayır
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=0)

# Modeli oluştur ve eğit
model = KNeighborsClassifier()
model.fit(X_train, Y_train)

# Modeli dosyaya kaydet
dump(model, 'knn_model.joblib')

# Kaydedilen modeli yükle
loaded_model = load('knn_model.joblib')

# Test verisi üzerinde tahminde bulun
Y_pred = loaded_model.predict(X_test)

# Tahmin performansını değerlendir
from sklearn.metrics import confusion_matrix
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

conf_matrix = confusion_matrix(Y_test, Y_pred)

# Hata matrisini görselleştir
labels = ['setosa', 'versicolor', 'virginica']
conf_df = pd.DataFrame(conf_matrix, index=labels, columns=labels)
plt.figure(figsize=(10,6))
sns.heatmap(conf_df, annot=True, fmt='g')
plt.show()

