# Программа вычисляет зп до удержаний (Обрабатывает исключение ValueError)

def main():
    try:
        # Получить часы
        hours = int(input('Введите кол-во отработанных часов: '))

        # Почасовая ставка
        pay_rate = float(input('Введите вашу почасовую ставку: '))

        # Вычислить зп
        gross_pay = hours * pay_rate

        # Показать зп
        print(f'ЗП: ${gross_pay:.2f}')
    
    except ValueError as err:
        print(err)

if __name__ == '__main__':
    main()