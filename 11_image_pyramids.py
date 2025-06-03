import cv2
import numpy as np

# --- NumPy Array Creation for Images ---
# --- NumPy ile Görüntü Matrisleri Oluşturma ---

# np.ones(shape): Create array filled with 1s
# np.ones(shape): Tüm elemanları 1 olan bir dizi oluşturur

# np.zeros(shape): Create array filled with 0s
# np.zeros(shape): Tüm elemanları 0 olan bir dizi oluşturur

# np.full(shape, value): Create array filled with a specific value
# np.full(shape, value): Tüm elemanları belirli bir değerle doldurulmuş bir dizi oluşturur

# --- Create Different Matrices ---
# --- Farklı Matrisler Oluşturma ---

# Black image (all pixels are 0)
# Siyah görüntü (tüm pikseller sıfır)
black_image = np.zeros((300, 300, 3), dtype=np.uint8)

# White image (all pixels are 1, but needs scaling to see white properly)
# Beyaz görüntü (tüm pikseller 1; görünür beyaz için 255 olmalı!)
white_image = np.ones((600, 600, 3), dtype=np.uint8) * 255

# Gray image (all pixels are 150)
# Gri görüntü (tüm pikseller 150 değeri)
gray_image = np.full((200, 200, 3), 150, dtype=np.uint8)

# --- Experimental Matrix ---
# --- Deneme Matrisi ---

# Single-channel image filled with 255 (pure white in grayscale)
# Tek kanallı, 255 ile dolu (grayscale saf beyaz) görüntü
experimental_image = np.full((200, 200, 1), 255, dtype=np.uint8)

# --- Important Note About Color Channels ---
# --- Renk Kanalları Hakkında Önemli Not ---

# ⚡ To create a colored image with different values per channel (B, G, R),
# you should construct a 3-channel image where each channel is controlled separately.
# ⚡ Her renk kanalı (B, G, R) için farklı değerler vererek renkli bir görüntü oluşturmak istiyorsan,
# her kanalı ayrı ayrı kontrol etmelisin.

# Example: Create a colored matrix manually
# Örnek: Manuel renkli matrix oluşturma
colored_image = np.zeros((200, 200, 3), dtype=np.uint8)
colored_image[:, :, 0] = 255  # Blue channel full
colored_image[:, :, 1] = 100  # Green channel medium
colored_image[:, :, 2] = 50   # Red channel low

# --- Display All Created Matrices ---
# --- Oluşturulan Tüm Matrisleri Gösterme ---
cv2.imshow("Black Image (Zeros)", black_image)
cv2.imshow("White Image (Ones scaled to 255)", white_image)
cv2.imshow("Gray Image (150)", gray_image)
cv2.imshow("Experimental Grayscale Image", experimental_image)
cv2.imshow("Colored Image (Custom BGR Values)", colored_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
