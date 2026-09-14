# Класс Procedure

class Procedure:
    def __init__(self, procedure, date, medic, cost):
        self.__procedure = procedure
        self.__date = date
        self.__medic = medic
        self.__cost = cost

    def set_procedure(self, procedure):
        self.__procedure = procedure

    def set_date(self, date):
        self.__date = date

    def set_medic(self, medic):
        self.__medic = medic

    def set_cost(self, cost):
        self.__cost = cost

    def __str__(self):
        return f'Название процедуры: {self.__procedure}\nДата: {self.__date}\nВрач: {self.__medic}\nСтоимость: {self.__cost:,.2f}\n'

    def inf_list(self):
        information_list = []
        information_list.append(self.__procedure)
        information_list.append(self.__date)
        information_list.append(self.__medic)
        information_list.append(str(self.__cost))
        return ', '.join(information_list)