import os

file_name1 = "duration_line.txt"
file_name2 = "number_line.txt"
file_name3 = "onnx_model_file.txt"
file_name4 = "start_time_str.txt"
file_name5 = "out.wav"
file_name6 = "out_speed_fixed.wav"

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

# Исходное имя файла
original_file = "dub.wav"
# Базовое имя нового файла
new_file_base = "final.wav"

# Проверяем, существует ли исходный файл
if not os.path.exists(original_file):
    print(f"Файл '{original_file}' не найден.")
else:
    new_file = new_file_base
    name, ext = os.path.splitext(new_file_base)
    counter = 1
    
    # Если файл с новым именем уже существует, добавляем цифру
    while os.path.exists(new_file):
        new_file = f"{name}{counter}{ext}"
        counter += 1
    
    os.rename(original_file, new_file)
    print(f"Файл переименован в '{new_file}'")