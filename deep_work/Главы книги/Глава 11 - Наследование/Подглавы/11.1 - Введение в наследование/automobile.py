# Класс Automobile содержит общие данные
# об автомобилях на складе


class Automobile:
    # __init__ принимает аргументы для
    # фирмы-изготовителя, модели, пробега и цены.
    # Он инициализирует атрибуты этих значений

    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    # Создание методов которые являются мутаторами
    # атрибутов этого класса

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    # Создание методов которые получателями
    # атрибутов этого класса.

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price


# Класс Car представляет легковой автомобиль.
# Он является подклассом класса Automobile.


class Car(Automobile):
    # __init__ принимает аргументы для
    # фирмы-изготовителя, модели, пробега и цены.
    # Он инициализирует атрибуты этих значений

    def __init__(self, make, model, mileage, price, doors):
        # Вызываем метод __init__ надкласса и передаем
        # требуемые аргументы. Так же мы передаем self в
        # качестве аргумента.
        Automobile.__init__(self, make, model, mileage, price)
        self.__doors = doors

    # Метод является методом-мутатором атрибута __doors
    def set_doors(self, doors):
        self.__doors = doors

    # Метод является методом-получателем атрибута __doors
    def get_doors(self):
        return self.__doors


# Класс Truck представляет легковой автомобиль.
# Он является подклассом класса Automobile.


class Truck(Automobile):
    # __init__ принимает аргументы для
    # фирмы-изготовителя, модели, пробега и цены.
    # Он инициализирует атрибуты этих значений

    def __init__(self, make, model, mileage, price, drive_type):
        # Вызываем метод __init__ надкласса и передаем
        # требуемые аргументы. Так же мы передаем self в
        # качестве аргумента.
        Automobile.__init__(self, make, model, mileage, price)
        self.__drive_type = drive_type

    # Метод является методом-мутатором атрибута __drive_type
    def set_doors(self, drive_type):
        self.__drive_type = drive_type

    # Метод является методом-получателем атрибута __drive_type
    def get_drive_type(self):
        return self.__drive_type


# Класс SUV представляет легковой автомобиль.
# Он является подклассом класса Automobile.


class SUV(Automobile):
    # __init__ принимает аргументы для
    # фирмы-изготовителя, модели, пробега и цены.
    # Он инициализирует атрибуты этих значений

    def __init__(self, make, model, mileage, price, pass_cap):
        # Вызываем метод __init__ надкласса и передаем
        # требуемые аргументы. Так же мы передаем self в
        # качестве аргумента.
        Automobile.__init__(self, make, model, mileage, price)
        self.__pass_cap = pass_cap

    # Метод является методом-мутатором атрибута __pass_cap
    def set_doors(self, pass_cap):
        self.__pass_cap = pass_cap

    # Метод является методом-получателем атрибута __pass_cap
    def get_pass_cap(self):
        return self.__pass_cap
