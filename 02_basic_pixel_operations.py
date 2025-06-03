import cv2
import numpy as np
image1 = cv2.imread("resimler/resim1.jpg")

# --- Image Properties Inspection ---
# --- Resim Özelliklerini İnceleme ---

print("Image1 total pixels (size):", image1.size)      # Resmin piksel sayısı
print("Image1 data type:", image1.dtype)                # Resmin veri tipi
print("Image1 shape (height, width, channels):", image1.shape)  # Yükseklik, genişlik, kanal bilgisi

height, width, channels = image1.shape
print(f"Height: {height}, Width: {width}, Channels: {channels}")

# --- Pixel Value Reading ---
# --- Piksel Değerini Okuma ---
print("Pixel value at (230, 80):", image1[230, 80])  # (B, G, R) değerleri


#  Piksel Tek Tek Okuma ve RGB Ayrıştırma
b, g, r = image1[230, 80]
print(f"Blue: {b}, Green: {g}, Red: {r}")


# --- Pixel Value Modification ---
# --- Piksel Değeri Değiştirme ---
image1[130, 81] = [255, 255, 255]  # Set pixel to white / Pikseli beyaz yap

# --- Drawing a White Line using For Loop ---
# --- For Döngüsüyle Beyaz Çizgi Çizimi ---
for i in range(200):
    image1[130, i] = [255, 255, 255]

# For döngüsü yerine hızlı numpy slice ile çizgi de atabiliriz:
image1[130, 0:200] = [255, 255, 255]  # Hızlı satır çizimi

# Sadece 1 piksel değil, bir alanı (bölgeyi) değiştirme örneği de koyabiliriz:
image1[100:150, 50:150] = [0, 255, 0]  # Yeşil bir dikdörtgen alan


# --- Displaying the Image ---
# --- Resmi Gösterme ---
cv2.imshow("Image-1", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()