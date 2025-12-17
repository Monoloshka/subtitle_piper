print("Файл lang_id_select.py запущен")

# Чтение файла .vtt
with open("input.vtt", "r", encoding="utf-8") as f:
    lines = f.readlines()

third_line = lines[2].strip()
print("Третья строка из input.vtt:", third_line)

# Словарь: язык → (параметр, значение)
mapping = {
    "Language: eu": "AhoTTS_Aitor_eu", #Баскский
    "Language: gl": "AhoTTS_Brais_gl", #Галисийский
}

if third_line not in mapping:
    raise ValueError("Нет подходящих моделей для текущего языка.")

name_voice = mapping[third_line]

print("Значение переменной name_voice:", name_voice)

# Записываем 2 строки в файл
with open("lang_id.txt", "w", encoding="utf-8") as f:
    f.write(name_voice + "\n")   # 1 строка: -id или -n

print("Файл lang_id.txt создан.")

print("Запуск number_line_set.py...")

with open("number_line_set.py", "r", encoding="utf-8") as f:
    exec(f.read())
