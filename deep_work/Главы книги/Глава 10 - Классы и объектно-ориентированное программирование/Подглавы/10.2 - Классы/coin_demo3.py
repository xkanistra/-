# Программа демонстрирует импорт модуля coin
# и создает экземпляр класса Coin

import coin

def main():
    # Создать объект на основе класса Coin
    my_coin = coin.Coin()

    # Показать обращенную вверх сторону монеты
    print('Эта сторона обращена вверх:', my_coin.get_sideup())

    # Подбросить монету
    print('Подбрасываю монету десять раз...')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

if __name__ == '__main__':
    main()