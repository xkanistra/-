# Программа расчитывает стоимость малярных работ исходя из:
# стоимости краски, часов работ, работы, кол-ва краски

# Константы при пересчете на 1 м^2 покраски
HOUR = 0.8
PAINT = 0.5

# Стоимость 1 часа работы
PRICE = 2000


def main():
    meter = int(input("Введите площадь поверхности: "))
    paint_price = float(input("Введите стоимость 5 л банки краски: "))

    # Кол-во банок краски
    amount_paint = get_amount_paint(meter)

    # Кол-во потраченных на работу часов
    amount_hour = get_amount_hour(meter)

    # Cтоимость краски
    price_can_paint = get_price_can_paint(amount_paint, paint_price)

    # Стоимость работы
    work_price = get_work_price(amount_hour)

    # Общая стоимость работ
    total_price = get_total_price(price_can_paint, work_price)

    print(f"Кол-во требуемых емкостей с краской: {amount_paint:.0f}")
    print(f"Кол-во потраченных на работу часов: {amount_hour:.0f}")
    print(f"Cтоимость краски: {price_can_paint:,.2f} рублей")
    print(f"Стоимость работы: {work_price:,.2f} рублей")
    print(f"Общая стоимость работ: {total_price:,.2f} рублей")


# Расчет кол-ва банок с краской
def get_amount_paint(meter):
    result = meter * PAINT
    return result


# Расчет потраченных на работу часов
def get_amount_hour(meter):
    result = meter * HOUR
    return result


# Расчет стоимости краски
def get_price_can_paint(amount_paint, paint_price):
    result = amount_paint * paint_price
    return result


# Расчет стоимости работ
def get_work_price(amount_hour):
    result = amount_hour * PRICE
    return result


# Расчет общей стоимости работ
def get_total_price(price_can_paint, work_price):
    result = price_can_paint + work_price
    return result


main()
