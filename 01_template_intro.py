# STANDART BAŞLANGIÇ ŞABLONU
import cv2
import numpy as np
resim1 = cv2.imread("resimler/resim1.jpg")
cv2.imshow("Resim-1", resim1)
cv2.waitKey(0) 
cv2.destroyAllWindows()  
# ---------------------

# Kütüphanelerin eklenmesi
import cv2
import numpy as np

# --- 1. RESİM OKUMA ---
resim1 = cv2.imread("resimler/resim1.jpg")
resim2 = cv2.imread("resim2.jpg")
resim3 = cv2.imread("resim3.jpg")

#--- 2. RESİM GÖSTERME ---
cv2.imshow("Resim-1", resim1)
cv2.imshow("Resim-2", resim2)
cv2.imshow("Resim-3", resim3),

# --- 3. PENCERE VE PROGRAM SONLANDIRMA ---
cv2.waitKey(0)  # Kullanıcının tuş basmasını bekler
cv2.destroyAllWindows()  # Tüm açılan OpenCV pencerelerini kapatır

