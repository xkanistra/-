print('=== Игра: "Угадай число!" ===')
print("Я загадал число от 1 до 50. Попробуй угадать!")

# Загаданное число
SECRET = 15

a = input("Нажмите <Enter> чтобы начать ")

attempt = 0
if attempt < 5:
    while attempt < 5:
        number = int(input("Введите число: "))

        if number == SECRET:
            print("Поздравляю! Ты угадал!")
            break

        elif number < SECRET:
            print("Слишком мало!")

        elif number > SECRET:
            print("Слишком много!")

        attempt += 1

        print(f"~~~~ Количество попыток: {attempt} ~~~~")

print("Вы проиграли, попытки закончились")

