# Программа демонстрирует как оператор in
# применяется к списку

def main():
    again = 'Д'
    while again == 'Д' or again == 'д':
        # Создать список нумеров изделия
        prod_nums = ['V475', 'F987', 'Q143', 'R688']

        # Получить искомый номер изделия
        search = input('Введите номер изделия: ')

        # Определить что номер есть в списке
        if search in prod_nums:
            print(f'{search} найден в списке')
            again = input('Желаете продолжить поиск?(Введите д/Д): ')
            if again == 'Д' or again == 'д':
                again = 'д'
            else: 
                break
        else:
            print(f'{search} не найден в списке')
            again = input('Желаете повторить поиск?(Введите д/Д): ')
            if again == 'Д' or again == 'д':
                again = 'д'
            else: 
                break

if __name__ == '__main__':
    main()