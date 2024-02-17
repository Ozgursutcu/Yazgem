import numpy as np

sinav_sonuclari = np.array([75, 80, 65, 90, 95])

print("Sınav Sonuçları:", sinav_sonuclari)


ortalama = np.mean(sinav_sonuclari)
print("Sınıfın Ortalama Sınav Sonucu:", ortalama)

en_yuksek = np.max(sinav_sonuclari)
en_dusuk = np.min(sinav_sonuclari)
print("En Yüksek Sınav Sonucu:", en_yuksek)
print("En Düşük Sınav Sonucu:", en_dusuk)

std_sapma = np.std(sinav_sonuclari)
print("Sınav Sonuçlarının Standart Sapması:", std_sapma)

yeni_sonuclar = sinav_sonuclari + 10
print("Yeniden Değerlendirilmiş Sınav Sonuçları (110 Üzerinden):", yeni_sonuclar)

ust_not_siniri = 80
ust_not_sayisi = np.sum(sinav_sonuclari > ust_not_siniri)
print(f"{ust_not_siniri} üzerinden not alan öğrenci sayısı:", ust_not_sayisi)
