# Класс Car
import logging

logger = logging.getLogger(__name__)

class Car:
    # Инициализация атрибутов класса
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # Метод присваивает модель автомобиля
    def set_year_model(self, year_model):
        self.__year_model = year_model

    # Метод присваивает фирму-изготовителя автомобиля
    def set_make(self, make):
        self.__make = make

    # Метод увеличивает скорость автомобиля
    def accelerate(self):
        self.__speed += 5

    # Метод уменьшает скорость автомобиля
    def brake(self):
        self.__speed -= 5   

    # Метод показывает текущую скорость автомобиля
    def get_speed(self):
        return f'Текущая скорость автомобиля: {self.__speed}'