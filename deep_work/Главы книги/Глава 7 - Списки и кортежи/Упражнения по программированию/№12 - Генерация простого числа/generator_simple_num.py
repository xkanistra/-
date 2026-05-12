# Генерация простых чисел до указанного числа начиная с 2

def main():
    num_list = add_list()
    print(num_list)

def add_list():
    num_list = []
    num = int(input('Введите число до которого хотите увидеть список: '))
    
    while num == 1:
        num = int(input('Введенное число должно быть > 1, попробуйте снова: '))

    for num in range(2, num + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                num_list.append(num)
    return num_list

if __name__ == '__main__':
    main()