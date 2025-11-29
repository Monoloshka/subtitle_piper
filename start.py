import os

try:
    print("Запуск файла vtt_clean.py...")

    with open("vtt_clean.py", "r", encoding="utf-8") as f:
        exec(f.read())
except Exception as e:
    print(f"Ошибка:{e}") 
    
finally:
    input("Нажмите Enter для закрытия...")