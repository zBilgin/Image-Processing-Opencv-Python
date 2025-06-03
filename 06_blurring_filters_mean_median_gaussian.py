import cv2
import numpy as np

# --- Load Image ---
# --- Resmi Yükleme ---
image1 = cv2.imread("resimler/resim1.jpg")

# --- Apply Mean Filter (Averaging Blur) ---
# --- Ortalama Filtresi (Bulanıklaştırma) Uygulama ---
# Mean filter: Calculates the average of the surrounding pixels and assigns it to the center pixel.
# Ortalama filtresi: Komşu piksellerin ortalamasını alır ve merkez piksele yazar.
# Useful for removing noise; it is a linear filter.
# Gürültü temizlemek için kullanılır; doğrusal (linear) filtredir.

mean_filter = cv2.blur(image1, (5, 5))
# Kernel size examples: (3,3), (5,5), (Y,T)

# --- Apply Median Filter ---
# --- Medyan Filtresi Uygulama ---
# Median filter: Sorts neighboring pixels and picks the middle value.
# Medyan filtresi: Komşu pikselleri sıralayıp ortadaki değeri merkez piksele atar.
# It is a non-linear filter.
# Doğrusal olmayan bir filtredir.

median_filter = cv2.medianBlur(image1, 3)
# Usage: cv2.medianBlur(src, ksize)

# --- Apply Gaussian Blur ---
# --- Gauss Filtresi ile Bulanıklaştırma ---
# Gaussian filter: Applies a weighted average based on a bell-shaped curve (Gaussian distribution).
# Gauss filtresi: Çan eğrisi (Gauss dağılımı) kullanarak ağırlıklı ortalama uygular.

gaussian_filter = cv2.GaussianBlur(image1, (3, 3), 0)
# Kernel size and standard deviation (sigma) are important parameters.

# --- Important Notes ---
# --- Önemli Notlar ---
# In mean filter, a single outlier pixel can heavily affect the average value.
# Ortalama filtrede, aşırı değerli bir piksel ortalamayı büyük ölçüde etkileyebilir.

# Median filter handles outliers better, preserving edges while removing noise.
# Medyan filtre, uç değerleri daha iyi bastırır, kenarları korurken gürültüyü azaltır.

# Gaussian filter combines the ideas of weighted averaging and spatial closeness.
# Gauss filtresi, hem ağırlıklı ortalama hem de uzamsal yakınlık kavramlarını birleştirir.

# --- Display Results ---
# --- Sonuçları Gösterme ---
cv2.imshow("Original Image-1", image1)
cv2.imshow("Mean Filter", mean_filter)
cv2.imshow("Median Filter", median_filter)
cv2.imshow("Gaussian Filter", gaussian_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()
