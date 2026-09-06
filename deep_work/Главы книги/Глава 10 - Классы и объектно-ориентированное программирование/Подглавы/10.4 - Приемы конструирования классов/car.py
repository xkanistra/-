# Класс Car
class Car:
        # Инициализировать объекта класса
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    # Задать изготовителя
    def set_make(self, make):
        self.__make = make

    # Задать адресс
    def set_model(self, model):
        self.__model = model

    # Задать номер телефона
    def set_year(self, year):
        self.__year = year

    # Вернуть изготовителя
    def get_make(self):
        return self.__make

    # Вернуть модель
    def get_model(self):
        return self.__model

    # Вернуть год изготовления
    def get_year(self):
        return self.__year