import win32com.client
import subprocess
import os

print("Fail send_command_to_piper.py zapushen")

try:
    with open("lang_id.txt", "r", encoding="utf-8") as f:
        name_voice = f.readline().strip()
   
    print("Znachenie peremennoy param:", name_voice)
    
    with open("number_line.txt", "r") as f:
        number_line = int(f.read())
    
    with open("input.vtt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    count = 0
    current_text = ""
    found = False 

    for i, line in enumerate(lines):
        if "-->" in line:
            count += 1
            if count == number_line:

                j = i + 1
                while j < len(lines) and lines[j].strip() != "":
                    current_text += lines[j].strip() + " "
                    j += 1
                found = True
                break

    current_text = current_text.strip()
    current_text = current_text.replace("&nbsp;", "")
    
    if found and current_text:
        print(f"Nashli text: {current_text}")
        
    out_wav = "out.wav"
        
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    
    voice_found = False
    for v in speaker.GetVoices():
        if v.GetAttribute("Name") == name_voice:
            speaker.Voice = v
            voice_found = True
            break
    
    if not voice_found:
        raise Exception(f"Golos '{name_voice}' ne naiden")
    
    stream = win32com.client.Dispatch("SAPI.SpFileStream")
    stream.Open(out_wav, 3)
    speaker.AudioOutputStream = stream
    
    speaker.Speak(current_text)
    stream.Close()
        
    print("Golos primenen korrektno, fail out.wav sozdan.")

except ValueError:
    print("Oshibka: v faile number_line.txt dolzhno byt tolko chuslo.")
except FileNotFoundError as e:
    print(f"Oshibka: Ne naiden fail -> {e.filename}")
except Exception as e:
    print("Proizoshla neozhidannaya oshibka:", e)
