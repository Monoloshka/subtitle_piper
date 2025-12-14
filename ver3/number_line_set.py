import os

print("Файл number_line_set.py запущен")

with open("number_line.txt", "r") as f:
    number_line = int(f.read())

if 'number_line' in locals() or 'number_line' in globals():
    number_line += 1
    print(f"Значение переменной number_line: {number_line}")
else:
    number_line = 1
    print(f"Значение переменной number_line: {number_line}")

with open("number_line.txt", "w") as f:
    f.write(str(number_line))
            
print("Запуск файла duration_line.py...")

with open("duration_line.py", "r", encoding="utf-8") as f:
    exec(f.read())