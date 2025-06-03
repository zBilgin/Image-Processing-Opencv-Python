import cv2
import numpy as np

# --- Load Images ---
# --- Resimleri Yükleme ---
image1 = cv2.imread("resimler/resim1.jpg")
image2 = cv2.imread("resimler/resim2.jpg")

# --- IMAGE RESIZING ---
# --- RESİM YENİDEN BOYUTLANDIRMA (Resize) ---

# Resize the image manually to specific dimensions
# Belirli boyutlara yeniden boyutlandırma
resized_image2 = cv2.resize(image2, (200, 600))
print("Original Image2 size:", image2.shape)
print("Resized Image2 size:", resized_image2.shape)

# --- IMAGE PYRAMIDS (Scaling by 2x) ---
# --- GÖRÜNTÜ PİRAMİTLERİ (İki Kat Büyütme/Küçültme) ---

# Automatically enlarge the image to double size (pyrUp)
# Görüntüyü otomatik 2 kat büyütme
double_size = cv2.pyrUp(image1)

# Multiply pixel values by 2 after enlarging (scaling pixel intensity too)
# Büyütmeden sonra piksel değerlerini de 2 ile çarparak (renkler değişir)
double_size_scaled = (cv2.pyrUp(image1)) * 2

# Automatically shrink the image to half size (pyrDown)
# Görüntüyü otomatik 2 kat küçültme
half_size = cv2.pyrDown(image1)

# --- ALTERNATIVE RESIZING (Manual Resize to Double) ---
# --- ALTERNATİF BOYUTLANDIRMA (Elle 2x Boyut Ayarlama) ---

# Manual resize by doubling width and height
# Yükseklik ve genişliği 2 ile çarparak elle boyutlandırma
height, width = image1.shape[:2]
double_width = 2 * width
double_height = 2 * height
manual_double_size = cv2.resize(image1, (double_width, double_height))

# --- DISPLAY ALL RESULTS ---
# --- TÜM SONUÇLARI GÖSTERME ---
cv2.imshow("Original Image-2", image2)
cv2.imshow("Resized Image-2", resized_image2)

cv2.imshow("Original Image-1", image1)
cv2.imshow("Double Size (pyrUp)", double_size)
cv2.imshow("Double Size with Pixel Scaling", double_size_scaled)
cv2.imshow("Half Size (pyrDown)", half_size)
cv2.imshow("Manual Double Size (resize)", manual_double_size)

cv2.waitKey(0)
cv2.destroyAllWindows()
