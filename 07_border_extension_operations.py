import cv2
import numpy as np

# --- Load Image ---
# --- Resmi Yükleme ---
image1 = cv2.imread("resimler/resim1.jpg")

# --- BORDER OPERATIONS ---
# --- KENAR (BORDER) İŞLEMLERİ ---
# We use the cv2.copyMakeBorder() function
# cv2.copyMakeBorder() fonksiyonunu kullanırız.

# --- Extend Image Borders ---

# Mirror the edges (Reflect effect)
# Kenarları yansıtarak genişletme (ayna efekti)
reflected_image = cv2.copyMakeBorder(image1, 150, 150, 150, 150, cv2.BORDER_REFLECT)

# Replicate edge pixels
# Kenar piksellerini çoğaltarak genişletme
replicated_image = cv2.copyMakeBorder(image1, 75, 75, 150, 150, cv2.BORDER_REPLICATE)

# Wrap around the image
# Resmi sararak (döngüsel) genişletme
wrapped_image = cv2.copyMakeBorder(image1, 75, 75, 150, 150, cv2.BORDER_WRAP)

# Add a constant border with default color (black)
# Sabit renkli (varsayılan siyah) çerçeve eklemek
constant_border = cv2.copyMakeBorder(image1, 75, 75, 150, 150, cv2.BORDER_CONSTANT)

# Add a constant border with custom color
# Özel renkli sabit çerçeve eklemek
constant_border_colored = cv2.copyMakeBorder(image1, 75, 75, 150, 150, cv2.BORDER_CONSTANT, value=(75, 150, 150))

# --- Display Results ---
# --- Sonuçları Gösterme ---
cv2.imshow("Original Image-1", image1)
cv2.imshow("Reflected Border", reflected_image)
cv2.imshow("Replicated Border", replicated_image)
cv2.imshow("Wrapped Border", wrapped_image)
cv2.imshow("Constant Border (Black)", constant_border)
cv2.imshow("Constant Border (Colored)", constant_border_colored)

cv2.waitKey(0)
cv2.destroyAllWindows()
