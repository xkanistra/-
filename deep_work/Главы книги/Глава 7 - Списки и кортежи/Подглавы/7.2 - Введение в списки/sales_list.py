# Константа NUM_DAYS содержит кол-во дней, 
# за которые мы соберем данные

NUM_DAYS = 5

def main():
    # Создать список содержащий продажи за каждый день
    sales = [0] * NUM_DAYS

    print('Введите продажи за каждый день')

    # Получить продажи за каждый день
    for index in range(len(sales)):
        sales[index] = float(input(f'День № {index + 1}: '))

    # Показать введенные значения
    print('Вот значения, которые были введены: ')
    for value in sales:
        print(value)

if __name__ == '__main__':
    main()