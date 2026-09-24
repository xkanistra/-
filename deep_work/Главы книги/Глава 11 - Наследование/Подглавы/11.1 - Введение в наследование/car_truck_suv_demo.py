# Программа создает объекты Car, Truck, SUV

import automobile


def main():
    # Создаем объект Car для авто BMW 2001 года
    # с 70000 милями пробега, ценой 15000.00$ и 4 дверьми
    car = automobile.Car("BMW", 2001, 70000, 15000.00, 4)

    # Создаем объект Truck для авто Toyota 2002 года
    # с 40000 милями пробега, ценой 1200.00$ и полным приводом
    truck = automobile.Truck("Toyota", 2002, 40000, 12000.00, "4WD")

    # Создаем объект SUV для авто Volvo 2000 года
    # с 30000 милями пробега, ценой 18500.00$ и вместимостью 5 человек
    suv = automobile.SUV("Volvo", 2000, 30000, 18500.00, 5)

    print("ПОДЕРЖАННЫЕ АВТО НА СКЛАДЕ")
    print("==========================")

    # Показать данные легковое авто
    print("Данный легковой автомобиль имеется на складе.")
    print(f"Изготовитель: {car.get_make()}")
    print(f"Модель: {car.get_model()}")
    print(f"Пробег: {car.get_mileage()}")
    print(f"Цена: {car.get_price()}")
    print(f"Количество дверей: {car.get_doors()}\n")

    # Показать данные пикапа
    print("Данный легковой автомобиль имеется на складе.")
    print(f"Изготовитель: {truck.get_make()}")
    print(f"Модель: {truck.get_model()}")
    print(f"Пробег: {truck.get_mileage()}")
    print(f"Цена: {truck.get_price()}")
    print(f"Тип привода: {truck.get_drive_type()}\n")

    # Показать данные джипа
    print("Данный легковой автомобиль имеется на складе.")
    print(f"Изготовитель: {suv.get_make()}")
    print(f"Модель: {suv.get_model()}")
    print(f"Пробег: {suv.get_mileage()}")
    print(f"Цена: {suv.get_price()}")
    print(f"Пассажирская вместимость: {suv.get_pass_cap()}\n")


if __name__ == "__main__":
    main()
