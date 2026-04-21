# Демонстрация считывания содержимого файла в список

def main():
    # Открыть файл
    with open('cities.txt', 'r', encoding='utf-8') as file:
        # Прочитать содержимое
        cities = file.readlines()

    # Удалить \n из каждого элемента
    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1

    print(cities)

if __name__ == '__main__':
    main()