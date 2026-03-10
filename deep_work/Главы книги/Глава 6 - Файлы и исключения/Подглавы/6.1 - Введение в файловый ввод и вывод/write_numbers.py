# Программа демонстрирует
# преобразование числовых значений в строковые перед их
# записью в текстовый файл

def main():
    # Открыть файл для записи
    outfile = open('numbers.txt', 'w')

    # Получить от пользователя 3 числа
    num1 = int(input('Введите число:'))  
    num2 = int(input('Введите еще одно число:')) 
    num3 = int(input('Введите еще одно число:'))   

    # Записать эти три числа в файл
    outfile.write(f'{str(num1)}\n')
    outfile.write(f'{str(num2)}\n')
    outfile.write(f'{str(num3)}\n')

    # Закрыть файл
    outfile.close()
    print('Данные записаны в numbers.txt')

if __name__ == '__main__':
    main()