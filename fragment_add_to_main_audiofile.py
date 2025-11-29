from pydub import AudioSegment

print("Файл fragment_add_to_main_audiofile.py запущен")

with open("start_time_str.txt", "r", encoding="utf-8") as f:
    start_str = f.read().strip()
    print(f"Значение переменной start_str: {start_str}")
    
main = AudioSegment.from_wav("dub.wav")
print(f"Значение переменной main: {main}")
insert = AudioSegment.from_wav("out_speed_fixed.wav")
print(f"Значение переменной insert: {insert}")

def parse_time_to_ms(time_str):
    parts = time_str.split(":")

    if len(parts) == 2:  # MM:SS.mmm
        minutes = int(parts[0])
        seconds = float(parts[1])
        return int((minutes * 60 + seconds) * 1000)

    elif len(parts) == 3:  # HH:MM:SS.mmm
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = float(parts[2])
        return int((hours * 3600 + minutes * 60 + seconds) * 1000)

    else:
        raise ValueError(f"Неверный формат start_str: {time_str}")

start_ms = parse_time_to_ms(start_str)

if start_ms + len(insert) > len(main):
    raise ValueError("Невозможно вставить: звук выходит за пределы основного трека")
    
main = main.overlay(insert, position=start_ms)

main.export("dub.wav", format="wav")

with open("number_line_set.py", "r", encoding="utf-8") as f:
    print("Запуск файла number_line_set.py...")
    exec(f.read())