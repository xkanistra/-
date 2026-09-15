# Класс Employee

class Employee:
    # Инициализируем атрибуты класса
    def __init__(self, name, id_num, department, position):
        self.__name = name
        self.__id_num = id_num
        self.__department = department
        self.__position = position

    # Присваиваем имя
    def set_name(self, name):
        self.__name = name

    # Присваиваем идентификационный номер
    def set_id_num(self, id_num):
        self.__id_num = id_num

    # Присваиваем отдел
    def set_position(self, position):
        self.__position = position

    # Присваиваем должность
    def set_department(self, department):
        self.__department = department

    def __str__(self):
        return f'Введённые вами данные\nИмя: {self.__name}\nИденцификационный номер: {self.__id_num}\nОтдел: {self.__department}\nНомер телефона: {self.__position}\n'

    def inf_list(self):
        information_list = []
        information_list.append(self.__name)
        information_list.append(self.__id_num)
        information_list.append(self.__department)
        information_list.append(self.__position)
        return ', '.join(information_list)