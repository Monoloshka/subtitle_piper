print("Файл onnx_model_select.py запущен")

# Чтение файла .vtt
with open("input.vtt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Получаем третью строку
third_line = lines[2].strip()
print("Третья строка из input.vtt:", third_line)

# Словарь соответствия языков и моделей
mapping = {
    "Language: en-GB": "en_GB-cori-high", #English Great Britain Английский Великобритания
    "Language: en-US": "en_US-ryan-high", #English United States Английский Соединенные Штаты
    "Language: ar": "ar_JO-kareem-medium", #Arabic Jordan Aрабский Иордания
    "Language: bg": "bg_BG-dimitar-medium", #Bulgarian Bulgaria Болгарский Болгария 
    "Language: ca": "ca_ES-upc_ona-medium", #Catalan Spain Каталанский Испания
    "Language: cs": "cs_CZ-jirka-medium", #Czech Czech Republic Чешский Чехия
    "Language: cy": "cy_GB-bu_tts-medium", #Welsh Great Britain Валлийский Великобритания
    "Language: da": "da_DK-talesyntese-medium", #Danish Denmark Датский Дания
    "Language: de": "de_DE-thorsten-high", #German Germany Немецкий Германия 
    "Language: de-DE": "de_DE-thorsten-high", #German Germany Немецкий Германия 
    "Language: el": "el_GR-rapunzelina-low", #Greek Greece Греческий Греция
    "Language: es": "es_MX-claude-high", #Spanish Mexico Испанский Мексика
    "Language: es-MX": "es_MX-claude-high", #Spanish Mexico Испанский Мексика 
    "Language: fa": "fa_IR-gyro-medium", #Farsi Iran Персидский Иран
    "Language: fa-IR": "fa_IR-gyro-medium", #Farsi Iran Персидский Иран
    "Language: fi": "fi_FI-harri-medium", #Finnish Finland Финский Финляндия
    "Language: fr": "fr_FR-tom-medium", #French France Французский Франция
    "Language: fr-FR": "fr_FR-tom-medium", #French France Французский Франция
    "Language: hi": "hi_IN-pratham-medium", #Hindi India Хинди Индия
    "Language: hu": "hu_HU-imre-medium", #Hungarian Hungary Венгерский Венгрия
    "Language: id": "id_ID-news_tts-medium", #Indonesian Indonesia Индонезийский Индонезия
    "Language: is": "is_IS-steinn-medium", #Icelandic Iceland Исландский Исландия
    "Language: it": "it_IT-riccardo-x_low", #Italian Italy Итальянский Италия 
    "Language: ka": "ka_GE-natia-medium", #Georgian Georgia Грузинский Грузия
    "Language: kz": "kk_KZ-issai-high", #Kazakh Kazakhstan Казахский Казахстан 
    "Language: kk": "kk_KZ-issai-high", #Kazakh Kazakhstan Казахский Казахстан 
    "Language: lb": "lb_LU-marylux-medium", #Luxembourgish Luxembourg Люксембургский Люксембург 
    "Language: lv": "lv_LV-aivars-medium", #Latvian Latvia Латышский Латвия
    "Language: ml": "ml_IN-arjun-medium", #Malayalam India Малаялам Индия 
    "Language: ne": "ne_NP-google-medium", #Nepali Nepal Непальский Непал 
    "Language: nl-BE": "nl_BE-rdh-medium", #Dutch Belgium Нидерландский Бельгия 
    "Language: nl-NL": "nl_NL-mls-medium", #Dutch Netherlands Нидерландский Нидерланды 
    "Language: no": "no_NO-talesyntese-medium", #Norwegian Norway Норвежский Норвегия 
    "Language: pl": "pl_PL-darkman-medium", #Polish Poland Польский Польша 
    "Language: pt": "pt_BR-faber-medium", #Portuguese Brazil Португальский Бразилия
    "Language: pt-BR": "pt_BR-faber-medium", #Portuguese Brazil Португальский Бразилия
    "Language: ro": "ro_RO-mihai-medium", #Romanian Romania Румынский Румыния
    "Language: ru": "ru_RU-dmitri-medium", #Russian Russia Русский Россия 
    "Language: sk": "sk_SK-lili-medium", #Slovak Slovakia Словацкий Словакия
    "Language: sl": "sl_SI-artur-medium", #Slovenian Slovenia Словенский Словения
    "Language: sr": "sr_RS-serbski_institut-medium", #Serbian Serbia Сербский Сербия
    "Language: sv": "sv_SE-nst-medium", #Swedish Sweden Шведский Швеция
    "Language: sw": "sw_CD-lanfrica-medium", #Swahili Democratic Republic of the Congo Суахили Демократическая Республика Конго
    "Language: te": "te_IN-venkatesh-medium", #Telugu India Телугу Индия
    "Language: tr": "tr_TR-dfki-medium", #Turkish Turkey Турецкий Турция 
    "Language: ua": "uk_UA-ukrainian_tts-medium", #Ukrainian Ukraine Украинский Украина
    "Language: uk": "uk_UA-ukrainian_tts-medium", #Ukrainian Ukraine Украинский Украина
    "Language: vi": "vi_VN-vais1000-medium", #Vietnamese Vietnam Вьетнамский Вьетнам
    "Language: zh": "zh_CN-huayan-medium" #Chinese China Китайский Китай
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

print("Запуск файла number_line_set.py...")

with open("number_line_set.py", "r", encoding="utf-8") as f:
    exec(f.read())