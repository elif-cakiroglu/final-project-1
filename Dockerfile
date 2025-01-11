# Python 3.9 tabanlı imajdan başla
FROM python:3.9

# Uygulama için çalışma dizini oluştur
WORKDIR /app

# Gereksinimler dosyasını kopyala
COPY requirements.txt /app/

# Pip'i güncelle
RUN pip install --upgrade pip

# Gereksinimleri yükle
RUN pip install -r requirements.txt

# Flask, Pandas gibi ek kütüphaneleri yükle
RUN pip install --upgrade flask==2.1.3 werkzeug==2.1.0 pandas numpy

# Uygulama dosyasını kopyala
COPY . /app/

# Uygulama çalıştırma komutu
CMD ["python3", "DebService.py"]

