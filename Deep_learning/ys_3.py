import numpy as np

# Sigmoid fonksiyonu
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Giriş ve çıkış verileri
X = np.array([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]])
                
y = np.array([[0],
              [1],
              [1],
              [0]])

np.random.seed(1)

# Ağırlıkların rastgele başlatılması
weights0 = 2*np.random.random((3,4)) - 1
weights1 = 2*np.random.random((4,1)) - 1

# Eğitim döngüsü
for iter in range(10000):

    # İleri yayılım
    layer0 = X
    layer1 = sigmoid(np.dot(layer0,weights0))
    layer2 = sigmoid(np.dot(layer1,weights1))

    # Hata hesaplama
    layer2_error = y - layer2
    
    if (iter% 1000) == 0:
        print("Error:" + str(np.mean(np.abs(layer2_error))))
        
    # Geri yayılım
    layer2_delta = layer2_error*sigmoid(layer2)
    layer1_error = layer2_delta.dot(weights1.T)
    layer1_delta = layer1_error * sigmoid(layer1)

    # Ağırlıkların güncellenmesi
    weights1 += layer1.T.dot(layer2_delta)
    weights0 += layer0.T.dot(layer1_delta)