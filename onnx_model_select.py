print("Файл onnx_model_select.py запущен")

# Чтение файла .vtt
with open("input.vtt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Получаем третью строку
third_line = lines[2].strip()
print("Третья строка из input.vtt:", third_line)

# Словарь соответствия языков и моделей
mapping = {
    "Language: ar": "ar_JO-kareem-low",
    "Language: bg": "bg_BG-dimitar-medium",
    "Language: ca": "ca_ES-upc_ona-medium",
    "Language: cs": "cs_CZ-jirka-medium",
    "Language: cy": "cy_GB-bu_tts-medium",
    "Language: da": "da_DK-talesyntese-medium",
    "Language: de": "de_DE-thorsten-high",
    "Language: el": "el_GR-rapunzelina-low",
    "Language: es": "es_MX-claude-high",
    "Language: fa": "fa_IR-gyro-medium",
    "Language: fi": "fi_FI-harri-medium",
    "Language: fr": "fr_FR-tom-medium",
    "Language: hi": "hi_IN-pratham-medium",
    "Language: hu": "hu_HU-imre-medium",
    "Language: id": "id_ID-news_tts-medium",
    "Language: is": "is_IS-steinn-medium",
    "Language: it": "it_IT-riccardo-x_low",
    "Language: ka": "ka_GE-natia-medium",
    "Language: kz": "kk_KZ-issai-high",
    "Language: lb": "lb_LU-marylux-medium",
    "Language: lv": "lv_LV-aivars-medium",
    "Language: ml": "ml_IN-arjun-medium",
    "Language: ne": "ne_NP-google-medium",
    "Language: nl-BE": "nl_BE-rdh-medium",
    "Language: nl": "nl_NL-mls-medium",
    "Language: no": "no_NO-talesyntese-medium",
    "Language: pl": "pl_PL-darkman-medium",
    "Language: pt": "pt_BR-faber-medium",
    "Language: ro": "ro_RO-mihai-medium",
    "Language: ru": "ru_RU-dmitri-medium",
    "Language: sk": "sk_SK-lili-medium",
    "Language: sl": "sl_SI-artur-medium",
    "Language: sr": "sr_RS-serbski_institut-medium",
    "Language: sv": "sv_SE-nst-medium",
    "Language: sw": "sw_CD-lanfrica-medium",
    "Language: te": "te_IN-venkatesh-medium",
    "Language: tr": "tr_TR-dfki-medium",
    "Language: ua": "uk_UA-ukrainian_tts-medium",
    "Language: vi": "vi_VN-vais1000-medium",
    "Language: zh": "zh_CN-huayan-medium"
}

# Проверяем, есть ли язык в словаре
if third_line in mapping:
    onnx_model_file = mapping[third_line]
    print("Значение переменной onnx_model_file:", onnx_model_file)
else:
    raise ValueError("Нет подходящих моделей для текущего языка.")

# Записываем результат в файл
with open("onnx_model_file.txt", "w", encoding="utf-8") as f:
    f.write(onnx_model_file)

print("Запуск файла create_audio_file.py...")

with open("create_audio_file.py", "r", encoding="utf-8") as f:
    exec(f.read())