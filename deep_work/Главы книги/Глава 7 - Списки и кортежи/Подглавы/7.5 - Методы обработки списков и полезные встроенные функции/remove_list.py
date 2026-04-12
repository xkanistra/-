# Программа демонстрирует применение метода
# remove для удаления значения из списка

def main():
    again = 'Д'
    while again == 'д' or again == 'Д':
            
        # Создать список 
        food = ['Бургеры', 'Пицца', 'Чипсы']

        # Показать список
        print('Список продуктов')
        print(food)

        # Значение подлежащее изменению
        item = input('Какое значение следует изменить? ')

        try:
            # Удалить значения
            food.remove(item)

            # Показать список 
            print('Измененный список')
            print(food)
            again = input('Желаете изменить список еще?(Д/д - да): ')
            if again == 'д' or again == 'Д':
                again = 'д'
            else:
                break

        except ValueError:
            print('Это значение не найдено')
            again = input('Желаете повторить? (Д/д - да): ')
            if again == 'д' or again == 'Д':
                again = 'д'
            else:
                break
            
if __name__ == '__main__':
    main()