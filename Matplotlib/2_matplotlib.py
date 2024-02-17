import matplotlib.pyplot as plt
# Veri noktaları
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# İkinci bir veri seti
x2 = [1, 2, 3, 4]
y2 = [20, 15, 30, 25]

plt.plot(x, y, label='İlk Veri Seti') # İlk veri setini çiz
plt.plot(x2, y2, label='İkinci Veri Seti') # İkinci veri setini çiz
plt.legend() # Grafikte açıklama kutusu (legend) ekle
plt.show()



plt.scatter(x, y) # Dağılım grafiği oluştur
plt.title('Dağılım Grafiği')
plt.xlabel('X Ekseni')
plt.ylabel('Y Ekseni')
plt.show()
