# Программа демонстрирует передачу объекта Coin
# в качестве аргумента в функцию
import coin

def main():
    # Создание объекта Coin
    my_coin = coin.Coin()

    # Функция покажет сторону которая сейчас
    print(my_coin.get_sideup())

    # Перадача объекта в функцию
    flip(my_coin)

    # Инструкция показывает либо Орел
    # либо Решка
    print(my_coin.get_sideup())

# Функция flip подбрасывет монету
def flip(coin_obj):
    coin_obj.toss()

if __name__ == '__main__':
    main()
    