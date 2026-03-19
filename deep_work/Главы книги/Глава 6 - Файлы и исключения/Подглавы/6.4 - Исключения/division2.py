# Это пример корректного предотвращения исключения.

def main():
    num1 = int(input('Введите число:'))
    num2 = int(input('Введите число:'))

    if num2 == 0:
        print('Ошибка, деление на 0 невозможно')
    else:
        result = num1 / num2
        print(f'{num1} делится на {num2} равно {result}')

if __name__ == '__main__':
    main()