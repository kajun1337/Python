FROM python:3.10-slim

# Çalışma dizinini belirleyelim
WORKDIR /app

# Gereksinim dosyasını kopyala ve bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyala
COPY . .
ENV PYTHONUNBUFFERED=1

# Uygulamayı debugpy ile çalıştırıyoruz.
# --listen parametresi container içinde 0.0.0.0:5678'de dinler,
# --wait-for-client parametresi debugger bağlanana kadar bekler.
CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "test.py"]

# Uygulamanın ve debug portunun erişilebilir olması için expose edelim
EXPOSE 5678
