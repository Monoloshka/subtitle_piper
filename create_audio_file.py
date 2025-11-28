import os
import sys
import struct
import wave

print("Файл create_audio_file.py запущен")

def parse_time(time_str):
    """
    Parse VTT timestamp to seconds.
    """
    time_str = time_str.strip()
    if '.' in time_str:
        seconds_part, ms_part = time_str.split('.')
        ms = float('0.' + ms_part[:3])  # Up to milliseconds
    else:
        seconds_part = time_str
        ms = 0.0
    
    time_parts = seconds_part.split(':')
    if len(time_parts) == 3:
        hours, minutes, seconds = map(int, time_parts)
    elif len(time_parts) == 2:
        hours = 0
        minutes, seconds = map(int, time_parts)
    elif len(time_parts) == 1:
        hours = 0
        minutes = 0
        seconds = int(time_parts[0])
    else:
        print("Исключение: Неверный формат времени")
        raise ValueError("Неверный формат времени")
    
    total_seconds = hours * 3600 + minutes * 60 + seconds + ms
    return total_seconds

# Get VTT file name
if len(sys.argv) > 1:
    vtt_filename = sys.argv[1]
else:
    vtt_filename = 'input.vtt'  # Default file name, change as needed
    print(f"Значение переменной vtt_filename: {vtt_filename}")

# Read the VTT file
with open(vtt_filename, 'r') as file:
    lines = file.readlines()

# Find the last line containing '-->'
last_end_time_str = None
for line in reversed(lines):
    if '-->' in line:
        parts = line.split('-->')
        if len(parts) >= 2:
            # Take the end time, split to ignore any additional info like position
            end_time_candidate = parts[1].strip().split()[0]
            last_end_time_str = end_time_candidate
            break

if last_end_time_str is None:
    raise ValueError("В файле VTT не найдена временная метка '-->'")
    print("В файле VTT не найдена временная метка '-->'")

# Parse the duration
duration_seconds = parse_time(last_end_time_str)

# Create silent WAV file
sample_rate = 48000  # Hz
print(f"Значение переменной sample_rate: {sample_rate}")
bit_depth = 24
print(f"Значение переменной bit_depth: {bit_depth}")
sample_width = bit_depth // 8  # 3 bytes
print(f"Значение переменной sample_width: {sample_width}")
channels = 1  # Mono, assume
print(f"Значение переменной channels: {channels}")

total_frames = int(duration_seconds * sample_rate)
silent_data = b'\x00' * (total_frames * channels * sample_width)

wav_filename = 'dub.wav'
print(f"Значение переменной wav_filename: {wav_filename}")
with wave.open(wav_filename, 'wb') as wav_file:
    wav_file.setnchannels(channels)
    wav_file.setsampwidth(sample_width)
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(silent_data)

print(f"Создан файл {wav_filename} с продолжительностью {duration_seconds:.3f} секунд в {sample_rate} Hz, {bit_depth}-bit.")

print("Запуск файла number_line_set.py...")

with open("number_line_set.py", "r", encoding="utf-8") as f:
    exec(f.read())