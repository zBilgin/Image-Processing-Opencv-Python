# 🧠 Görüntü İşleme Projeleri - Python & OpenCV  
# 🧠 Image Processing Projects - Python & OpenCV

📌 Bu proje hem Türkçe hem İngilizce açıklamalar içermektedir.  
📌 This project includes both Turkish and English explanations.

---

## 🎯 Amaç / Purpose

This repository organizes various image processing projects developed using Python and OpenCV by topic. Each file includes sample code with both Turkish and English explanations.

Bu depo, Python ve OpenCV kullanılarak geliştirilen çeşitli görüntü işleme uygulamalarını konu başlıklarına göre sıralar. Her bir dosya, örnek kodlarla birlikte hem Türkçe hem İngilizce açıklamalar içerir.  


---

## 🗂️ Konular / Topics

| Kategori / Category                  | Dosya / File                                     | Açıklama / Description |
|--------------------------------------|--------------------------------------------------|--------------------------|
| 📌 Giriş / Intro                      | [`01_template_intro.py`](01_template_intro.py)                           | Şablon dosya yapısı <br> Template project structure |
| 🟩 Piksel İşlemleri / Pixel Ops      | [`02_basic_pixel_operations.py`](02_basic_pixel_operations.py)                   | Piksel erişimi, kanal ayırma <br> Pixel access, channel ops |
| ✂️ Kırpma / Cropping                 | [`03_cropping_extract_patch.py`](03_cropping_extract_patch.py)                   | ROI seçimi, yama çıkarma <br> ROI selection and patch extraction |
| ⚫ Gri Tonlama / Grayscale            | [`04_grayscale_channel_operations.py`](04_grayscale_channel_operations.py)             | Gri ton dönüşümü <br> Grayscale conversion |
| 🎨 Renk Kanalları / Color Filters    | [`05_color_channel_filters.py`](05_color_channel_filters.py)                    | Kanal bazlı filtreleme <br> Channel-wise filtering |
| 🌫️ Bulanıklaştırma / Blurring       | [`06_blurring_filters_mean_median_gaussian.py`](06_blurring_filters_mean_median_gaussian.py)    | Gürültü azaltma filtreleri <br> Denoising filters |
| ⛔ Kenar Uzatma / Border Extension   | [`07_border_extension_operations.py`](07_border_extension_operations.py)              | Kenar oluşturma yöntemleri <br> Border types and padding |
| 🖍️ Çizim / Drawing                   | [`08_shape_and_text_drawing.py`](08_shape_and_text_drawing.py)                   | Şekil ve metin çizme <br> Drawing shapes and text |
| ➕ Görüntü Aritmetiği / Arithmetic    | [`09_image_arithmetic_operations.py`](09_image_arithmetic_operations.py)              | Görüntü toplama, çıkarma vs. <br> Addition, subtraction etc. |
| 🔍 Yeniden Boyutlandırma / Resize    | [`10_image_resizing_scaling.py`](10_image_resizing_scaling.py)                   | Ölçekleme ve yeniden boyutlandırma <br> Scaling and resizing |
| 🧱 Görüntü Piramitleri / Pyramids    | [`11_image_pyramids.py`](11_image_pyramids.py)                           | Gaussian ve Laplacian piramitleri <br> Gaussian & Laplacian pyramids |
| 🔧 Morfoloji / Morphology            | [`12_morphological_operations.py`](12_morphological_operations.py)                 | Erozyon, genişleme, açma-kapama <br> Erosion, dilation, opening-closing |
| 🔄 Döndürme / Rotation               | [`13_image_rotation.py`](13_image_rotation.py)                           | Açılı döndürme <br> Angle-based rotation |
| 🎥 Kamera İşlemleri / Camera Input   | [`15_camera_frame_capture_video_operations.py`](15_camera_frame_capture_video_operations.py)    | Kamera görüntüsü alma <br> Capturing from camera |
| 💾 Kayıt / Recording                 | [`16_camera_video_recording.py`](16_camera_video_recording.py)                   | Kamera ile video kaydı <br> Recording video from camera |
| ⚖️ Eşikleme / Thresholding           | [`17_thresholding_basic_methods.py`](17_thresholding_basic_methods.py)               | Sabit ve uyarlanabilir eşikleme <br> Static and adaptive thresholding |
| 🔪 Kenar Algılama / Edge Detection   | [`18_canny_edge_detection.py`](18_canny_edge_detection.py)                     | Canny algoritması ile kenar bulma <br> Canny edge detection |

> 🔄 Liste zamanla güncellenecektir.  
> 🔄 This list will be updated over time.

---

## 🧾 Ekstra / Extras

- 📘 [OpenCV_Cheatsheet_(Türkçe-English).md](./OpenCV_Cheatsheet_(Türkçe-English).md) → 
>Reference for frequently used OpenCV functions  
>Sık kullanılan OpenCV fonksiyonları için başvuru kılavuzu 

- 📘 [Numpy_Cheatsheet_(Türkçe-English).md](./Numpy_Cheatsheet_(Türkçe-English).md) →
>Reference for frequently used Numpy functions  
>Sık kullanılan Numpy fonksiyonları için başvuru kılavuzu 

---

## 🚀 Kurulum ve Çalıştırma / Setup & Run

1. Gerekli kütüphaneleri yükleyin / Install required packages:

```bash
pip install opencv-python numpy matplotlib
```
---

## 📌 Katkı / Contribution
>This repo is under active development. Contributions and feedback are welcome. <br>
>Bu repo aktif olarak geliştirilmektedir. Geri bildirim ve katkılarınızı beklerim.
   

---
## Hızlı Bakış / Quick Look

## 1️⃣ Resim Yükleme ve Gösterme
```python
# Load an image
image = cv2.imread("path/to/image.jpg")

# Display the image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

> **📌 Continued below**
>
> **📌 Aşağıda devam ediyor**

<details>
<summary>🔽 Daha fazlası için tıklayın / Click for more</summary>



---


# OpenCV Görüntü İşleme CheatSheet
# OpenCV Image Processing CheatSheet
---

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

## 1️⃣0 Canny Edge Detection (Kenar Algılama)
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

## 1️⃣1️⃣ Kameradan Görüntü Alma
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

## 1️⃣2️⃣ Video Kaydetme
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


>Please for more sample look for repos project
>Lütfen daha fazla örnek için projelere bakın



---

</details> 



