print('=== Игра: "Угадай число!" ===')
print("Я загадал число от 1 до 10. Попробуй угадать!")

secret = 5
attempts = 0

while True:
    guess = int(input("Ваше число: "))
    attempts += 1
    
    if guess == secret:
        print(f"Угадал за {attempts} попыток!")
        break
    elif guess < secret:
        print("Слишком мало!")
    else:
        print("Слишком много!")