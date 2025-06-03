import cv2
import numpy as np

# --- Morphology - Morfoloji ---

# Morphology: modifying shapes using structuring elements
# Morfoloji: Yapılandırma elemanı kullanarak şekilleri değiştirme

kernel = np.ones((5, 5), np.uint8)
image = cv2.imread("resimler/image.jpg")

# --- Dilation ---
# --- Dilation (Genişletme) ---
# Dilation expands bright (white) regions and connects objects.
# Dilation, parlak (beyaz) bölgeleri genişletir ve kopuk nesneleri birleştirir.
# (Usage: Making text thicker, connecting broken objects)
# (Kullanım Alanı: Metin kalınlaştırma, kopuk nesneleri birleştirme)
dilation = cv2.dilate(image, kernel, iterations=1)
cv2.imshow("Dilation", dilation)

# --- Erosion ---
# --- Erosion (Aşındırma) ---
# Erosion shrinks bright regions, removing small noises.
# Erosion, beyaz bölgeleri küçültür ve küçük gürültüleri temizler.
# (Usage: Removing small noises, refining objects)
# (Kullanım Alanı: Gürültü temizleme, nesne inceltme)
erosion = cv2.erode(image, kernel, iterations=1)
cv2.imshow("Erosion", erosion)

# --- Opening ---
# --- Opening (Önce aşındırma sonra genişletme) ---
# Opening = Erosion followed by Dilation.
# Opening = Erozyon ardından Dilation yapılır.
# (Usage: Remove small white noise)
# (Kullanım Alanı: Küçük beyaz gürültüleri temizleme)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening", opening)

# --- Closing ---
# --- Closing (Önce genişletme sonra aşındırma) ---
# Closing = Dilation followed by Erosion.
# Closing = Dilation ardından Erosion yapılır.
# (Usage: Close small holes inside objects)
# (Kullanım Alanı: Nesnelerin içindeki küçük delikleri kapatma)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing", closing)

# --- Morphological Gradient ---
# --- Morfolojik Gradyan ---
# Gradient = Difference between Dilation and Erosion.
# Gradyan = Dilation ve Erosion arasındaki farktır.
# (Usage: Edge detection)
# (Kullanım Alanı: Kenar bulma)
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Gradient", gradient)

# --- Top Hat ---
# --- Top Hat (Üst Şapka İşlemi) ---
# Top Hat = Original Image - Opening
# Top Hat = Orijinal Görüntü - Opening işlemi
# (Usage: Extract small bright objects)
# (Kullanım Alanı: Küçük parlak nesneleri çıkartma)
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Top Hat", tophat)

# --- Black Hat ---
# --- Black Hat (Alt Şapka İşlemi) ---
# Black Hat = Closing - Original Image
# Black Hat = Closing işlemi - Orijinal Görüntü
# (Usage: Extract small dark objects)
# (Kullanım Alanı: Küçük karanlık nesneleri çıkartma)
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("Black Hat", blackhat)

# --- Wait and Close ---
# --- Bekle ve Pencereleri Kapat ---
cv2.waitKey(0)
cv2.destroyAllWindows()
