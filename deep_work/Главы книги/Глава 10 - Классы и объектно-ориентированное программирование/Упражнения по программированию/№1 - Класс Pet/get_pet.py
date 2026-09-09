# Программа получает данные о домашних животных


# Импорт логгера и класса Pet
import logging
import pet
LOGGER_FILE = 'Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Упражнения по программированию/№1 - Класс Pet/app.log'


# Настройка логгера
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s -> %(message)s',
    filename=LOGGER_FILE,
    filemode='a' 
)


def main():
    # Переменная для работы цикла
    again = 'д'

    # Логгер для отслеживания действий и работы программы
    logging.debug('Программа запущенна')
    logging.debug('Пользователь вводит даные...\n')

    # Запуск цикла
    while again.lower() == 'д':
        try:
            # Ввести данные о домашнем животном
            name = input('Введите имя домашнего животного: ')
            animal_type = input('Введите вид домашнего животного(собака, кот и т.п): ')
            age = int(input('Введите возраст животного: '))
            while age <= 0:
                age = int(input('Введите корректный возраст животного: '))
            logging.debug('Пользователь успешно ввел данные!\n')
        

            logging.debug('Создание объекта на основе класса Pet...')
            pet_information = pet.Pet(name, animal_type, age)

            logging.debug('Вывод введенных данных пользователем...\n')
            print(f'Имя вашего питомца: {pet_information.get_name()}')
            print(f'Тип вашего питомца: {pet_information.get_animal_type()}')
            if age > 4:
                print(f'Возраст вашего питомца: {pet_information.get_age()} лет')
            elif 2 <= age <= 4:
                print(f'Возраст вашего питомца: {pet_information.get_age()} года')
            else:
                print(f'Возраст вашего питомца: {pet_information.get_age()} год\n')

            again = input('Желаете продолжить?(д/н): ')

        except ValueError:
            logging.error('!ПОЛЬЗОВАТЕЛЬ ВВЕЛ НЕКОРЕКТНЫЕ ДАННЫЕ!')
            print('Введите возраст животного как число.')


if __name__ == '__main__':
    main()

