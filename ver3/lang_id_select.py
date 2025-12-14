print("Файл lang_id_select.py запущен")

# Чтение файла .vtt
with open("input.vtt", "r", encoding="utf-8") as f:
    lines = f.readlines()

third_line = lines[2].strip()
print("Третья строка из input.vtt:", third_line)

# Словарь: язык → (параметр, значение)
mapping = {
    "Language: sq": ("-id", "1052"), #Албанский
    "Language: be": ("-id", "1059"), #Белорусский
    "Language: ky": ("-id", "1088"), #Киргизский
    "Language: mk": ("-id", "1071"), #Македонский
    "Language: tt": ("-id", "1092"), #Татарский
    "Language: tn": ("-n", "RHVoice Dimpho"), #Тсвана
    "Language: tk": ("-id", "1090"), #Туркменский
    "Language: uz": ("-id", "1091"), #Узбекский
    "Language: hr": ("-n", "RHVoice Karmela"), #Хорватский
    "Language: eo": ("-n", "RHVoice Spomenka")  # Эсперанто
}

if third_line not in mapping:
    raise ValueError("Нет подходящих моделей для текущего языка.")

param, value = mapping[third_line]

print("Параметр для balcon:", param)
print("Значение:", value)

# Записываем 2 строки в файл
with open("lang_id.txt", "w", encoding="utf-8") as f:
    f.write(param + "\n")   # 1 строка: -id или -n
    f.write(value + "\n")   # 2 строка: число или имя голоса

print("Файл lang_id.txt создан.")

print("Запуск number_line_set.py...")

with open("number_line_set.py", "r", encoding="utf-8") as f:
    exec(f.read())
