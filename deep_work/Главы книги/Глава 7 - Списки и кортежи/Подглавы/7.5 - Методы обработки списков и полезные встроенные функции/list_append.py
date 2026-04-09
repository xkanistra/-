# Демонстрация применения метода append
# для добавления значения в список

def main():
    # Создать пустой список
    name_list = []

    # Переменная для управ циклом  
    again = 'д'

    # Добавление в список имен через цикл
    while again == 'д' or again == 'Д':
        # Получаем имя пользователя
        name = input('Введите имя: ')

        # Добавить имя в конец списка
        name_list.append(name)

        # Добавить еще одно?
        again = input('Желаете добавить еще имя?(Введите д/Д): ')
        if again == 'Д' or again == 'д':
            again = 'д'
            print()
        else: 
            print()
            break

    # Показать введенные имена
    print('Введенные имена')

    for name in name_list:
        print(name)

if __name__ == '__main__':
    main()
