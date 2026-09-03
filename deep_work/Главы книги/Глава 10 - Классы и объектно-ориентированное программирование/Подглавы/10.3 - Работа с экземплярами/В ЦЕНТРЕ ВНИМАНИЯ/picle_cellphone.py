# Программа консервирует объекты CellPhone
import pickle
import cellphone

# Константа для имени файла
FILENAME = 'Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Подглавы/10.3 - Работа с экземплярами/В ЦЕНТРЕ ВНИМАНИЯ/cellphones.dat'

def main():
    # Переменная для управления циклом
    again = 'д'

    # Открыть файл
    with open(FILENAME, 'wb') as output_file:

        # Получить данные от пользователя
        while again.lower() == 'д':
            # Получить данные о телефоне
            man = input('Введите производителя: ')
            mod = input('Введите номер модели: ')   
            retail = float(input('Введите розничную цену: '))

            # Создать объект CellPhone
            phone = cellphone.CellPhone(man, mod, retail)

            # Законсервировать объект и записать в файл
            pickle.dump(phone, output_file)

            # Получить еще один элемент?
            again = input('Введете еще один элемент данные? (д/н): ')

if __name__ == '__main__':
    main()