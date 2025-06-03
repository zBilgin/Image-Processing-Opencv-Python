# OpenCV ile Temel Görüntü İşleme Uygulamaları

# Bu içerik boyunca basit den ileri seviye
# open cv2 ve numpy kütüphaneleri kullanılarak 
#  görüntü işleme uygulamaları ele alınmış 
# kısmi olarak açıklamalar da bulunulmuştur
# bir cheatsheet - kopya kağıdı olarak
# hızlı referans olması amacıyla hazırlanmıştır

# --- EKLEME YAPILACAKLAR ---
Aspect ratio koruyarak boyutlandırma (ekleyebilirsin)
bunu döndürme rotate işlemleri ekle 
Buraya ayrıca thresholding (eşikleme) ekleyebilirsin: cv2.threshold
✅ Burada import pyautogui ile koordinat yakalama da bonus bilgi olarak geçilebilir.
8. İleri Seviye İşlemler (İleride Ekle)
Kenar bulma (cv2.Canny)

Gaussian Blur, Median Blur (cv2.GaussianBlur, cv2.medianBlur)

Erozyon, Genişleme (cv2.erode, cv2.dilate)

Perspektif düzeltme (warp perspective)

Kontur bulma (cv2.findContours)

Histogram hesaplama ve eşitleme (cv2.calcHist)

#  --- CHEATSHEET ---
İşlem | Komut | Açıklama
Resim Okuma | cv2.imread("resim.jpg") | Dosyadan resmi yükler
Resim Gösterme | cv2.imshow("Başlık", resim) | Resmi yeni pencerede gösterir
Resize | cv2.resize(resim, (genişlik, yükseklik)) | Boyut değiştirir
Grayscale Çevirme | cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY) | Renkli resmi gri yapar
Kesit Alma | resim[y1:y2, x1:x2] | Belirli alanı seçer
Piksel Değeri Okuma | resim[x,y] | BGR değerlerini döner
Piksel Değeri Değiştirme | resim[x,y] = [255,255,255] | Pikseli değiştirir
Çerçeve Ekleme | cv2.copyMakeBorder() | Resmi kenarlardan genişletir
Şekil Çizimi | cv2.rectangle(), cv2.circle() | Resmin üstüne şekil çizer
Yazı Ekleme | cv2.putText() | Resme yazı yazar
Aritmetik Toplama | cv2.add(), cv2.addWeighted() | Resimleri birleştirir
Kenar Bulma | cv2.Canny(resim,50,150) | Kenarları algılar
Bulanıklaştırma | cv2.GaussianBlur(resim, (5,5), 0) | Resmi yumuşatır

# 🚀 Mini-Proje Fikirleri

Mini Proje	Açıklama
Basit Filtre Uygulayıcı	Kullanıcıdan seçim al, resmi gri, bulanık veya kenarlı yap
Dinamik Kesit Alıcı	Mouse ile resim üstünde seçip kırpma
Resim Karşılaştırıcı	İki resmi karşılaştır ve farkları işaretle
Gerçek Zamanlı Kamera Uygulaması	Kameradan anlık görüntü alıp filtre uygula
Basit Resim Editörü	Çizim yapma, yazı ekleme, renk değiştirme
Şekil Dedektörü	Daire, kare gibi şekilleri bul ve sınıflandır