# Python ile basit bir tek katmanlı sinir ağı (Perceptron) örneği

import numpy as np

# Sigmoid aktivasyon fonksiyonu ve türevi
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Eğitim veri seti: giriş ve beklenen çıkışlar
training_inputs = np.array([[0,0],
                            [0,1],
                            [1,0],
                            [1,1]])

training_outputs = np.array([[0, 1, 1, 0]]).T

# Ağırlıkları rastgele başlatma
np.random.seed(1)
weights = 2 * np.random.random((2, 1)) - 1

print("Başlangıç ağırlıkları:")
print(weights)

# Eğitim süreci
learning_rate = 0.1
for iteration in range(10000):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, weights))
    
    # Hata
    error = training_outputs - outputs
    adjustments = error * sigmoid_derivative(outputs)
    
    # Ağırlıkları güncelleme
    weights += np.dot(input_layer.T, adjustments) * learning_rate

print("Eğitimden sonra ağırlıklar:")
print(weights)

print("Test sonuçları:")
for i in range(len(training_inputs)):
    print(f"Giriş: {training_inputs[i]} -> Beklenen Çıkış: {training_outputs[i]}, Elde Edilen Çıkış: {sigmoid(np.dot(training_inputs[i], weights))}")
