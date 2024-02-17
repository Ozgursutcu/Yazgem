"""
Pandas, Python için açık kaynaklı, yüksek performanslı, esnek ve kolay kullanımlı bir veri 
yapıları ve veri analizi kütüphanesidir. Veri manipülasyonu ve analizi için özellikle tasarlanmıştır. 
Pandas, veri analizi işlemlerinde sıklıkla kullanılan DataFrame ve Series gibi veri yapıları sunar.
"""
# Pandas kütüphanesini pd takma adı ile içe aktar
import pandas as pd

# Series oluştur
# Pandas Series, tek boyutlu bir veri yapısıdır ve bir diziyi temsil eder.
seri = pd.Series([1, 3, 5, 7, 9])
print("Pandas Serisi:\n", seri)

# DataFrame oluştur
# DataFrame, iki boyutlu bir veri yapısıdır ve bir tabloyu temsil eder.
data = {
    'İsim': ['Ahmet', 'Mehmet', 'Zeynep', 'Elif'],
    'Yaş': [25, 30, 22, 19],
    'Şehir': ['İstanbul', 'Ankara', 'İzmir', 'Bursa']
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# CSV dosyasından veri okuma
# Bu örnek dosya yolu varsayılandır, gerçek bir dosya yolu kullanmanız gerekir.
# df_from_csv = pd.read_csv('dosya_yolu.csv')
# print(df_from_csv)

# DataFrame başlıklarını yazdır
print("\nDataFrame Başlıkları:", df.columns)

# Belirli bir sütunu seçme
yaslar = df['Yaş']
print("\nYaş Sütunu:\n", yaslar)

# Birden fazla sütunu seçme
secilen_sutunlar = df[['İsim', 'Şehir']]
print("\nİsim ve Şehir Sütunları:\n", secilen_sutunlar)

# İlk 2 satırı seçme
ilk_iki_satir = df.head(2)
print("\nİlk İki Satır:\n", ilk_iki_satir)

# Belirli bir satırı seçme (iloc ile)
ucuncu_satir = df.iloc[2]
print("\nÜçüncü Satır (iloc ile):\n", ucuncu_satir)

# Koşullu seçim yapma
# Örneğin, yaşları 23'ten büyük olan kişileri seçme
yas_23_ustu = df[df['Yaş'] > 23]
print("\nYaşı 23'ten Büyük Olanlar:\n", yas_23_ustu)

# Yeni bir sütun ekleme
df['Meslek'] = ['Mühendis', 'Doktor', 'Öğretmen', 'Mimar']
print("\nMeslek Sütunu Eklenmiş DataFrame:\n", df)

# Sütunları yeniden adlandırma
df.rename(columns={'İsim': 'Ad', 'Yaş': 'Yas'}, inplace=True)
print("\nSütunlar Yeniden Adlandırılmış DataFrame:\n", df)

# Eksik değerleri kontrol etme
# Örneğin, eksik değerler (NaN) içeren bir DataFrame
data_with_nan = {
    'İsim': ['Ahmet', 'Mehmet', None, 'Elif'],
    'Yaş': [25, None, 22, 19],
}
df_nan = pd.DataFrame(data_with_nan)
print("\nEksik Değerleri İçeren DataFrame:\n", df_nan)
print("\nEksik Değerlerin Kontrolü:\n", df_nan.isnull())

# Eksik değerleri bir değerle doldurma
df_nan_filled = df_nan.fillna('Bilinmiyor')
print("\nEksik Değerler Doldurulmuş DataFrame:\n", df_nan_filled)
