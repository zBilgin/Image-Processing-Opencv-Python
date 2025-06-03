import cv2
import numpy as np

# --- Load Images ---
# --- Resimleri Yükleme ---
image1 = cv2.imread("resimler/resim1.jpg")
image3 = cv2.imread("resimler/resim3.jpg")

# --- DRAWING SHAPES ON IMAGE ---
# --- RESİM ÜZERİNE ŞEKİL ÇİZME ---

# Draw a Rectangle
# Dikdörtgen çizimi
# Syntax: cv2.rectangle(image, start_point, end_point, color(BGR), thickness)
cv2.rectangle(image3, (50, 100), (150, 30), [0, 0, 255], 3)

# To find pixel coordinates easily, you can use: 
# Koordinatları kolayca bulmak için kullanılabilir:
# import pyautogui as gui → gui.position()

# Draw a Line
# Çizgi çizimi
# Syntax: cv2.line(image, start_point, end_point, color(BGR), thickness)
cv2.line(image1, (0, 0), (100, 100), (150, 125, 89), 3)

# Draw a Circle
# Daire çizimi
# Syntax: cv2.circle(image, center_point, radius, color(BGR), thickness)
cv2.circle(image3, (100, 260), 25, (0, 255, 0), 3)

# Put Text on Image
# Resme Yazı Ekleme
# Syntax: cv2.putText(image, "text", start_point, font, font_scale, color(BGR), thickness)
cv2.putText(image1, "ZEKI", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 5)

# Note: cv2.FONT_HERSHEY_COMPLEX is one of the available fonts in OpenCV.
# Not: cv2.FONT_HERSHEY_COMPLEX OpenCV'de bulunan yazı tipi çeşitlerinden biridir.

# --- Display Results ---
# --- Sonuçları Gösterme ---
cv2.imshow("Image-1 with Drawings", image1)
cv2.imshow("Image-3 with Drawings", image3)

cv2.waitKey(0)
cv2.destroyAllWindows()
