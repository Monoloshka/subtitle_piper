import os
import sys

print("Файл start.py запущен")

number_line = 0

with open("number_line.txt", "w") as f:
    f.write(str(number_line)
    )

try:
    # список возможных имен файлов
    file_candidates = [
        "Английский (Великобритания).vtt",
        "Английский (Соединенные Штаты).vtt",
        "Арабский.vtt",
        "Болгарский.vtt",
        "Каталанский.vtt",
        "Чешский.vtt",
        "Валлийский.vtt",
        "Датский.vtt",
        "Немецкий (Германия).vtt",
        "Греческий.vtt",
        "Испанский (Мексика).vtt",
        "Персидский (Иран).vtt",
        "Финский.vtt",
        "Французский (Франция).vtt",
        "Хинди.vtt",
        "Венгерский.vtt",
        "Индонезийский.vtt",
        "Исландский.vtt",
        "Итальянский.vtt",
        "Грузинский.vtt",
        "Казахский.vtt",
        "Люксембургский.vtt",
        "Латышский.vtt",
        "Малаялам.vtt",
        "Непальский.vtt",
        "Нидерландский (Бельгия).vtt",
        "Нидерландский (Нидерланды).vtt",
        "Норвежский.vtt",
        "Польский.vtt",
        "Португальский (Бразилия).vtt",
        "Румынский.vtt",
        "Русский.vtt",
        "Сербский.vtt",
        "Словацкий.vtt",
        "Словенский.vtt",
        "Шведский.vtt",
        "Суахили.vtt",
        "Телугу.vtt",
        "Турецкий.vtt",
        "Украинский.vtt",
        "Вьетнамский.vtt",
        "Китайский.vtt"
    ]
    
    found_file = None
    
    # ищем первое существующее имя файла
    for filename in file_candidates:
        if os.path.isfile(filename):
            found_file = filename
            print(f"Значение переменной found_file: {found_file}")
            break
    
    if not found_file:
        print("Файлы не найдены.")
        input("Нажмите Enter чтобы выйти...")
        sys.exit()
    
    # переименовываем найденный файл в input.vtt
    os.rename(found_file, "input.vtt")
    
    # записываем исходное имя файла
    with open("current_vtt_file.txt", "w", encoding="utf-8") as f:
        f.write(found_file)
    
    print(f"Файл {found_file} переименован в input.vtt и записан в current_vtt_file.txt")
    with open("vtt_clean.py", "r", encoding="utf-8") as f:
        exec(f.read())
except Exception as e:
    print(f"Ошибка:{e}") 
    
finally:
    input("Нажмите Enter для закрытия...")
