# Класс CashRegister

class CashRegister:
    def __init__(self):
        self.__retailitem_list = []

    def purchase_item(self, item):
        self.__retailitem_list.append(item)

    def get_total(self):
        total_price = 0
        for item in self.__retailitem_list:
            total_price += item.get_price()
        return total_price
    
    def show_items(self):
        num_item = 0
        for item in self.__retailitem_list:
            num_item += 1
            print(f'Товар №{num_item}. {item.get_description()} - {item.get_price()}')
            

    def clear(self):
        self.__retailitem_list.clear()