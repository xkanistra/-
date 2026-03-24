# Программа считывает сумму всех чисел в файле

def main():
    total = 0
    number_file = open('number_list.txt', 'r')

    line = number_file.readline()

    while line != '':
        amount = int(line)
        total += amount
        line = number_file.readline()

    print(f'{total}')
    number_file.close()

if __name__ == '__main__':
    main()