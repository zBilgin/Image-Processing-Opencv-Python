import cv2
import numpy as np

# --- Camera Initialization ---
# --- Kamera Başlatma ---

# cv2.VideoCapture(x): Start capturing from camera or video source
# cv2.VideoCapture(x): Kameradan veya video kaynağından görüntü alır
# 0 = Built-in (laptop) camera
# 1 = External USB camera
# 2 = Video file

camera = cv2.VideoCapture(0)  # Use 0 for internal camera

# --- Real-time Video Processing Loop ---
# --- Gerçek Zamanlı Video İşleme Döngüsü ---

while True:
    ret, frame = camera.read()
    # Read frame from the camera
    # Kameradan bir kare (frame) oku

    if not ret:
        break  # If reading fails, exit loop
        # Okuma başarısızsa döngüyü kır

    # --- Apply Simple Effects on Frame ---
    # --- Kare Üzerine Basit Efektler Uygulama ---

    frame[:, :, 0] = 160
    # Set blue channel to 160 (slight bluish effect)
    # Mavi kanalı 160'a ayarlayarak hafif mavi efekti verir

    cv2.rectangle(frame, (225, 225), (400, 400), (0, 0, 255), 2)
    # Draw a red rectangle on the frame
    # Kare üzerine kırmızı bir dörtgen çizer

    # --- Display the Frame ---
    # --- Kareyi Ekranda Gösterme ---
    cv2.imshow("Camera Frame", frame)

    # --- Break the Loop with 'q' Key ---
    # --- 'q' Tuşu ile Döngüyü Bitirme ---
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

# --- Release the Camera and Close Windows ---
# --- Kamerayı Serbest Bırak ve Pencereleri Kapat ---
camera.release()
cv2.destroyAllWindows()
