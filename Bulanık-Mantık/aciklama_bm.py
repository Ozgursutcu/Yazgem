# Gerekli kütüphaneleri içe aktar
import numpy as np # NumPy kütüphanesi matematiksel işlemler için kullanılır.
import skfuzzy as fuzz # Skfuzzy, bulanık mantık işlemleri için kullanılır.
from skfuzzy import control as ctrl # Bulanık kontrol modülü, kurallar ve kontrol sistemi oluşturmak için kullanılır.

# Giriş ve çıkış değişkenlerini tanımla
bulasik_miktari = ctrl.Antecedent(np.arange(0, 100, 1), 'bulaşık miktarı')
kirlilik = ctrl.Antecedent(np.arange(0, 100, 1), 'kirlilik seviyesi')
yikama = ctrl.Consequent(np.arange(0, 180, 1),'yıkama süresi')

# Üyelik fonksiyonlarını tanımla
bulasik_miktari['az'] = fuzz.trimf(bulasik_miktari.universe, [0, 0, 30])
bulasik_miktari['normal'] = fuzz.trimf(bulasik_miktari.universe, [10, 30, 60])
bulasik_miktari['çok'] = fuzz.trimf(bulasik_miktari.universe, [50, 60, 100])
kirlilik['az'] = fuzz.trimf(kirlilik.universe, [0, 0, 30])
kirlilik['normal'] = fuzz.trimf(kirlilik.universe, [10, 30, 60])
kirlilik['çok'] = fuzz.trimf(kirlilik.universe, [50, 60, 100])

yikama['kisa'] = fuzz.trimf(yikama.universe, [0, 0, 50])
yikama['normal'] = fuzz.trimf(yikama.universe, [40, 50, 100])
yikama['uzun'] = fuzz.trimf(yikama.universe, [60, 80, 180])

# Kuralları tanımla
kural1 = ctrl.Rule(bulasik_miktari['az'] & kirlilik['az'], yikama['kisa'])
kural2 = ctrl.Rule(bulasik_miktari['normal'] & kirlilik['az'], yikama['normal'])
kural3 = ctrl.Rule(bulasik_miktari['çok'] & kirlilik['az'], yikama['normal'])
kural4 = ctrl.Rule(bulasik_miktari['az'] & kirlilik['normal'], yikama['normal'])
kural5 = ctrl.Rule(bulasik_miktari['normal'] & kirlilik['normal'], yikama['uzun'])
kural6 = ctrl.Rule(bulasik_miktari['çok'] & kirlilik['normal'], yikama['uzun'])
kural7 = ctrl.Rule(bulasik_miktari['az'] & kirlilik['çok'], yikama['normal'])
kural8 = ctrl.Rule(bulasik_miktari['normal'] & kirlilik['çok'], yikama['uzun'])
kural9 = ctrl.Rule(bulasik_miktari['çok'] & kirlilik['çok'], yikama['uzun'])

# Kontrol sistemi oluştur
sonuc = ctrl.ControlSystem([kural1, kural2, kural3, kural4, kural5, kural6, kural7, kural8, kural9])

# Kontrol sistemi simülasyonunu oluştur
model_sonuc = ctrl.ControlSystemSimulation(sonuc) 

# Giriş değerlerini belirle
model_sonuc.input['bulaşık miktarı'] = 50
model_sonuc.input['kirlilik seviyesi'] = 80

# Sistemi çalıştır
model_sonuc.compute()

# Çıkışı yazdır
print(model_sonuc.output['yıkama süresi'])
