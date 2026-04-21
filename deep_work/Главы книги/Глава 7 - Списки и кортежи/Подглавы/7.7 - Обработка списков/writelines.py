# Демонстрация метода writelines

def main():
    # Список 
    cities = ['Нью-Йорк', 'Бостон', 'Атланта', 'Даллас']

    # Открытие файла для записи
    with open('cities.txt', 'w', encoding='utf-8') as file:
        # Записать список в файл
        file.writelines(cities)

if __name__ == '__main__':
    main()