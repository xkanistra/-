# Эта программа показывает 5 случайных числес
# от 1 до 100
import random

def main():
    for count in range(5):
        # Получить случайное число
        number = random.randint(1, 100)
        # Показать число
        print(number)

main()