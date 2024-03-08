import numpy as np

# Aktivasyon fonksiyonunu tanımla
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Tek katmanlı sinir ağı sınıfını tanımla
class SingleLayerNN:
    def __init__(self, input_size, output_size):
        # Ağırlık ve bias değerlerini başlat
        self.weights = np.random.randn(input_size, output_size)
        self.bias = np.zeros((1, output_size))

    def forward(self, inputs):
        # İleri yayılım fonksiyonu
        self.inputs = inputs
        self.output = sigmoid(np.dot(inputs, self.weights) + self.bias)

    def backward(self, targets, learning_rate):
        # Geri yayılım fonksiyonu
        error = targets - self.output  # Hedefler ile çıkış arasındaki hata
        delta = error * self.output * (1 - self.output)  # Hata düzeltme değeri
        self.weights += learning_rate * np.dot(self.inputs.T, delta)  # Ağırlıkları güncelle
        self.bias += learning_rate * np.sum(delta, axis=0)  # Bias'ı güncelle

# Örnek kullanım
input_size = 2
output_size = 1

# Tek katmanlı sinir ağı örneği oluştur
nn = SingleLayerNN(input_size, output_size)

# Giriş verileri ve hedefleri tanımla
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets = np.array([[0], [1], [1], [0]])

# Sinir ağını eğit
epochs = 1000  # Eğitim döngüsü sayısı
learning_rate = 0.1  # Öğrenme oranı

for epoch in range(epochs):
    nn.forward(inputs)  # İleri yayılım
    nn.backward(targets, learning_rate)  # Geri yayılım

# Sinir ağını test et
nn.forward(inputs)
print(nn.output)  # Test sonuçlarını yazdır
