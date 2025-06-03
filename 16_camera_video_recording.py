import cv2

# --- Video Capture and Save ---
# --- Kamera Görüntüsü Al ve Video Kaydet ---

# Reminder: For large data like video/audio, we use encoding (compression) when sending, and decoding (decompression) when receiving.
# Hatırlatma: Video, ses gibi büyük veriler gönderilirken encode (sıkıştırma), alınırken decode (çözme) işlemi yapılır.

# Start camera capture
# Kamera görüntüsü başlatma
camera = cv2.VideoCapture(0)

# --- Get Frame Dimensions ---
# --- Kare Boyutlarını Alma ---
width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Frame dimensions: Width={width}, Height={height}")
# (Usage: Needed to define video writer size)
# (Kullanım Alanı: Video kaydında boyut belirlemek için gereklidir.)

# --- FOURCC Encoding ---
# --- FOURCC Kodlayıcı Kullanımı ---

# FOURCC (Four Character Code) is a 4-byte code identifying video codecs.
# FOURCC (Dört Karakter Kodu), video codec'lerini tanımlayan 4 baytlık bir koddur.
# Example codecs: 'XVID', 'MJPG', 'mp4v'
# Örnek codec'ler: 'XVID', 'MJPG', 'mp4v'

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
# Note: The asterisk (*) unpacks the string into separate characters
# Not: Yıldız (*) karakterleri tek tek açarak fonksiyona gönderir.

# --- Initialize Video Writer ---
# --- Video Writer'ı Başlatma ---

# cv2.VideoWriter(filename, codec, fps, frame_size)
# cv2.VideoWriter(dosya_adı, codec, fps, kare_boyutu)
writer = cv2.VideoWriter("kayit.mp4v", fourcc, 20, (width, height))
# (Usage: Save frames into a video file)
# (Kullanım Alanı: Kameradan alınan kareleri video dosyasına kaydetmek.)

# --- Real-time Capture and Save Loop ---
# --- Gerçek Zamanlı Kaydetme Döngüsü ---

while True:
    ret, frame = camera.read()
    # Read a frame from the camera
    # Kameradan bir kare oku

    if not ret:
        break  # If reading fails, exit
        # Okuma başarısızsa döngüden çık

    writer.write(frame)
    # Write frame into video file
    # Kareyi video dosyasına yaz

    cv2.imshow("Recording...", frame)
    # Display the frame while recording
    # Kayıt sırasında kareyi göster

    # Press 'q' to stop recording
    # 'q' tuşuna basarak kaydı durdur
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# --- Release Resources ---
# --- Kaynakları Serbest Bırakma ---

camera.release()
writer.release()
cv2.destroyAllWindows()
