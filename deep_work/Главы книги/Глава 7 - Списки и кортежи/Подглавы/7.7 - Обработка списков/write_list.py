# Демонстрация сохранения списка в файл

def main():
    # Список
    cities = ['Нью-Йорк', 'Бостон', 'Атланта', 'Даллас']

    # Создать файл
    with open('cities.txt', 'w', encoding='utf-8') as file:
        # Записать список в файл
        for item in cities:
            file.write(item + '\n')

if __name__ == '__main__':
    main()