# Программа получает данные о авто, ускоряет, тормозит и показывает текущую скорость авто

import car
import logging

LOGGER_FILE = 'Главы книги/Глава 10 - Классы и объектно-ориентированное программирование/Упражнения по программированию/№2 - Класс Car/app.log'

def main(): 
    year = int(input('Введите год выспука авто: '))
    make = input('Введите марку авто: ')

    car_inf = car.Car(year, make)

    for _ in range(5):
        car_inf.accelerate()
    print(car_inf.get_speed())

    for _ in range(5):
        car_inf.brake()
    print(car_inf.get_speed())

if __name__ == '__main__':
    main()