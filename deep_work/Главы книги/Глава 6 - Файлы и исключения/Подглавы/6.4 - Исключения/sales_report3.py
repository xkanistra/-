# Программа показывает итоговый объем продаж 
# из файла sales_data.txt

def main():
    total = 0.0

    try:
        # Открываем файл sales_data.txt 
        infile = open('sales_data.txt', 'r')

        # Читаем значения из файлов 
        # и накапливаем их
        for line in infile:
            amount = float(line)
            total += amount

        # Закрыть файл
        infile.close()

        # Печать итога
        print(f'{total:.2f}')
    except Exception as err:
        print(err)

if __name__ == '__main__':
    main()