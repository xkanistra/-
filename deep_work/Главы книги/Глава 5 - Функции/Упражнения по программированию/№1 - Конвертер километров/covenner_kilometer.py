# Программа конветирует введенные пользователем киллометры в мили

def main():
    kilometer = float(input('Введите число пройденных километров: '))
    result = coventer(kilometer)
    print(f'Пройдено {result:.2f} миль')

def coventer(kilometer):
    return kilometer * 0.6214

main()