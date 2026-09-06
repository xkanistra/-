# Константа для вставки налога с продаж
TAX_RATE = 0.05

# Класс ServiceQuote
class ServiceQuote:
    # Инициализировать объекта класса
    def __init__(self, pcharges, lcharges):
        self.__parts_charges = pcharges
        self.__labor_charges = lcharges

    # Задать оценочную стоимость запчастей
    def set_parts_charges(self, pcharges):
        self.__parts_charges = pcharges

    # Задать оценочную стоимость трудозатрат
    def set_labor_charges(self, lcharges):
        self.__labor_charges = lcharges

    # Задать оценочную стоимость запчастей
    def get_parts_charges(self):
        return self.__parts_charges

    # Получить оценочную стоимость трудозатрат
    def get_labor_charges(self):
        return self.__labor_charges

    # Получить налог с продаж
    def get_sales_tax(self):
        return self.__parts_charges * TAX_RATE

    # Получить оценочная стоимость расходов
    def get_total_charges(self):
        return self.__parts_charges + self.__labor_charges + (self.__parts_charges * TAX_RATE)

    