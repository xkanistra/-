# Программа запрашивает ряд чисел без разделителя и выводит сумму чисел

def main():
    numbers_string = get_numbers()
    total_numbers = get_total(numbers_string)
def get_numbers():
    num = input('Введите ряд чисел без разделителя(без пробелов/,/:/;/. и т.п): ')
    return num

def get_total(numbers_string):
    total_num = 0
    for num in numbers_string:
        total_num += int(num)
    print(total_num)
    
if __name__ == '__main__':
    main()