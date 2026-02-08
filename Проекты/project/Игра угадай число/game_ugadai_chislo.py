print('=== Игра: "Угадай число!" ===')
print("Я загадал число от 1 до 10. Попробуй угадать!")

# Загаданное число
SECRET = 5 

number = int(input('Введите число: '))

if number == SECRET:
    print("Поздравляю! Ты угадал!")

elif number < SECRET:
    print('Слишком мало!')

elif number > SECRET:
    print('Слишком много!')   

attempt = 1
print(f'~~~~ Количество попыток: {attempt} ~~~~')