# Функция получает число в аргумент и показывает результат уможенный на 10

def main():
    number = int(input("Введите число: "))
    result = times_ten(number)
    print(result)

def times_ten(num):
    result = num * 10
    return result

main()
