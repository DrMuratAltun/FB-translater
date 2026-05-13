# AI Decisions (ADR)

1. **Framework Seçimi:** Kullanıcı arayüzü için hızlı geliştirme ve makine öğrenimi modelleri ile iyi entegrasyonu nedeniyle `Gradio` seçildi.
2. **Cihaz Optimizasyonu:** Apple Silicon M serisi işlemciler için PyTorch `mps` (Metal Performance Shaders) cihazı otomatik tespit edilerek kullanılacak şekilde ayarlandı.
3. **Model:** `facebook/nllb-200-distilled-600M` modeli yerel olarak indirilip kullanılacak. Pipeline yerine manuel `generate` metodu `mps` ile daha stabil çalıştığı için tercih edildi.
