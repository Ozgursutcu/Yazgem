"""

Scikit-learn (SciKit-Learn veya SKLearn), Python programlama dilinde veri bilimi ve makine 
öğrenmesi çalışmaları için kullanılan çok yönlü bir kütüphanedir. Veri işleme, regresyon, 
küme analizi gibi birçok makine öğrenmesi algoritmasını içerir. 

"""

""" ---------------------------Veri Setini Bölmek

Veri setini eğitim ve test setlerine bölmek, modelinizi değerlendirirken overfitting'i önlemek için önemlidir.
"""
from sklearn.model_selection import train_test_split

# Örnek veri seti ve etiketler
X, y = [[0, 1], [1, 1], [2, 1]], [0, 1, 0]

# Veri setini eğitim ve test setlerine bölme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
# X_train ve X_test eğitim ve test için özellik setleri
# y_train ve y_test eğitim ve test için etiketler


"""---------------------Bir Modeli Eğitmek

Sklearn, çeşitli makine öğrenmesi algoritmalarını içerir. Bir modeli eğitmek için, 
öncelikle modelinizi seçin ve ardından fit metodu ile eğitin.
"""
from sklearn.ensemble import RandomForestClassifier

# Rastgele Orman sınıflandırıcısı örneği oluşturma
clf = RandomForestClassifier(random_state=42)

# Modeli eğitim seti üzerinde eğitme
clf.fit(X_train, y_train)

# Eğitilmiş modeli kullanarak tahminler yapma
predictions = clf.predict(X_test)

"""-------------------- Model Performansını Değerlendirme

Modelinizi eğittikten sonra, performansını çeşitli metriklerle değerlendirmek önemlidir.
"""
from sklearn.metrics import accuracy_score, confusion_matrix

# Modelin doğruluğunu hesaplama
accuracy = accuracy_score(y_test, predictions)
print(f"Model Doğruluğu: {accuracy}")

# Karışıklık matrisi ile model performansını daha detaylı inceleme
conf_matrix = confusion_matrix(y_test, predictions)
print(f"Karışıklık Matrisi:\n {conf_matrix}")


"""-----------------------  Veri Ön İşleme

Sklearn, veri ön işleme için bir dizi araç sunar. Örneğin, özellikleri ölçeklendirebilirsiniz.

"""


from sklearn.preprocessing import StandardScaler

# Özellik ölçekleyici örneği oluşturma
scaler = StandardScaler()

# Eğitim verisine uydurma ve dönüştürme
X_train_scaled = scaler.fit_transform(X_train)

# Test verisini dönüştürme
X_test_scaled = scaler.transform(X_test)
