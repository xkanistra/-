# Программа выводит диаграмму расходов
import matplotlib.pyplot as plt
DATA_FILE = 'Главы книги/Глава 7 - Списки и кортежи/Упражнения по программированию/Условия для задач/Мои расходы.txt'
COST_CATEGORY = ('За квартиру', 'Проезд', 'Продукты', 'Одежда', 'Связь и интернет', 'Бытовые расходы')

def main():
    cost_list = []
    cost_list = add_list()
    slice_labels = COST_CATEGORY
    color = ['r', 'g', 'b', 'm', 'k', 'y']
    plt.pie(cost_list, labels = slice_labels, colors=color)
    plt.title('Расходы по категориям за апрель - май')
    plt.show()

def add_list():
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        cost = file.readlines()
    index = 0
    while index < len(cost):
        cost[index] = float(cost[index])
        index += 1
    return cost

 
if __name__ == '__main__':
    main()