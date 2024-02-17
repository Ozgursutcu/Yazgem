import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

#from keras.utils import np_utils
from keras.models import load_model
from tensorflow.keras.utils import to_categorical



# Iris veri setini yükle
iris = load_iris()
X = iris.data
Y = iris.target

# Çıktıyı one-hot encoding formatına dönüştür
Y_one_hot = to_categorical(Y)

# Veri setini eğitim ve test setlerine ayır
X_train, X_test, Y_train, Y_test = train_test_split(X, Y_one_hot, test_size=0.20, random_state=0)
# Kaydedilen modeli yükle
loaded_model = load_model('iris_model.h5')

# Test seti üzerinde tahminde bulun
predictions = loaded_model.predict(X_test)

# Tahminleri etiketlere dönüştür (en yüksek olasılıklı sınıfı seç)
predicted_classes = np.argmax(predictions, axis=1)

# Gerçek sınıfları one-hot encoding formatından geri dönüştür
true_classes = np.argmax(Y_test, axis=1)

# Performansı değerlendir
from sklearn.metrics import accuracy_score
print("Doğruluk:", accuracy_score(true_classes, predicted_classes))
    
