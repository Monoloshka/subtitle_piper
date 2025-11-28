# Глобальные переменные
for name, value in list(globals().items()):
    if isinstance(value, (bytes, bytearray)):
        print(f"Глобальные переменные: {name} - <bytes, length {len(value)}>")
    elif isinstance(value, (wave.Wave_write, AudioSegment)):
        print(f"Глобальные переменные: {name} - <{type(value).__name__}>")
    else:
        print(f"Глобальные переменные: {name} - {value}")

# Локальные переменные
for name, value in list(locals().items()):
    if isinstance(value, (bytes, bytearray)):
        print(f"Локальные переменные: {name} - <bytes, length {len(value)}>")
    elif isinstance(value, (wave.Wave_write, AudioSegment)):
        print(f"Локальные переменные: {name} - <{type(value).__name__}>")
    else:
        print(f"Локальные переменные: {name} - {value}")