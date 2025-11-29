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

    if found and current_text:
        print(f"Нашли текст: {current_text}")

        # --- БЛОК ЗАПУСКА PIPER ---
        print("Запускаем Piper...")

        command = [
            r"C:\Users\Admin\AppData\Roaming\Subtitle Edit\TextToSpeech\Piper\piper.exe",
            "-m", "kk_KZ-issai-high.onnx",
            "-c", "kk_KZ-issai-high.onnx.json",
            "-f", "out.wav"
        ]

        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
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

print("Запуск файла speed_audio_set.py...")

with open("speed_audio_set.py", "r", encoding="utf-8") as f:
    exec(f.read())
