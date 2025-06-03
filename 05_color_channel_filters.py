import cv2
import numpy as np

# --- Load Images ---
# --- Resimleri Yükleme ---
image1 = cv2.imread("resimler/resim1.jpg")
image3 = cv2.imread("resimler/resim3.jpg")
image4 = cv2.imread("resimler/resim4.jpg")
image5 = cv2.imread("resimler/resim5.jpg")

# --- 5. COLOR FILTER APPLICATIONS ---
# --- 5. RENK FİLTRESİ UYGULAMALARI ---

# Set the blue channel of the entire image to 255
# Tüm resmin mavi (blue) kanalını tamamen 255 yapmak
image5[:, :, 0] = 255  # Blue channel

# Apply a mixed color filter
# Karışık renk filtresi uygulamak
image3[:, :, 1] = 150  # Set green channel to 150 / Yeşil kanalı 150 yap
image3[:, :, 2] = 50   # Set red channel to 50 / Kırmızı kanalı 50 yap

# Apply only red filter to a specific region
# Belirli bir bölgeye sadece kırmızı filtre uygulamak
image4[100:125, 75:150, 2] = 255

# --- Display Filtered Images ---
# --- Filtre Uygulanmış Resimleri Gösterme ---
cv2.imshow("Image-3", image3)
cv2.imshow("Image-4", image4)
cv2.imshow("Image-5", image5)

# --- Wait for Keypress and Close Windows ---
# --- Tuş Basımı Bekle ve Pencereleri Kapat ---
cv2.waitKey(0)
cv2.destroyAllWindows()
