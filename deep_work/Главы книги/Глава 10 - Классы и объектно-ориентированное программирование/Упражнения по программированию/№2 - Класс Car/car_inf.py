# Программа получает данные о авто, ускоряет, тормозит и показывает текущую скорость авто

import car
import logging

LOGGER_FILE = 'Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Упражнения по программированию/№2 - Класс Car/app.log'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s -> %(message)s',
    filename=LOGGER_FILE,
    filemode='a' 
)

def main(): 
    try:
        logging.debug('Начало программы. Сбро данных')
        year = int(input('Введите год выспука авто: '))
        make = input('Введите марку авто: ')

        logging.debug('Данные переданы в класс. Создание объекта класса.')
        car_inf = car.Car(year, make)

        logging.info('Расчет разгона и торможения.')
        for _ in range(5):
            car_inf.accelerate()
        print(car_inf.get_speed())

        for _ in range(5):
            car_inf.brake()
        print(car_inf.get_speed())

    except ValueError:
        logging.error(f'Пользователь ввел недопустимый форма ввода')
        print('Введите допустимое значение в формате целого числа.')

if __name__ == '__main__':
    main()