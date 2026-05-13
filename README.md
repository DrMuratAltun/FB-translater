# NLLB-200 Çeviri Arayüzü (Mac Silicon Optimize)

Bu proje, Meta'nın [facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M) modelini yerel ortamda çalıştırmak için hazırlanmış, `Gradio` tabanlı modern ve hızlı bir çeviri arayüzüdür.

Özellikle **Apple Silicon (M1/M2/M3)** cihazlar için `mps` (Metal Performance Shaders) donanım hızlandırmasını destekler. Bu sayede çeviri süreleri cihazınızın kapasitesine göre önemli ölçüde hızlanır.

## Özellikler

- **Yerel Çeviri (Offline):** İnternet bağlantısına ihtiyaç duymadan, verilerinizi üçüncü parti API'lerle paylaşmadan gizlilik içerisinde çalışır.
- **Donanım Hızlandırma:** `mps` ve `cuda` (eğer desteklenen bir bilgisayarda çalıştırılıyorsa) otomatik olarak tespit edilir ve aktif hale gelir.
- **Kullanıcı Dostu Arayüz:** Gradio tabanlı temiz, modern ve kullanımı kolay bir arayüz.
- **11 Seçili Dil Desteği:** İngilizce, Türkçe, Almanca, Fransızca, İspanyolca, İtalyanca, Rusça, Arapça, Çince, Japonca, Korece. (NLLB-200 normalde 200 dili destekler, bu sayı arayüzden kolayca arttırılabilir.)

## Kurulum

### Gereksinimler

- Python 3.8 veya üzeri
- Mac Silicon işlemciler (M1/M2/M3 vb.) için tam uyumluluk ve yüksek hız sunar.

### Başlangıç

1. Depoyu bilgisayarınıza klonlayın:
   ```bash
   git clone https://github.com/DrMuratAltun/FB-translater.git
   cd FB-translater
   ```

2. Ortam kurulumunu yapın ve çalıştırın:
   Linux/Mac için hazırlanan `run.sh` scripti sanal ortamı (`venv`) otomatik kurar, bağımlılıkları indirir ve arayüzü başlatır:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

3. Kurulum tamamlandıktan sonra tarayıcınızda otomatik olarak arayüz sekmesi (`http://127.0.0.1:7860`) açılacaktır. (İlk kurulumda modelin indirilmesi birkaç dakika sürebilir).

## Dosya Yapısı

- `app.py`: Ana Gradio uygulaması ve model çalıştırma mantığı.
- `requirements.txt`: Python paket bağımlılıkları.
- `run.sh`: Tek tuş kurulum ve çalıştırma betiği.
- `docs/`, `CLAUDE.md`, `GEMINI.md`: Yapay zeka ajanları iletişim ve mimari karar dosyaları.

## Teknolojiler
- **[Hugging Face Transformers](https://huggingface.co/docs/transformers/index)**
- **[PyTorch](https://pytorch.org/)**
- **[Gradio](https://gradio.app/)**
- **[NLLB-200](https://ai.meta.com/research/no-language-left-behind/)**
