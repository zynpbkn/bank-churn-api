# 🏦 Bank Customer Churn Prediction API

Bu proje, bir bankanın müşterilerinin hizmeti terk edip etmeyeceğini tahmin eden bir **Makine Öğrenimi API servisidir**. Model, FastAPI ile RESTful servis haline getirilmiş ve Docker container içinde çalıştırılabilir durumdadır.

---

## 📦 İçerik

- `train_model.py`: Veriyi işleyip modeli eğitir ve `churn_model.joblib` olarak kaydeder.
- `app.py`: FastAPI uygulaması. JSON veri alır ve tahmin döner.
- `requirements.txt`: Gerekli Python kütüphaneleri.
- `Dockerfile`: Uygulamayı kapsayan Docker imajı.

---

## 🧠 Model Özeti

- **Model Tipi**: RandomForestClassifier
- **Girdi Özellikleri**:
  - `CreditScore`, `Geography`, `Gender`, `Age`, `Tenure`, `Balance`, `NumOfProducts`, `HasCrCard`, `IsActiveMember`, `EstimatedSalary`
- **Çıktı**: 
  - `0` → Müşteri kalır  
  - `1` → Müşteri bankadan ayrılır

---

## ⚙️ Kurulum

### 1. Modeli Eğit

```bash
python train_model.py
Bu işlem churn_model.joblib adlı modeli oluşturur.

2. Docker İmajı Oluştur
bash
Kopyala
Düzenle
docker build -t bank-churn-app .
3. Container’ı Çalıştır
bash
Kopyala
Düzenle
docker run -d -p 8502:8502 --name bank-churn-container bank-churn-app
📮 API Kullanımı
POST /predict
Örnek İstek:
json
Kopyala
Düzenle
{
  "CreditScore": 619,
  "Geography": "France",
  "Gender": "Female",
  "Age": 42,
  "Tenure": 2,
  "Balance": 0.0,
  "NumOfProducts": 1,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 101348.88
}
Curl ile Gönder:
bash
Kopyala
Düzenle
curl -X POST "http://localhost:8502/predict" -H "Content-Type: application/json" -d '{
  "CreditScore": 619,
  "Geography": "France",
  "Gender": "Female",
  "Age": 42,
  "Tenure": 2,
  "Balance": 0,
  "NumOfProducts": 1,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 101348.88
}'
Yanıt:
json
Kopyala
Düzenle
{
  "Exited": 1
}
🛡️ Güvenlik Notu
Bu proje geliştirici/test ortamı için hazırlanmıştır.
Herhangi bir API anahtarı, kullanıcı adı, parola veya hassas bilgi bu projede yer almamaktadır.

Tavsiye: Gerçek ortamda .env dosyası kullanarak gizli bilgiler ayrı tutulmalıdır.

🧪 Test
API arayüzüne tarayıcıdan eriş:

http
Kopyala
Düzenle
http://localhost:8502/docs
Swagger arayüzü ile test işlemleri kolaylıkla yapılabilir.

✍️ Geliştiren
Bu proje, eğitim ve demo amaçlı geliştirilmiştir.
Modelin doğruluğu gerçek dünyada garanti edilmez.
Katkıda bulunmak isteyenler pull request gönderebilir. ✅