# Программа считывает чиловые знач из файла в список

def main():
    # Открыть файл
    with open('numberlist.txt', 'r', encoding='utf-8') as file:
        # Прочитать список
        numbers = file.readlines()

    # Конвентрировать из str в int
    index = 0
    while index < len(numbers):
        numbers[index] = int(numbers[index])
        index += 1

    print(numbers)
if __name__ == '__main__':
    main()