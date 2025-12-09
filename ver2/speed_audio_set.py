import os
from pydub import AudioSegment
from subprocess import run

print("Файл speed_audio_set.py запущен")

def build_atempo_chain(speed):
    # Логика ТОЛЬКО для ускорения
    filters = []
    remaining = speed
    if speed > 1:
        while remaining > 2.0:
            filters.append("atempo=2.0")
            remaining /= 2.0
        filters.append(f"atempo={remaining:.6f}")
    # Блок else для замедления удален намеренно
    return ",".join(filters)

# -----------------------
# Пути к ffmpeg и ffprobe
# -----------------------
current_dir = os.getcwd()
ffmpeg_dir = os.path.join(current_dir, "ffmpeg-master-latest-win64-gpl-shared", "bin")
ffmpeg_path = os.path.join(ffmpeg_dir, "ffmpeg.exe")
ffprobe_path = os.path.join(ffmpeg_dir, "ffprobe.exe")

AudioSegment.converter = ffmpeg_path
AudioSegment.ffprobe = ffprobe_path

print("Используем FFmpeg:", ffmpeg_path)
print("Используем FFprobe:", ffprobe_path)

# -----------------------
# Основная логика
# -----------------------
wav_path = "out.wav"

# Читаем целевую длительность
with open("duration_line.txt", "r", encoding="utf-8") as f:
    duration_line = f.read().strip()

minutes, sec_ms = duration_line.split(":")
seconds = float(sec_ms)
target_duration_ms = int(minutes) * 60000 + int(seconds * 1000)

audio = AudioSegment.from_wav(wav_path)
original_duration_ms = len(audio)

# ПРОВЕРКА:
if original_duration_ms > target_duration_ms:
    # Если аудио длиннее, чем нужно -> УСКОРЯЕМ
    speed_factor = original_duration_ms / target_duration_ms
    print("Коэффициент ускорения:", speed_factor)
    
    filter_chain = build_atempo_chain(speed_factor)
    print("Фильтры FFmpeg:", filter_chain)
    
    run([
        ffmpeg_path, "-y",
        "-i", wav_path,
        "-filter:a", filter_chain,
        "out_speed_fixed.wav"
    ])
    print("Готово: out_speed_fixed.wav (Файл ускорен)")

else:
    # Если аудио короче или равно (нужно замедление или ничего не делать) ->
    # ПРОСТО КОПИРУЕМ оригинал в out_speed_fixed.wav
    print("Ускорение не требуется (или требовалось замедление).")
    print("Сохраняем оригинал как out_speed_fixed.wav для продолжения работы.")
    
    # Используем pydub для сохранения копии (так как audio уже загружено в память)
    audio.export("out_speed_fixed.wav", format="wav")

# Запуск следующего скрипта
with open("fragment_add_to_main_audiofile.py", "r", encoding="utf-8") as f:
    print("Запуск файла fragment_add_to_main_audiofile.py...")
    exec(f.read())