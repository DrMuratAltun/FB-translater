import gradio as gr
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import logging

logging.basicConfig(level=logging.INFO)

# Popüler diller ve NLLB-200 dil kodları
LANGUAGES = {
    "İngilizce": "eng_Latn",
    "Türkçe": "tur_Latn",
    "Almanca": "deu_Latn",
    "Fransızca": "fra_Latn",
    "İspanyolca": "spa_Latn",
    "İtalyanca": "ita_Latn",
    "Rusça": "rus_Cyrl",
    "Arapça": "arb_Arab",
    "Çince (Basitleştirilmiş)": "zho_Hans",
    "Japonca": "jpn_Jpan",
    "Korece": "kor_Hang"
}

model_name = "facebook/nllb-200-distilled-600M"

# Cihaz tespiti (Mac M-Serisi için MPS)
device = "cpu"
if torch.backends.mps.is_available():
    device = "mps"
elif torch.cuda.is_available():
    device = "cuda"

logging.info(f"Kullanılan cihaz: {device}")
logging.info("Model yükleniyor, bu işlem ilk seferde biraz zaman alabilir...")

# Model ve Tokenizer yükleme
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)

logging.info("Model başarıyla yüklendi!")

def translate(text, src_lang, tgt_lang):
    if not text.strip():
        return ""
    
    src_code = LANGUAGES.get(src_lang, "eng_Latn")
    tgt_code = LANGUAGES.get(tgt_lang, "tur_Latn")
    
    try:
        # Kaynak dili ayarla
        tokenizer.src_lang = src_code
        
        # Girdiyi tokenize et ve cihaza gönder
        inputs = tokenizer(text, return_tensors="pt").to(device)
        
        # Hedef dil için zorunlu başlangıç tokeni ID'sini al
        forced_bos_token_id = tokenizer.convert_tokens_to_ids(tgt_code)
        
        # Çeviriyi üret
        with torch.no_grad():
            translated_tokens = model.generate(
                **inputs, 
                forced_bos_token_id=forced_bos_token_id, 
                max_length=512,
                num_beams=4 # Daha kaliteli çeviri için beam search
            )
        
        # Tokenleri metne dönüştür
        result = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
        return result
    except Exception as e:
        logging.error(f"Çeviri hatası: {e}")
        return f"Hata oluştu: {str(e)}"

# Gradio Arayüzü
with gr.Blocks(title="NLLB-200 Çeviri", theme=gr.themes.Soft()) as demo:
    gr.Markdown(f"""
    # 🌍 NLLB-200 Çeviri Arayüzü
    **Model:** `{model_name}` | **Donanım Hızlandırma:** `{device.upper()}`
    
    Bu arayüz, Meta'nın NLLB-200 modeliyle internet gerektirmeden bilgisayarınızda yerel ve hızlı çeviri yapar.
    """)
    
    with gr.Row():
        with gr.Column():
            src_lang = gr.Dropdown(choices=list(LANGUAGES.keys()), value="İngilizce", label="Kaynak Dil")
            src_text = gr.Textbox(lines=6, label="Çevrilecek Metin", placeholder="Metninizi buraya yapıştırın veya yazın...")
            btn = gr.Button("Çevir 🚀", variant="primary")
        
        with gr.Column():
            tgt_lang = gr.Dropdown(choices=list(LANGUAGES.keys()), value="Türkçe", label="Hedef Dil")
            out_text = gr.Textbox(lines=6, label="Çeviri Sonucu", interactive=False)
            
    btn.click(fn=translate, inputs=[src_text, src_lang, tgt_lang], outputs=out_text)
    
    # Enter tuşu ile de çeviri yapabilmek için (metin kutusundayken)
    # src_text.submit(fn=translate, inputs=[src_text, src_lang, tgt_lang], outputs=out_text)

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, inbrowser=True)
