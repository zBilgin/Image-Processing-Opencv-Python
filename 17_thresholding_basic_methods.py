import cv2
import numpy as np

# --- Thresholding Techniques ---
# --- Eşik Ayarlama Teknikleri ---

# What is Thresholding?
# Thresholding is a technique to separate regions based on pixel intensity.
# Eşik Ayarlama, piksel yoğunluğuna göre bölgeleri ayıran bir tekniktir.
# It highlights areas of interest by setting pixel values based on a threshold.
# Bir eşik değere göre pikselleri sıfır veya maksimum değer yaparak ilgi alanlarını ön plana çıkarır.

# --- Load Grayscale Image ---
# --- Gri Tonlamalı Resim Yükleme ---

# For thresholding, image must be grayscale.
# Eşik ayarlama işlemi için görüntü gri tonlamalı (tek kanal) olmalıdır.
image = cv2.imread("resimler/resim1.jpg", 0)

# --- Simple Thresholding ---
# --- Basit Eşikleme ---

# Syntax: ret, thresh = cv2.threshold(src, threshold_value, max_value, threshold_type)
# Kullanımı: ret, thresh = cv2.threshold(kaynak, eşik_değeri, max_değer, eşik_tipi)

ret, thresh_binary = cv2.threshold(image, 128, 164, cv2.THRESH_BINARY)
# (Usage: Pixels >128 are set to 164, others set to 0)
# (Kullanım: 128 üstü pikseller 164 yapılır, diğerleri 0 olur.)

# Other common threshold types:
# Diğer threshold tipleri:
# - cv2.THRESH_BINARY
# - cv2.THRESH_BINARY_INV
# - cv2.THRESH_TRUNC
# - cv2.THRESH_TOZERO
# - cv2.THRESH_TOZERO_INV

# --- Adaptive Thresholding ---
# --- Uyarlamalı Eşikleme ---

# What is Adaptive Thresholding?
# Adaptive Thresholding adjusts the threshold value dynamically based on local regions.
# Adaptive Thresholding, görüntünün farklı bölgelerinde farklı eşik değerleri kullanarak adaptif şekilde eşik belirler.
# (Usage: Useful in varying lighting conditions)
# (Kullanım: Işık değişimi olan görüntülerde etkilidir.)

# Syntax: thresh = cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)

# Mean Method
# Ortalama (mean) yöntemi kullanılarak adaptif eşikleme
adaptive_thresh_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                             cv2.THRESH_BINARY, 11, 2)

# Gaussian Method
# Gauss ağırlıklı yöntem kullanılarak adaptif eşikleme
adaptive_thresh_gaussian = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                 cv2.THRESH_BINARY, 11, 2)

# --- Otsu's Thresholding ---
# --- Otsu Yöntemi ile Eşikleme ---

# What is Otsu's Method?
# Otsu automatically calculates the best threshold value without manually choosing one.
# Otsu yöntemi, en uygun eşik değerini otomatik olarak bulur, kullanıcıdan değer girilmesine gerek yoktur.

# Syntax: ret, thresh = cv2.threshold(src, threshold_value, max_value, threshold_type + OTSU)
# Not: threshold_value 0 verilmeli!

ret, otsu_thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# (Usage: Best for bimodal histograms - images with two clear intensity peaks)
# (Kullanım: İki ayrı yoğunluk tepesine sahip (bimodal) görüntülerde mükemmel çalışır.)

# --- Display Results ---
# --- Sonuçları Gösterme ---

cv2.imshow("Original Image", image)
cv2.imshow("Simple Threshold", thresh_binary)
cv2.imshow("Adaptive Threshold - Mean", adaptive_thresh_mean)
cv2.imshow("Adaptive Threshold - Gaussian", adaptive_thresh_gaussian)
cv2.imshow("Otsu Threshold", otsu_thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
