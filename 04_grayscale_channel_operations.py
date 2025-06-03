import cv2
import numpy as np

# --- Load Image ---
# --- Resmi Yükleme ---
image5 = cv2.imread("resimler/resim5.jpg")

# --- Convert to Grayscale (Method 1) ---
# --- Griye Çevirme (Yöntem 1) ---
# Read directly as grayscale
# Doğrudan gri olarak okuma
image7 = cv2.imread("resim7.png", 0)
cv2.imshow("Grayscale Image-7", image7)

# --- Convert to Grayscale (Method 2) ---
# --- Griye Çevirme (Yöntem 2) ---
# Convert after reading color image
# Renkli resmi sonradan griye çevirme
image5_gray = cv2.cvtColor(image5, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image-5", image5_gray)
cv2.imshow("Original Image-5", image5)

# --- Shape Difference Between Color and Grayscale Images ---
# --- Renkli ve Gri Resimler Arasındaki Shape (Boyut) Farkı ---
height, width, channel_count = image5.shape
print(f"Color image -> Height: {height}, Width: {width}, Channels: {channel_count}")

height, width = image5_gray.shape
print(f"Grayscale image -> Height: {height}, Width: {width}")
# In grayscale images, there is no channel dimension.
# Gri resimlerde kanal boyutu yoktur.

# --- Wait for Keypress and Close Windows ---
# --- Tuş Basımı Bekle ve Pencereleri Kapat ---
cv2.waitKey(0)
cv2.destroyAllWindows()
