print("Файл vtt_clean.py запущен")

vtt_file = "input.vtt"

with open(vtt_file, "r", encoding="utf-8") as f:
    content = f.read()

# Полное удаление "&nbsp;"
content = content.replace("&nbsp;", "")

with open(vtt_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Все '&nbsp;' удалены из файла.")
            
print("Запуск файла onnx_model_select.py...")

with open("onnx_model_select.py", "r", encoding="utf-8") as f:
    exec(f.read())