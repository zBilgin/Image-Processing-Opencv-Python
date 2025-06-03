import cv2
import numpy as np

# --- Load Images ---
# --- Resimleri Yükleme ---
image5 = cv2.imread("resimler/resim5.jpg")
image6 = cv2.imread("resimler/resim6.jpg")

# --- IMAGE ARITHMETIC OPERATIONS ---
# --- RESİMLERİN ÜST ÜSTE EKLENMESİ ---

# Simple addition
# Düz toplama
sum_image = cv2.add(image5, image6)
cv2.imshow("Sum Image", sum_image)

# Weighted addition
# Ağırlıklı toplama
weighted_sum = cv2.addWeighted(image5, 0.7, image6, 0.3, 0)
cv2.imshow("Weighted Sum Image", weighted_sum)

# --- BITWISE OPERATIONS ---
# --- BİT DÜZEYİNDE (BITWISE) İŞLEMLER ---

# Bitwise AND
# Bitwise AND işlemi
bitwise_and = cv2.bitwise_and(image5, image6)
cv2.imshow("Bitwise AND (Intersection)", bitwise_and)

# Bitwise XOR
# Bitwise XOR işlemi
bitwise_xor = cv2.bitwise_xor(image5, image6)
cv2.imshow("Bitwise XOR (Differences)", bitwise_xor)

# --- MASKING - REGION SELECTION ---
# --- MASKELEME - BÖLGE SEÇİMİ ---

# What is masking?
# Masking (Maskeleme) nedir?
# - Masking allows selecting only certain areas of an image.
# - Maskeleme, bir görüntünün sadece belirli alanlarını seçmemizi sağlar.
# - White areas (255) are visible; black areas (0) are hidden.
# - Beyaz alanlar (255) görünür; siyah alanlar (0) gizlenir.

# Intersection using bitwise_and
# İki görüntünün kesişim bölgelerini gösterir (bitwise_and)

# Differences using bitwise_xor
# İki görüntünün sadece farklı olan bölgelerini gösterir (bitwise_xor)

# Masking, segmentation and object extraction techniques are built on these basic operations.
# Maskeleme, nesne ayırma (segmentation) ve nesne çıkarma işlemleri bu temel operasyonlar üzerine kurulur.

# --- Simple Mask Example ---
# --- Basit Maske Örneği ---

# Create a black mask and draw a white rectangle
# Siyah bir maske oluştur ve üzerine beyaz bir dikdörtgen çiz
mask = np.zeros(image5.shape[:2], dtype="uint8")
cv2.rectangle(mask, (50, 50), (250, 250), 255, -1)

# Apply mask to image5
# Maskeyi image5 üzerine uygula
masked_image = cv2.bitwise_and(image5, image5, mask=mask)

# --- Display Mask Results ---
# --- Maskeleme Sonuçlarını Gösterme ---
cv2.imshow("Original Image-5", image5)
cv2.imshow("Original Image-6", image6)
cv2.imshow("Masked Image-5", masked_image)
cv2.imshow("Mask", mask)

# --- Wait for Keypress and Close All Windows ---
# --- Tuş Basımı Bekle ve Tüm Pencereleri Kapat ---
cv2.waitKey(0)
cv2.destroyAllWindows()
