#!/bin/bash
echo "Sanal ortam (venv) kontrol ediliyor..."
if [ ! -d "venv" ]; then
    echo "Sanal ortam oluşturuluyor..."
    python3 -m venv venv
fi

echo "Sanal ortam aktifleştiriliyor..."
source venv/bin/activate

echo "Gerekli kütüphaneler yükleniyor (bu biraz zaman alabilir)..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Uygulama başlatılıyor..."
python app.py
