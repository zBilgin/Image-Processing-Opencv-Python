import cv2
import numpy as np

# --- Image Rotation ---
# --- Görüntü Döndürme ---

# Load Image
# Resmi Yükleme
image = cv2.imread("resimler/image.jpg")

# --- Rotate using cv2.getRotationMatrix2D ---
# --- cv2.getRotationMatrix2D ile Döndürme ---

# Create rotation matrix
# Rotasyon matrisi oluştur (center=merkez, angle=açı, scale=ölçek)
# (Usage: Rotate images by any angle, keeping scale)
# (Kullanım Alanı: Görüntüyü istediğin açıda döndürmek, ölçek koruma)

(h, w) = image.shape[:2]
center = (w // 2, h // 2)  # Image center (Görüntü merkezi)

rotation_matrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=1.0)

# Apply the rotation
# Döndürmeyi uygula
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

cv2.imshow("Rotated Image (45 degrees)", rotated_image)

# --- Rotate 90, 180, 270 degrees quickly ---
# --- Hızlı 90, 180, 270 derece döndürme ---

# Rotate 90 degrees clockwise
# 90 derece saat yönünde döndürme
rotated_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotated 90 Clockwise", rotated_90)

# Rotate 180 degrees
# 180 derece döndürme
rotated_180 = cv2.rotate(image, cv2.ROTATE_180)
cv2.imshow("Rotated 180 Degrees", rotated_180)

# Rotate 90 degrees counterclockwise
# 90 derece saat yönünün tersine döndürme
rotated_90_counter = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Rotated 90 CounterClockwise", rotated_90_counter)

# --- Usage Notes ---
# --- Kullanım Notları ---

# getRotationMatrix2D: Any custom angle rotation
# (Kullanım Alanı: İstediğin açıda döndürme, esnek kontrol)
# rotate (predefined): Fast 90-180-270 degree rotations
# (Kullanım Alanı: Hızlı sabit açılı döndürmeler)

# --- Wait and Close ---
# --- Bekle ve Pencereleri Kapat ---
cv2.waitKey(0)
cv2.destroyAllWindows()
