BURGER = "Изысканные бургеры от Джо"  # нет нет нет
PIZZA = "Центральная пиццерия"  # да нет да
CAFE = "Кафе за углом"  # да да да
MAMA = "Блюдо от итальянской мамы"  # да нет нет
SHEF = "Кухня шеф-повара"  # да да да

vegetarian = input("Будет ли на ужине вегатерианец? ")
vegan = input("Будет ли на ужине веган? ")
gluten = input("Будет ли на ужине cторонник безглютеновой диеты? ")

if vegetarian == 'Нет' or vegetarian == 'нет' and vegan == 'Нет' or vegan == 'нет' and gluten == 'Нет' or gluten == 'нет':
    print('Вот ваш вариант ресторанов: ')
    print(BURGER)

elif vegetarian == 'Да' or vegetarian == 'да' and vegan == 'Нет' or vegan == 'нет' and gluten == 'Да' or gluten == 'да':
    print('Вот ваш вариант ресторанов: ')
    print(PIZZA)

elif vegetarian == 'Да' or vegetarian == 'да' and vegan == 'Да' or vegan == 'да' and gluten == 'Да' or gluten == 'да':
    print('Вот ваш вариант ресторанов: ')
    print(CAFE)
    print(SHEF)

elif vegetarian == 'Да' or vegetarian == 'да' and vegan == 'Нет' or vegan == 'нет' and gluten == 'Нет' or gluten == 'нет':
    print('Вот ваш вариант ресторанов: ')
    print(MAMA)