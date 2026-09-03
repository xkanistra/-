# Программа расконсервирует объекты CellPhone
import pickle
import cellphone

# Константа для имени файла
FILENAME = 'Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Подглавы/10.3 - Работа с экземплярами/В ЦЕНТРЕ ВНИМАНИЯ/cellphones.dat'

def main():
    # Переменная для управления циклом
    end_of_file = False

    # Открыть файл
    with open(FILENAME, 'rb') as input_file:

        # Прочесть файл до конца
        while not end_of_file:
            try:
                # Расконсервировать следующий объект
                phone = pickle.load(input_file)

                # Показать данные о телефоне
                display_data(phone)
            except EOFError:
                # Установить флаг, для обозначения, что
                # был достигнут конец файла
                end_of_file = True

# Функция показывает данные из объекта Cellphone
def display_data(phone):
    print(f'Производитель: {phone.get_manufact()}')
    print(f'Номер модели: {phone.get_model()}')
    print(f'Розничная цена: {phone.get_retail_price():,.2f}')
    print()
    
if __name__ == '__main__':
    main()