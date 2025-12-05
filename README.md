Озвучка vtt субтитров в Piper TTS с помощью Python кода

Данный код предназначен для того чтобы Piper озвучивал не просто текст а текст строго по субтитрам формата .vtt решая проблему программы Subtitle Edit когда нет ускорения речи из-за чего речь не успевает завершится по времени и тогда озвучка попадает по времени на следующую озвучку и тогда происходит перебивание речи

Код Python был написан за счёт нейросетей (ChatGPT, Claude, Grok, Gemini, Le Chat, Alice Ai, DeepSeek, Qwen) без знания программирования

Установка и использование:
Установить Python.
В командной строке установить все библиотеки через команду pip install: os, sys, struct, wave, re, datetime, timedelta, pydub, AudioSegment, subprocess, run но могут быть ошибки если библиотека уже имеется так что на такое не обращайте внимания.
Для использования моего кода закиньте мои файлы в %AppData%\Subtitle Edit\TextToSpeech\Piper после установки Subtitle Edit и после закиньте субтитры формата vtt в туже папку при этом файл должен называтся input.vtt и ещё скачайте репозиторий https://huggingface.co/rhasspy/piper-voices/tree/main и от туда файлы с раширением .onnx .onnx.json закинуть в %AppData%\Subtitle Edit\TextToSpeech\Piper и после скачайте ffmpeg и положите в %AppData%\Subtitle Edit\TextToSpeech\Piper и путь к ffmpeg.exe и ffprobe.exe должен быть таким %AppData%\Subtitle Edit\TextToSpeech\Piper\ffmpeg-master-latest-win64-gpl-shared\bin потом по желанию папку %AppData%\Subtitle Edit\TextToSpeech\Piper можно перенести куда угодно потом запускаете start.py и ждите пока не появится сообщение "Нажмите Enter для закрытия..." результат будет в файле final.wav.
Список поддерживаемых языков указано в файле onnx_model_select.py

Программный код может содержать ошибки. Возможны расхождения озвучки с субтитрами
