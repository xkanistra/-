# Программа расчитывает стоимость страховки

BELAY = 0.8

def main():
    price = float(input('Введите стоимость вашей недвижимости: '))
    total_belay = get_belay(price)
    print(f'Рекомендованная минимальная страховая сумма: {total_belay:.2f} $')

def get_belay(price):
    recomended_belay = price * BELAY
    return recomended_belay

main()