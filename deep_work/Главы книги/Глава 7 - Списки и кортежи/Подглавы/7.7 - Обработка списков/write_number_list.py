# Демонстрация сохранения списка с числами в файл

def main():
    # Список
    numbers = [1, 2, 3, 4, 5, 6, 7]

    # Открыть файл
    with open('numberlist.txt', 'w', encoding='utf-8') as file:

        # Записать список в файл
        for item in numbers:
            file.write(f'{item}\n')

if __name__ == '__main__':
    main()