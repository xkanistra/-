# Класс Customer
class Customer:
    # Инициализировать объекта класса
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    # Задать имя
    def set_name(self, name):
        self.__name = name

    # Задать адресс
    def set_address(self, address):
        self.__address = address

    # Задать номер телефона
    def set_phone(self, phone):
        self.__phone = phone

    # Вернуть имя
    def get_name(self):
        return self.__name

    # Вернуть адресс
    def get_address(self):
        return self.__address

    # Вернуть номер телефона
    def get_phone(self):
        return self.__phone
    