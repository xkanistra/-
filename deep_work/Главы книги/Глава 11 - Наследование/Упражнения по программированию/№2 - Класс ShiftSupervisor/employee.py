# Класс Employee


class Employee:
    # Инициализируем атрибуты класса
    def __init__(self, name, id_num):
        self.__name = name
        self.__id_num = id_num

    # Присваиваем имя
    def set_name(self, name):
        self.__name = name

    # Присваиваем идентификационный номер
    def set_id_num(self, id_num):
        self.__id_num = id_num

    # Вернуть имя
    def get_name(self):
        return self.__name

    # Вернуть идентификационный номер
    def get_id_num(self):
        return self.__id_num


# Подкласс ProductionWorker
class ProductionWorker(Employee):
    # Инициализируем атрибуты подкласса
    def __init__(self, name, id_num, shift_num, h_rate):
        Employee.__init__(self, name, id_num)
        self.__shift_num = shift_num
        self.__h_rate = h_rate

    # Получить номер смены
    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num

    # Получить почасовую ставку
    def set_h_rate(self, h_rate):
        self.__h_rate = h_rate

    # Вернуть номер смены
    def get_shift_num(self):
        if self.__shift_num == 1:
            return f"дневная"
        else:
            return f"ночная"

    # Вернуть почасовую ставку
    def get_h_rate(self):
        return self.__h_rate


# Подкласс ShiftSupervisor
class ShiftSupervisor(Employee):
    def __init__(self, name, id_num, annual_salary, annual_bonus):
        Employee.__init__(self, name, id_num)
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus

    # Получить годовой оклад
    def set_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    # Получить годовую премию
    def set_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus

    # Вернуть годовой оклад
    def get_salary(self):
        return self.__annual_salary

    # Вернуть годовую премию
    def get_bonus(self):
        return self.__annual_bonus
