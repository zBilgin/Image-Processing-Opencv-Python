import cv2
import numpy as np

# --- Load Image ---
# --- Resmi Yükleme ---
image2 = cv2.imread("resimler/resim2.jpg")

# --- Cropping a Region from the Image ---
# --- Resimden Belirli Bir Bölgeyi Kesme ---
crop = image2[20:100, 60:120]  # Select region by slicing / Dilimleme ile bölge seçimi
cv2.imshow("Crop", crop)

# --- Pasting the Cropped Region to Another Location ---
# --- Kesilen Bölgeyi Başka Bir Konuma Yapıştırma ---
image2[40:120, 80:140] = crop
# Note: The size of the cropped area and the target area must be the same, otherwise an error occurs.
# Not: Kesit ve hedef alanın boyutları aynı olmalıdır, aksi halde hata alınır.

# --- Display Modified Image ---
# --- Değiştirilen Resmi Gösterme ---
cv2.imshow("Image-2", image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
