# Программа показывает график цен на бензин по неделям
import matplotlib.pyplot as plt
DATA_FILE = 'Главы книги/Глава 7 - Списки и кортежи/Упражнения по программированию/Условия для задач/1994_Weekly_Gas_Averages.txt'

def main():
    price_list = []
    price_list, week_list = add_list()
    graph = price_graph(price_list, week_list)

def add_list():
    week_list = []
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        price = file.readlines()
    index = 0
    total_week = 0
    while index < len(price):
        price[index] = float(price[index].rstrip('\n'))
        total_week += 1
        index += 1
        week_list.append(total_week)
    return price, week_list    

def price_graph(price, week):
    x_coords = week
    y_coords = price

    plt.plot(x_coords, y_coords, color = 'r')

    plt.title('График цен на бензин за 1994 год')
    plt.xlabel('Недели')
    plt.ylabel('Цена за 1 литр')
    plt.grid(True)
    plt.show()
    
if __name__ == '__main__':
    main()