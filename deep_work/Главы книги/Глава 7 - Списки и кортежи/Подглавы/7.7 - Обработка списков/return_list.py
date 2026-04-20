# Программа применяет функцию для создания списка
# Указанная функция возвращает ссылку на список

def main():
    # Получить ссылку на список
    numbers = get_values()

    # Показать значения в списке
    print(f'Числа в списке\n{numbers}')

# Функция get_values() получает от пользователя значения и сохраняет
# их в списке
def get_values():
    # Создать пустой список
    values = []

    again = 'д'

    while again == 'д' or again == 'Д':
        num = int(input('Введите число: '))
        values.append(num)

        again = input('Желаете изменить еще имя?(Введите д/Д): ')
        print()

    return values

if __name__ == '__main__':
    main()