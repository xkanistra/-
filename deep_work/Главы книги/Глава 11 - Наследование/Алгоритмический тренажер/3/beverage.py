class Beverage:
    def __init__(self, bev_name):
        self.__bev_name = bev_name

    def message(self):
        print(f'Я - {self.__bev_name}')
class Cola(Beverage):
    def __init__(self, bev_name):
        Beverage.__init__(self, 'кока-кола')

    def message(self):
        print('Я - кока-кола')