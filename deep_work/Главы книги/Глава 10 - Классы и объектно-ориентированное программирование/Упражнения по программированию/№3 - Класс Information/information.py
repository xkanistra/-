# Класс Information

class Information:
    # Инициализируем атрибуты класса
    def __init__(self, name, age, adress, mobile_number):
        self.__name = name
        self.__age = age
        self.__adress = adress
        self.__mobile_number = mobile_number

    # Присваиваем имя
    def set_name(self, name):
        self.__name = name

    # Присваиваем возраст
    def set_age(self, age):
        self.__age = age

    # Присваиваем номер телефона
    def set_mobile_number(self, mobile_number):
        self.__mobile_number = mobile_number

    # Присваиваем адрес
    def set_adress(self, adress):
        self.__adress = adress

    def __str__(self):
        return f'Введённые вами данные\nИмя: {self.__name}\nВозраст: {self.__age}\nАдрес: {self.__adress}\nНомер телефона: {self.__mobile_number}'

    def inf_list(self):
        information_list = []
        information_list.append(self.__name)
        information_list.append(self.__age)
        information_list.append(self.__adress)
        information_list.append(self.__mobile_number)
        return ', '.join(information_list)