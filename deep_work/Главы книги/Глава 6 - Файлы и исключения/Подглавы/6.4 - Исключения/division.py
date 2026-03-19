# Программа демонстрирует работу исключения при делении числа на 0

def main():
    num1 = int(input('Введите число:'))
    num2 = int(input('Введите число:'))

    result = num1 / num2
    print(f'{num1} делится на {num2} равно {result}')

if __name__ == '__main__':
    main()