import matplotlib.pyplot as plt
import numpy as np
"""
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([0.5, 1.0, 2.0])
print(sigmoid(x))

x = np.linspace(-10, 10, 100)
y = sigmoid(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sigmoid(x)')
plt.title('Sigmoid Function')
plt.grid(True)
plt.show()

#----------------------------------------------

def relu(x):
    return np.maximum(0, x)
x = np.array([-10.0, 1.0, -2.0])
y = relu(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('relu(x)')
plt.title('ReLU Function')
plt.grid(True)
plt.show()

#----------------------------------------------

def tanh(x):
    return np.tanh(x)
x = np.array([0.5, 1.0, 2.0])
y = tanh(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('tanh(x)')
plt.title('Hyperbolic Tangent Function')
plt.grid(True)
plt.show()

#----------------------------------------------
def leaky_relu(x, alpha=0.01):
    return np.where(x >= 0, x, alpha * x)

y = leaky_relu(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('leaky_relu(x)')
plt.title('Leaky ReLU Function')
plt.grid(True)
plt.show()


"""
#----------------------------------------------

def elu(x, alpha=1.0):
    return np.where(x >= 0, x, alpha * (np.exp(x) - 1))

x = np.linspace(-10, 10, 100)
y = elu(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('elu(x)')
plt.title('Exponential Linear Unit (ELU) Function')
plt.grid(True)
plt.show()
