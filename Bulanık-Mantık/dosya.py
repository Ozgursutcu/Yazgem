import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

# Giriş verilerini tanımla
hava_sicakligi = np.arange(0, 101, 1)
nem_orani = np.arange(0, 101, 1)
rüzgar_hizi = np.arange(0, 101, 1)

# Üyelik fonksiyonlarını tanımla
hava_sicakligi_soguk = fuzz.trimf(hava_sicakligi, [0, 0, 50])
hava_sicakligi_ılıman = fuzz.trimf(hava_sicakligi, [0, 50, 100])
hava_sicakligi_sıcak = fuzz.trimf(hava_sicakligi, [50, 100, 100])

nem_orani_dusuk = fuzz.trimf(nem_orani, [0, 0, 50])
nem_orani_orta = fuzz.trimf(nem_orani, [0, 50, 100])
nem_orani_yuksek = fuzz.trimf(nem_orani, [50, 100, 100])

rüzgar_hizi_dusuk = fuzz.trimf(rüzgar_hizi, [0, 0, 50])
rüzgar_hizi_orta = fuzz.trimf(rüzgar_hizi, [0, 50, 100])
rüzgar_hizi_yuksek = fuzz.trimf(rüzgar_hizi, [50, 100, 100])

# Çıkış verilerini tanımla ve basit bir örnek çıktı hesaplama yap (Bu kısmı sizin doldurmanız gerekiyor)

# Sonucu görselleştir (Bu kısım çıktı hesaplamalarınıza göre güncellenmelidir)
fig, ax = plt.subplots()
ax.plot(hava_sicakligi, hava_sicakligi_soguk, 'b', linewidth=1.5, label='Soğuk')
ax.plot(hava_sicakligi, hava_sicakligi_ılıman, 'g', linewidth=1.5, label='Ilıman')
ax.plot(hava_sicakligi, hava_sicakligi_sıcak, 'r', linewidth=1.5, label='Sıcak')
ax.set_title('Hava Sıcaklığı Üyelik Dereceleri')
ax.legend()

plt.show()
