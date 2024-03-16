from PIL import Image

# Görüntü dosyasının adını belirle
filename = "buildings.jpg"

# Görüntüyü aç, 'with' kullanarak otomatik olarak kapatmayı sağla
with Image.open(filename) as img:
    img.load()  # Görüntüyü belleğe yükle

# img nesnesinin tipini yazdır (geliştirme amaçlı kontrol)
type(img)

# img nesnesinin Image.Image tipinde olup olmadığını kontrol et
isinstance(img, Image.Image)

# Görüntüyü göster
img.show()

# Görüntünün formatını, boyutunu ve modunu yazdır
print(img.format, img.size, img.mode)

# Görüntüyü belirli bir alana göre kırp
cropped_img = img.crop((300, 150, 700, 1000))

# Kırpılmış görüntünün boyutunu yazdır
cropped_img.size

# Kırpılmış görüntüyü göster
cropped_img.show()

# Kırpılmış görüntüyü orijinalinin dörtte bir boyutunda yeniden boyutlandır
low_res_img = cropped_img.resize(
    (cropped_img.width // 4, cropped_img.height // 4)
)

# Düşük çözünürlüklü görüntüyü göster
low_res_img.show()

# Kırpılmış görüntüyü daha da küçültmek için 'reduce' kullan
low_res_img = cropped_img.reduce(4)

# Kırpılmış görüntüyü ve düşük çözünürlüklü görüntüyü kaydet
cropped_img.save("cropped_image.jpg")
low_res_img.save("low_resolution_cropped_image.png")

# Görüntüyü yukarıdan aşağıya çevir (yorum satırlarını kaldırarak kullanabilirsiniz)
#converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
#converted_img.show()

# Görüntüyü 45 derece döndür (yorum satırlarını kaldırarak kullanabilirsiniz)
#rotated_img = img.rotate(45)
#rotated_img.show()
