import cv2
import numpy as np

# --- Canny Edge Detection ---
# --- Canny Kenar Algılama ---

# Load Image
# Resmi Yükleme
image = cv2.imread("resimler/grott.jpg")  # (Correct path and extension!)
# (Usage: Original color image loaded.)
# (Kullanım: Orijinal renkli görüntüyü yükler.)

# --- Preprocessing for Canny ---
# --- Canny İçin Ön Hazırlık ---

# Convert to Grayscale
# Gri Tonlamaya Çevir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
# Gürültüyü azaltmak için Gauss bulanıklaştırması uygula
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

# (Usage: Blurring removes small edges and noise before edge detection.)
# (Kullanım: Küçük kenarları ve gürültüyü azaltarak daha net kenarlar elde edilir.)

# --- Basic Canny Edge Detection ---
# --- Temel Canny Kenar Algılama ---

# Syntax: edges = cv2.Canny(src, lower_threshold, upper_threshold)
# Kullanımı: edges = cv2.Canny(kaynak, alt_eşik, üst_eşik)

edges_basic = cv2.Canny(blurred, 50, 150)
# (Usage: Detect edges between intensity gradients 50-150.)
# (Kullanım: 50-150 yoğunluk arası gradyanlarda kenarları bulur.)

# --- Automatic Canny Edge Detection ---
# --- Otomatik Canny Kenar Algılama ---

# What is Auto Canny?
# Auto Canny automatically calculates optimal thresholds based on image statistics.
# Auto Canny, görüntünün istatistiksel özelliklerine göre eşik değerlerini otomatik ayarlar.

def auto_canny(image, sigma=0.33):
    # Compute the median of the pixel intensities
    # Piksel yoğunluklarının medyanını hesapla
    median = np.median(image)

    # Set lower and upper thresholds
    # Alt ve üst eşik değerlerini ayarla
    lower = int(max(0, (1.0 - sigma) * median))
    upper = int(min(255, (1.0 + sigma) * median))

    # Apply Canny using the automatically computed thresholds
    # Hesaplanan eşikler ile Canny uygula
    edges = cv2.Canny(image, lower, upper)
    return edges

edges_auto = auto_canny(blurred)

# --- Visualize Results Side by Side ---
# --- Sonuçları Yan Yana Görselleştirme ---

# np.hstack([array1, array2, array3]) horizontally stacks images
# np.hstack([array1, array2, array3]) görüntüleri yatayda birleştirir

combined = np.hstack([edges_basic, edges_auto])

cv2.imshow("Edges: Basic vs Auto Canny", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()
