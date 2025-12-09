import subprocess
import os

print("Файл send_command_to_piper.py запущен")

try:
    # 1. Читаем номер строки
    with open("number_line.txt", "r") as f:
        number_line = int(f.read())
    
    # 2. Читаем файл субтитров
    with open("input.vtt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    # 3. Логика поиска текста
    count = 0
    current_text = ""
    found = False  # Флаг — нашли мы текст или нет

    for i, line in enumerate(lines):
        if "-->" in line:
            count += 1
            if count == number_line:
                # Начинаем со следующей строки
                j = i + 1
                while j < len(lines) and lines[j].strip() != "":
                    current_text += lines[j].strip() + " "
                    j += 1
                found = True
                break

    current_text = current_text.strip()
    
    with open("onnx_model_file.txt", "r", encoding="utf-8") as file:
        linestxt = file.readlines()
    
    onnx_model_file = linestxt[0].strip()
   
    print("Используемая модель: onnx_model_file", onnx_model_file)
    
    if found and current_text:
        print(f"Нашли текст: {current_text}")

        # --- БЛОК ЗАПУСКА PIPER ---
        print("Запускаем Piper...")
        current_dir = os.getcwd()
        piper_path = os.path.join(current_dir, "piper.exe")
        command = [
            piper_path,
            "-m", f"{onnx_model_file}.onnx",
            "-c", f"{onnx_model_file}.onnx.json",
            "-f", "out.wav"
        ]

        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        stdout_data, stderr_data = process.communicate(
            input=current_text.encode('utf-8')
        )

        if process.returncode == 0:
            print("Готово! Файл out.wav создан.")
        else:
            print("Ошибка Piper:")
            print(stderr_data.decode('utf-8', errors='ignore'))
        # --------------------------

    else:
        print(f"Субтитр номер {number_line} не найден или он пустой.")

except ValueError:
    print("Ошибка: в файле number_line.txt должно быть только число.")
except FileNotFoundError as e:
    print(f"Ошибка: Не найден файл -> {e.filename}")
except Exception as e:
    print("Произошла неожиданная ошибка:", e)

print("Запуск файла create_audio_file.py...")

with open("create_audio_file.py", "r", encoding="utf-8") as f:
    exec(f.read())
