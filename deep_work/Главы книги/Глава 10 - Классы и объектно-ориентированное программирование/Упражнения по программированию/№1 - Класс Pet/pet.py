# Класс Pet

class Pet:
    # Инициализация атрибутов класса
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # Метод присваивает имя питомца
    def set_name(self, name):
        self.__name = name

    # Метод присваивает тип питомца
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # Метод присваивает возвраст
    def set_age(self, age):
        self.__age = age

    # Метод возвращает имя питомца
    def get_name(self):
        return self.__name

    # Метод возвращает тип питомца
    def get_animal_type(self):
        return self.__animal_type

    # Метод возвращает возвраст питомца
    def get_age(self):
        return self.__age
    