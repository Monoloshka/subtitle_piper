import re
from datetime import timedelta
import os

print("Файл duration_line.py запущен")

with open("number_line.txt", "r") as f:
    number_line = int(f.read())

print(f"Значение переменной number_line: {number_line}")

final_task = 0

def parse_time(time_str):
    """Преобразует 'MM:SS.mmm' или 'HH:MM:SS.mmm' в миллисекунды."""
    parts = re.split(r'[:.]', time_str)

    if len(parts) == 3:  # MM:SS.mmm
        minutes = int(parts[0])
        seconds = int(parts[1])
        millis = int(parts[2])
        hours = 0

    elif len(parts) == 4:  # HH:MM:SS.mmm
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
        millis = int(parts[3])

    else:
        raise ValueError(f"Неверный формат времени: {time_str}")

    return ((hours * 3600) + (minutes * 60) + seconds) * 1000 + millis


def format_time_from_millis(total_millis):
    """Преобразует миллисекунды в строку вида 'MM:SS.mmm'."""
    total_seconds = total_millis // 1000
    millis = total_millis % 1000
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes:02d}:{seconds:02d}.{millis:03d}"


def main():

    global final_task

    # Шаг 2: найти n-ю строку с временной меткой в input.vtt
    timestamp_pattern = re.compile(
        r'(\d{2}:\d{2}:\d{2}\.\d{3}|\d{2}:\d{2}\.\d{3}) --> '
        r'(\d{2}:\d{2}:\d{2}\.\d{3}|\d{2}:\d{2}\.\d{3})'
    )

    matches = []

    try:
        with open("input.vtt", "r", encoding="utf-8") as f:
            for line in f:
                match = timestamp_pattern.search(line)
                if match:
                    matches.append((match.group(1), match.group(2)))

    except FileNotFoundError:
        print("Файл input.vtt не найден.")
        print("Запуск файла other_file.py...")
        os.startfile("other_file.py")
        return

    # Шаг 3: проверить, есть ли n-я запись (нумерация с 1)
    if number_line < 1 or number_line > len(matches):
        print(f"Не найдено {number_line}-й временной метки.")
        final_task = 1
        print(f"Значение переменной final_task: {final_task}")
        print("Запуск файла final_task.py...")
        with open("final_task.py", "r", encoding="utf-8") as f:
            exec(f.read())
        return

    start_str, end_str = matches[number_line - 1]
    print(f"Значение переменной start_str {start_str}")
    print(f"Значение переменной end_str {end_str}")

    # Шаг 4: вычислить разницу
    try:
        start_ms = parse_time(start_str)
        end_ms = parse_time(end_str)
        duration_ms = end_ms - start_ms

        if duration_ms < 0:
            raise ValueError("Конечное время меньше начального")

        result_str = format_time_from_millis(duration_ms)

    except Exception as e:
        print(f"Ошибка при вычислении разницы: {e}")
        final_task = 1
        print(f"Значение переменной final_task: {final_task}")
        print("Запуск файла final_task.py...")
        with open("final_task.py", "r", encoding="utf-8") as f:
            exec(f.read())
        return

    # Шаг 5: сохранить результат
    with open("duration_line.txt", "w", encoding="utf-8") as f:
        f.write(result_str)

    with open("start_time_str.txt", "w", encoding="utf-8") as f:
        f.write(start_str)

    print(f"Результат: {result_str} сохранён в duration_line.txt")

# Запуск main() — и только если final_task == 0
if final_task == 0:
    if __name__ == "__main__":
        main()
else:
    print("\n")

# И только после main() — принимаем окончательное решение
if final_task == 0:
    with open("send_command_to_piper.py", "r", encoding="utf-8") as f:
        print(f"Значение переменной final_task: {final_task}")
        print("Запуск файла send_command_to_piper.py...")
        exec(f.read())
else:
    print("Запуск send_command_to_piper.py отменён")