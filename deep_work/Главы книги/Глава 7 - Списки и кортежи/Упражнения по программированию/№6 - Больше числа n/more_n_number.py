# Сравнение введенного числа с числом n

def main():
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n_number = int(input('Введите значение числа n: '))
    comparison(numbers_list, n_number)

def comparison(num_list, n):
    for item in num_list:
        if item > n:
            print(item, end=' ')


if __name__ == '__main__':
    main()