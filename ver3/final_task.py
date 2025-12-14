import os

print("Файл final_task.py запущен")

file_name1 = "duration_line.txt"
file_name2 = "number_line.txt"
file_name3 = "lang_id.txt"
file_name4 = "start_time_str.txt"
file_name5 = "out.wav"
file_name6 = "out_speed_fixed.wav"
file_name7 = "input.vtt"

if os.path.exists(file_name1):
    os.remove(file_name1)
    print(f"Файл '{file_name1}' удалён.")
else:
    print(f"Файл '{file_name1}' не найден.")
    
if os.path.exists(file_name2):
    os.remove(file_name2)
    print(f"Файл '{file_name2}' удалён.")
else:
    print(f"Файл '{file_name2}' не найден.")
    
if os.path.exists(file_name3):
    os.remove(file_name3)
    print(f"Файл '{file_name3}' удалён.")
else:
    print(f"Файл '{file_name3}' не найден.")
    
if os.path.exists(file_name4):
    os.remove(file_name4)
    print(f"Файл '{file_name4}' удалён.")
else:
    print(f"Файл '{file_name4}' не найден.")

if os.path.exists(file_name5):
    os.remove(file_name5)
    print(f"Файл '{file_name5}' удалён.")
else:
    print(f"Файл '{file_name5}' не найден.")
    
if os.path.exists(file_name6):
    os.remove(file_name6)
    print(f"Файл '{file_name6}' удалён.")
else:
    print(f"Файл '{file_name6}' не найден.")
    
if os.path.exists(file_name7):
    os.remove(file_name7)
    print(f"Файл '{file_name7}' удалён.")
else:
    print(f"Файл '{file_name7}' не найден.")

# Исходное имя файла
original_file = "dub.wav"
# Базовое имя нового файла
with open("current_vtt_file.txt", "r", encoding="utf-8") as f:
    current_vtt_file = f.read().strip()
current_lang = current_vtt_file[:-4]
new_file_base =  current_lang + ".wav"

# Проверяем, существует ли исходный файл
if not os.path.exists(original_file):
    print(f"Файл '{original_file}' не найден.")
else:
    new_file = new_file_base        
    os.rename(original_file, new_file)
    print(f"Файл переименован в '{new_file}'")
    
number_line = 0
    
print("Запуск файла start.py...")

os.startfile("start.py")