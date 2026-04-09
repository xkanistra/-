# Демонстрация метода insert

def main():
    again = 'д'
    # Список имен
    names = ['Джеймс', 'Кэтрин', 'Билл']

    # Показать список
    print('Вот список имен')
    print(names)

    # Вставить новое имя в нужный элемент
    while again == 'Д' or again == 'д':
        try:
            index = int(input('Выберите нужное имя в списке введя 1 - 3: '))
            new_names = input('Введите имя на которое хотите заменить: ')
            names.insert(index - 1, new_names)
            # Показать обновленный списко
            print('Обновленный список:')
            print(names)
            
            again = input('Желаете изменить еще имя?(Введите д/Д): ')
            if again == 'Д' or again == 'д':
                again = 'д'
            else: 
                break
        except ValueError:
            again = input('Вы ввели неверное значение, попробуйте снова(Введите д/Д): ')
            if again == 'Д' or again == 'д':
                again = 'д'
            else: 
                break
        
    # Показать обновленный списко
    print('Обновленный список:')
    print(names)

if __name__ == '__main__':
    main()