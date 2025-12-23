Озвучка vtt субтитров в Piper TTS/RHVoice и AhoTTS с помощью Python кода

Данный код предназначен для того чтобы Piper озвучивал не просто текст а текст строго по субтитрам формата .vtt решая проблему программы Subtitle Edit когда нет ускорения речи из-за чего речь не успевает завершится по времени и тогда озвучка попадает по времени на следующую озвучку и тогда происходит перебивание речи

Код Python был написан за счёт нейросетей (ChatGPT, Claude, Grok, Gemini, Le Chat, Alice Ai, DeepSeek, Qwen) без знания программирования

Установка и использование:
Установить Python.
В командной строке установить все библиотеки через команду pip install: os, sys, struct, wave, re, datetime, timedelta, pydub, AudioSegment, subprocess, run но могут быть ошибки если библиотека уже имеется так что на такое не обращайте внимания.
Для использования моего кода закиньте мои файлы в %AppData%\Subtitle Edit\TextToSpeech\Piper после установки Subtitle Edit и после закиньте субтитры формата vtt в туже папку при этом файл должен называтся input.vtt и ещё скачайте репозиторий https://huggingface.co/rhasspy/piper-voices/tree/main и от туда файлы с раширением .onnx .onnx.json закинуть в %AppData%\Subtitle Edit\TextToSpeech\Piper и после скачайте ffmpeg и положите в %AppData%\Subtitle Edit\TextToSpeech\Piper и путь к ffmpeg.exe и ffprobe.exe должен быть таким %AppData%\Subtitle Edit\TextToSpeech\Piper\ffmpeg-master-latest-win64-gpl-shared\bin потом по желанию папку %AppData%\Subtitle Edit\TextToSpeech\Piper можно перенести куда угодно потом запускаете start.py и ждите пока не появится сообщение "Нажмите Enter для закрытия..." результат будет в файле final.wav.
Список поддерживаемых языков указано в файле onnx_model_select.py

Программный код может содержать ошибки. Возможны расхождения озвучки с субтитрами

В папке ver2 находится версия кода рассчитанная на работу с несколькими .vtt субтитрами и допустимые названия .vtt файлов вы можете узнать в файле start.py так же при озвучке следующего языка создаётся новое окно командной строки

В папке ver3 находится версия кода рассчитанная на работу с программой Balabolka с версией для командной строки. Этот версия кода была сделана для того чтобы можно было озвучить дополнительно на 10 языков неподдерживаемые самим Piper. Используется голоса RHVoice SAPI и для работы этих голосов нужно чтоб у вас была не модифицированная сборка Windows иначе большая вероятность что у вас повреждена встроенная SAPI без возможности восстановления но это решается установкой оригинальной Windows в VirtualBox.

В командной строке установить все библиотеки через команду pip install: os, sys, struct, wave, re, datetime, timedelta, pydub, AudioSegment, subprocess, run но могут быть ошибки если библиотека уже имеется так что на такое не обращайте внимания.

Windows оригинальную опасно впускать в интернет (иначе через неделю не будет работать у вас) то вы можете через команду в не VirtualBox при установленной Python скачать библеотеки: "pip download <назхвание билиотеки (wheel и setuptools тоже ставим библиотеки)> -d ./packages" а потом скаченные файлы отправляем в VirtualBox после выполняем команду "for %i in (packages\*.whl) do python -m pip install packages\%~nxi" после мы в Windows установленный вне VirtualBox копируем папку %userprofile%\AppData\Local\Programs\Python при условии что выше указанные библиотеки установлены в тот же путь на в VirtualBox и это нужно для покрытия сбоев установки библиотек

Список доступных языков для Balabolka есть в файле lang_id_select.py

Голоса SAPI5 RHVoice для Balabolka можно скачать тут: https://louderpages.org/ и https://rhvoice.org/languages/

Наличие ffmpeg.exe и ffprobe.exe с путём ffmpeg-master-latest-win64-gpl-shared\bin тоже обязательно для работы с Balabolka так же как с Piper.

Так же получить другие озвучки можно скачав автодубляж с русского на английский с вашего видео Youtube и потом перезалить видео с заменой на английскую озвучку тогда Youtube сделает автодубляж видео на 20 языков и вы их можете скачать и потом интегрировать в основное видео

В папке ver4 находится версия кода рассчитанная на работу с голосами AhoTTS Баскский и Галисийский но для скачивания этих голосов нужно будет зарегистрироватся на сайте AhoTTS https://aholab.ehu.eus/ahomytts/ потом скачать https://aholab.ehu.eus/aholab/ahosapi/ и запустить установщик и потом указать логин и пороль при установке в моем коде задействованы голоса Aitor м Brais.

Внимание! Некоторые строки на Басском и Галисийском языке могут не озвучится из-за сбоев (код 3221225477, баг в файле AhoTTSEngine.dll)

```
8:58:48 PM		0	0.00	New Event	Error Source=Application Error Message=Faulting application name: python.exe, version: 3.13.7150.1013, time stamp: 0x689df05c Faulting module name: AhoTTSEngine.dll, version: 1.0.0.1, time stamp: 0x6908e2c9 Exception code: 0xc0000005 Fault offset: 0x000000000017c8a0 Faulting process id: 0x1dcc Faulting application start time: 0x1dc70a427b7978f Faulting application path: C:\Users\Admin\AppData\Local\Programs\Python\Python313\python.exe Faulting module path: C:\Program Files\Aholab\AhoSapi64\AhoTTSEngine.dll Report Id: 013dd0d0-7d45-477d-88e2-38ac59ee22cd Faulting package full name: ? Faulting package-relative application ID: ? 	0
```

Здесь тоже нужен рабочий SAPI для Баскского и Галисийского.

В командной строке установить все библиотеки через команду pip install: os, sys, struct, wave, re, datetime, timedelta, pydub, AudioSegment, subprocess, run но могут быть ошибки если библиотека уже имеется так что на такое не обращайте внимания.

Есть альтернативный способ озвучки Баскского и Галисийского: https://github.com/hitz-zentroa/aHoTTS но не проверял и код не интегрирован с моим кодом возможно потом попробую
