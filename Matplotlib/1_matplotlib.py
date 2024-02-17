import matplotlib.pyplot as plt

# Veri noktaları
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y) # x ve y veri noktalarını çizgi grafiği olarak çiz
plt.title('Basit Çizgi Grafiği') # Grafiğe başlık ekle
plt.xlabel('X Ekseni') # X ekseni etiketi
plt.ylabel('Y Ekseni') # Y ekseni etiketi
plt.show() # Grafiği göster
