# Программа моделирует работу вложенных циклов для
# работы электронных часов.

for hours in range(24):
    for minute in range(60):
        for second in range(60):
            print(f'{hours}:{minute}:{second}')