import os

try:
    print("Запуск файла create_audio_file.py...")

    with open("create_audio_file.py", "r", encoding="utf-8") as f:
        exec(f.read())
except Exception as e:
    print(f"Ошибка запуска файла: {e}") 
    
finally:
    input("Нажмите Enter для закрытия...")