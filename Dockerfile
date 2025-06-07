# Resmi Python 3.10 imajı
FROM python:3.10-slim

# Çalışma dizinini oluşturma ve belirleme
WORKDIR /app

# Gereksinim dosyasını kopyalama ve bağımlılıkları yükleme
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyalama
COPY . .

# Uvicorn ile FastAPI app'ını başlat
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8502"]