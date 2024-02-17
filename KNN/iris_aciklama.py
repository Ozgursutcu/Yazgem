# sklearn.datasets'ten load_iris fonksiyonunu içe aktar
from sklearn.datasets import load_iris

# Iris veri setini yükle
iris = load_iris()

# Öznitelik isimlerini yazdır
print(iris.feature_names)

# Hedef sınıf isimlerini yazdır
print(iris.target_names)

# Hedef sınıf değerlerini yazdır
print(iris.target)

# Öznitelik verilerini yazdır
print(iris.data)

# Öznitelikleri X'e, hedef sınıfları Y'ye ata
X = iris.data
Y = iris.target

# Eğitim ve test veri setlerini bölmek için gerekli fonksiyonu içe aktar
from sklearn.model_selection import train_test_split

# Veri setini eğitim ve test setlerine böl
# Test seti boyutu %20 olarak ayarlanmıştır ve random_state ile rastgelelik kontrol altına alınmıştır
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=0)

# Eğitim ve test setlerinin boyutunu yazdır
print("Eğitim veri seti boyutu=", len(X_train))
print("Test veri seti boyutu=", len(X_test))

# KNeighborsClassifier'ı içe aktar
from sklearn.neighbors import KNeighborsClassifier

# KNN modelini oluştur
model = KNeighborsClassifier()

# Modeli eğitim veri seti ile eğit
model.fit(X_train, Y_train)

# Test seti üzerinden tahminlerde bulun
Y_tahmin = model.predict(X_test)

# Confusion matrix için gerekli fonksiyonu içe aktar
from sklearn.metrics import confusion_matrix

# Hata matrisini hesapla ve yazdır
hata_matrisi = confusion_matrix(Y_test, Y_tahmin)
print(hata_matrisi)

# Görselleştirme için gerekli kütüphaneleri içe aktar
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Hata matrisi için etiketler
index = ['setosa', 'versicolor', 'virginica']
columns = ['setosa', 'versicolor', 'virginica']

# Hata matrisini DataFrame olarak oluştur
hata_goster = pd.DataFrame(hata_matrisi, columns, index)

# Hata matrisini görselleştir
plt.figure(figsize=(10, 6))
sns.heatmap(hata_goster, annot=True)
