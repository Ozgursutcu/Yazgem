from PIL import Image

# 'strawberry.jpg' adlı görüntü dosyasını açar
filename = "strawberry.jpg"
with Image.open(filename) as img:
    img.load()  # Görüntüyü belleğe yükler

# Görüntüyü CMYK renk formatına dönüştürür
cmyk_img = img.convert("CMYK")
# Görüntüyü gri tonlamalı (grayscale) formatına dönüştürür
gray_img = img.convert("L")

# CMYK formatındaki görüntüyü gösterir
cmyk_img.show()
# Gri tonlamalı görüntüyü gösterir
gray_img.show()

# Orijinal görüntünün renk bantlarını alır (örn. 'RGB')
img.getbands()

# CMYK formatındaki görüntünün renk bantlarını alır ('C', 'M', 'Y', 'K')
cmyk_img.getbands()

# Gri tonlamalı görüntünün renk bantlarını alır ('L')
gray_img.getbands()

# Orijinal görüntüyü RGB kanallarına ayırır
red, green, blue = img.split()
# Kırmızı kanalı gösterir
red

# Kırmızı kanalın modunu alır ('L' çünkü tek bir kanal)
red.mode

# Kırmızı kanalın tüm değerlerini 0 yaparak yeni bir 'zeroed_band' oluşturur
zeroed_band = red.point(lambda _: 0)

# Yalnızca kırmızı kanalın aktif olduğu yeni bir görüntü oluşturur
red_merge = Image.merge(
    "RGB", (red, zeroed_band, zeroed_band)
)

# Yalnızca yeşil kanalın aktif olduğu yeni bir görüntü oluşturur
green_merge = Image.merge(
    "RGB", (zeroed_band, green, zeroed_band)
)

# Yalnızca mavi kanalın aktif olduğu yeni bir görüntü oluşturur
blue_merge = Image.merge(
    "RGB", (zeroed_band, zeroed_band, blue)
)

# Yalnızca kırmızı kanalın aktif olduğu görüntüyü gösterir
red_merge.show()
# Yalnızca yeşil kanalın aktif olduğu görüntüyü gösterir
green_merge.show()
# Yalnızca mavi kanalın aktif olduğu görüntüyü gösterir
blue_merge.show()
