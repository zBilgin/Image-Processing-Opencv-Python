# OpenCV Görüntü İşleme CheatSheet

---

## 1️⃣ Resim Yükleme ve Gösterme
```python
# Load an image
image = cv2.imread("path/to/image.jpg")

# Display the image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 2️⃣ Temel Görüntü İşlemleri
```python
# Get image properties
height, width, channels = image.shape

# Access pixel values
pixel = image[100, 200]

# Modify pixel values
image[100, 200] = [255, 0, 0]
```

---

## 3️⃣ Boyutlandırma (Resize)
```python
# Resize image to fixed size
resized = cv2.resize(image, (300, 300))

# Double size using pyramids
bigger = cv2.pyrUp(image)

# Half size using pyramids
smaller = cv2.pyrDown(image)
```

---

## 4️⃣ Renk Kanalları ve Filtreler
```python
# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Mean Blur
mean_blur = cv2.blur(image, (5,5))

# Apply Median Blur
median_blur = cv2.medianBlur(image, 5)
```

---

## 5️⃣ Kenar (Border) İşlemleri
```python
# Add border to image
border = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(0, 0, 0))
```

---

## 6️⃣ Şekil ve Yazı Çizimi
```python
# Draw rectangle
cv2.rectangle(image, (50, 50), (150, 150), (0, 255, 0), 2)

# Draw circle
cv2.circle(image, (100, 100), 50, (255, 0, 0), 3)

# Write text
cv2.putText(image, "OpenCV", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
```

---

## 7️⃣ Resim Aritmetiği
```python
# Add two images
added = cv2.add(image1, image2)

# Weighted addition
weighted = cv2.addWeighted(image1, 0.7, image2, 0.3, 0)
```

---

## 8️⃣ Morphological Operations (Morfolojik İşlemler)
```python
kernel = np.ones((5,5), np.uint8)

# Dilation
dilated = cv2.dilate(image, kernel, iterations=1)

# Erosion
eroded = cv2.erode(image, kernel, iterations=1)

# Opening
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Closing
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
```

---

## 9️⃣ Thresholding (Eşikleme)
```python
# Simple Thresholding
ret, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# Adaptive Thresholding (Mean)
adaptive_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                       cv2.THRESH_BINARY, 11, 2)

# Adaptive Thresholding (Gaussian)
adaptive_gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY, 11, 2)

# Otsu Thresholding
ret, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
```

---

## 🔠 Canny Edge Detection (Kenar Algılama)
```python
# Apply Canny Edge Detection
edges = cv2.Canny(blurred, 50, 150)

# Auto Canny
def auto_canny(image, sigma=0.33):
    median = np.median(image)
    lower = int(max(0, (1.0 - sigma) * median))
    upper = int(min(255, (1.0 + sigma) * median))
    return cv2.Canny(image, lower, upper)

edges_auto = auto_canny(blurred)
```

---

## 1️⃣ Kameradan Görüntü Alma
```python
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    cv2.imshow("Camera Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
```

---

## 1️⃣ Video Kaydetme
```python
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, 20.0, (width, height))

while True:
    ret, frame = camera.read()
    out.write(frame)
    cv2.imshow("Recording", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
out.release()
cv2.destroyAllWindows()
```

---


---



