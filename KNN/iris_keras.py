
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

from tensorflow.keras.utils import to_categorical


# Iris veri setini yükle
iris = load_iris()
X = iris.data
Y = iris.target

# Çıktıyı one-hot encoding formatına dönüştür
Y_one_hot = to_categorical(Y)

# Veri setini eğitim ve test setlerine ayır
X_train, X_test, Y_train, Y_test = train_test_split(X, Y_one_hot, test_size=0.20, random_state=0)

# Modeli oluştur
model = Sequential()
model.add(Dense(8, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))

# Modeli derle
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Modeli eğit
model.fit(X_train, Y_train, epochs=150, batch_size=10, verbose=1)

# Modeli 'iris_model.h5' dosyasına kaydet
model.save('iris_model.h5')
print("model save")

