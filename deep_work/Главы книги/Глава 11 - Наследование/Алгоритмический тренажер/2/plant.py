class Plant:
    def __init__(self, plant_type):
        self.__plant_type = plant_type

    def message(self):
        print("Я - планета")


class Tree(Plant):
    def __init__(self):
        Plant.__init__("дерево")

    def message(self):
        print("Я - дерево")
