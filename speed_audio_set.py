import os
from pydub import AudioSegment
from subprocess import run

print("Файл speed_audio_set.py запущен")

def build_atempo_chain(speed):
    filters = []
    remaining = speed

    if speed > 1:
        while remaining > 2.0:
            filters.append("atempo=2.0")
            remaining /= 2.0
        filters.append(f"atempo={remaining:.6f}")
    else:
        while remaining < 0.5:
            filters.append("atempo=0.5")
            remaining /= 0.5
        filters.append(f"atempo={remaining:.6f}")

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

with open("duration_line.txt", "r", encoding="utf-8") as f:
    duration_line = f.read().strip()

minutes, sec_ms = duration_line.split(":")
seconds = float(sec_ms)
target_duration_ms = int(minutes) * 60000 + int(seconds * 1000)

audio = AudioSegment.from_wav(wav_path)
original_duration_ms = len(audio)

if original_duration_ms != target_duration_ms:
    speed_factor = original_duration_ms / target_duration_ms
    print("Коэффициент:", speed_factor)

    filter_chain = build_atempo_chain(speed_factor)
    print("Фильтры FFmpeg:", filter_chain)

    run([
        ffmpeg_path, "-y",
        "-i", wav_path,
        "-filter:a", filter_chain,
        "out_speed_fixed.wav"
    ])

    print("Готово: out_speed_fixed.wav")
else:
    print("Длительности совпадают — ничего делать не нужно.")
    
with open("fragment_add_to_main_audiofile.py", "r", encoding="utf-8") as f:
    print("Запуск файла fragment_add_to_main_audiofile.py...")
    exec(f.read())