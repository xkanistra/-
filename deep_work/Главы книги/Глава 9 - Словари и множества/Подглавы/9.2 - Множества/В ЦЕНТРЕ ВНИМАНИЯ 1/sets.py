# Программа содержит множества которые содержат имена членов баскетбольной и бейсбольных команд

baseball = set(['Джоди', 'Кармен', 'Аида', 'Алисия'])
basketball = set(['Ева', 'Кармен', 'Алисия', 'Сара'])

# Показать игроков бейсбольной команды
print('Эти студенты состоят в бейсбольной команде: ')
for name in baseball:
    print(name)

# Показать игроков баскетбольной команды
print()
print('Эти студенты состоят в баскетбольной команде: ')
for name in baseball:
    print(name)

# Показать пересечение
print()
print('Эти студенты играют и в бейсбол, и в баскетбол: ')
for name in baseball.intersection(basketball):
    print(name)

# Показать объединение
print()
print('Эти студенты играют в одну или обе игры: ')
for name in baseball.union(basketball):
    print(name)

# Показать разность между бейсбольной и баскетбольной командами
print()
print('Эти студенты играют в бейсбол, но не играют в баскетбол: ')
for name in baseball.difference(basketball):
    print(name)

# Показать разность между баскетбольной и бейсбольной командами
print()
print('Эти студенты играют в баскетбол, но не играют в баскетбол: ')
for name in basketball.intersection(baseball):
    print(name)

# Показать симметрическую разность
print()
print('Эти студенты играют одну из игр, но не в обе одновременно: ')
for name in baseball.symmetric_difference(basketball):
    print(name)