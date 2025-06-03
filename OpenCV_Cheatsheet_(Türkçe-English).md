# OpenCV Cheatsheet (Türkçe - English)

| Fonksiyon / Function Name       | Kullanım / Usage                                    | Açıklama / Description                                          |
|--------------------------------|----------------------------------------------------|----------------------------------------------------------------|
| `cv2.imread()`                 | `cv2.imread(filename, flags)`                       | Görüntüyü okur. / Reads an image.                             |
| `cv2.imwrite()`                | `cv2.imwrite(filename, img)`                        | Görüntüyü dosyaya yazar. / Writes image to a file.             |
| `cv2.imshow()`                 | `cv2.imshow(winname, img)`                          | Pencerede görüntü gösterir. / Displays image in a window.      |
| `cv2.waitKey()`                | `cv2.waitKey(delay)`                                | Tuş bekler. / Waits for a key event for delay milliseconds.    |
| `cv2.destroyAllWindows()`      | `cv2.destroyAllWindows()`                           | Tüm pencereleri kapatır. / Closes all OpenCV windows.          |
| `cv2.cvtColor()`               | `cv2.cvtColor(img, code)`                           | Renk uzayı dönüşümü yapar. / Converts color space.             |
| `cv2.resize()`                 | `cv2.resize(img, dsize)`                            | Görüntüyü yeniden boyutlandırır. / Resizes the image.          |
| `cv2.threshold()`              | `cv2.threshold(src, thresh, maxval, type)`         | Eşikleme uygular. / Applies a fixed-level threshold.           |
| `cv2.GaussianBlur()`           | `cv2.GaussianBlur(img, ksize, sigmaX)`             | Gauss bulanıklaştırma filtresi. / Gaussian blur filter.         |
| `cv2.medianBlur()`             | `cv2.medianBlur(img, ksize)`                        | Ortanca filtre uygular. / Applies median blur filter.          |
| `cv2.blur()`                  | `cv2.blur(img, ksize)`                              | Ortalama filtre uygular. / Applies averaging filter.           |
| `cv2.Canny()`                 | `cv2.Canny(img, threshold1, threshold2)`           | Kenar algılama yapar. / Detects edges using Canny algorithm.   |
| `cv2.add()`                   | `cv2.add(img1, img2)`                               | İki görüntüyü toplar. / Adds two images element-wise.          |
| `cv2.subtract()`              | `cv2.subtract(img1, img2)`                          | İki görüntü çıkarır. / Subtracts one image from another.       |
| `cv2.bitwise_and()`           | `cv2.bitwise_and(img1, img2)`                       | Mantıksal VE işlemi yapar. / Bitwise AND operation.            |
| `cv2.bitwise_or()`            | `cv2.bitwise_or(img1, img2)`                        | Mantıksal VEYA işlemi yapar. / Bitwise OR operation.           |
| `cv2.bitwise_not()`           | `cv2.bitwise_not(img)`                              | Mantıksal TERSLEME yapar. / Bitwise NOT operation.             |
| `cv2.rectangle()`             | `cv2.rectangle(img, pt1, pt2, color, thickness)`   | Dikdörtgen çizer. / Draws a rectangle on image.                |
| `cv2.circle()`                | `cv2.circle(img, center, radius, color, thickness)`| Daire çizer. / Draws a circle on image.                        |
| `cv2.line()`                  | `cv2.line(img, pt1, pt2, color, thickness)`        | Çizgi çizer. / Draws a line on image.                          |
| `cv2.putText()`               | `cv2.putText(img, text, org, font, scale, color, thickness)` | Görüntüye metin yazar. / Writes text on the image.     |
| `cv2.getRotationMatrix2D()`  | `cv2.getRotationMatrix2D(center, angle, scale)`    | Dönme matrisi oluşturur. / Creates rotation matrix.            |
| `cv2.warpAffine()`            | `cv2.warpAffine(img, M, dsize)`                     | Afine dönüşüm uygular. / Applies affine transformation.        |
| `cv2.erode()`                 | `cv2.erode(img, kernel)`                            | Erozyon işlemi yapar. / Applies erosion morphological operation.|
| `cv2.dilate()`                | `cv2.dilate(img, kernel)`                           | Genleşme işlemi yapar. / Applies dilation morphological operation.|
| `cv2.morphologyEx()`          | `cv2.morphologyEx(img, op, kernel)`                 | Gelişmiş morfolojik işlemler. / Advanced morphological ops.    |
| `cv2.pyrUp()`                 | `cv2.pyrUp(img)`                                    | Görüntüyü büyütür. / Upscales the image.                       |
| `cv2.pyrDown()`               | `cv2.pyrDown(img)`                                  | Görüntüyü küçültür. / Downscales the image.                    |
| `cv2.VideoCapture()`          | `cv2.VideoCapture(0)`                               | Kamera ya da video açar. / Opens camera or video file.         |
| `cv2.VideoWriter()`           | `cv2.VideoWriter(filename, fourcc, fps, size)`     | Video kaydı oluşturur. / Creates video writer to save video.   |

---

## Örnek Kullanım / Example Usage

```python
import cv2
import numpy as np

# Görüntü oku / Read image
img = cv2.imread('image.jpg', cv2.IMREAD_COLOR)

# Görüntüyü gri yap / Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gaussian bulanıklaştırma / Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Kenar algılama / Edge detection
edges = cv2.Canny(blur, 50, 150)

# Görüntüyü göster / Show image
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
