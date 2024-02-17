"""

Numpy, Python programlama dilinde bilimsel hesaplamalar için temel bir kütüphanedir. 
Çok boyutlu dizilerle çalışmayı ve üzerlerinde çeşitli matematiksel işlemler
yapmayı kolaylaştırır. 
"""

# Numpy kütüphanesini içe aktar
import numpy as np

# Numpy dizisi oluştur
arr = np.array([1, 2, 3, 4, 5])
print("Dizi:", arr) # Tek boyutlu bir dizi oluşturur

# Çok boyutlu dizi oluştur
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
#print("Çok boyutlu dizi:\n", arr_2d)

# 0'lardan oluşan bir dizi oluştur
zeros = np.zeros((3, 3))
#print("0'larla dolu dizi:\n", zeros)

# 1'lerden oluşan bir dizi oluştur
ones = np.ones((2, 2))
#print("1'lerle dolu dizi:\n", ones)

# Belirli bir aralıkta sayılarla dizi oluştur
range_array = np.arange(0, 10, 2)
#print("Belirli bir aralıkta sayılarla dizi:", range_array)

# Rastgele sayılarla dizi oluştur
random_array = np.random.rand(3, 3)
#print("Rastgele sayılarla dizi:\n", random_array)

# Dizi boyutunu öğren
#print("Dizi boyutu:", arr_2d.shape)

# Dizi yeniden şekillendirme
reshaped = arr.reshape((5, 1))
#print("Yeniden şekillendirilmiş dizi:\n", reshaped)

# Dizi elemanları toplamı
#print("Dizi elemanları toplamı:", np.sum(arr))

# Diziler arası toplama
result_array = np.add(arr, np.array([5, 5, 5, 5, 5]))
#print("Diziler arası toplama sonucu:", result_array)

# Dizi indeksleme
#print("Dizinin ilk elemanı:", arr[0])

# Dizi kesme
#print("Dizinin ilk üç elemanı:", arr[:3])

# Dizi elemanlarının maksimum ve minimum değerleri
#print("Dizi maksimum değeri:", np.max(arr))
#print("Dizi minimum değeri:", np.min(arr))

# Dizi elemanlarının ortalaması
#print("Dizi ortalaması:", np.mean(arr))
