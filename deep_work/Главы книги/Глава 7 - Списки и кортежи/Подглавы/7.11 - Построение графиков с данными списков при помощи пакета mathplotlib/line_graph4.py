import matplotlib.pyplot as plt

def main():
    # Списки координат
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Построене графика
    plt.plot(x_coords, y_coords)

    # Добавить заголовок
    plt.title('Продажи с разбивкой на года')

    # Добавить описание меток
    plt.xlabel('Год')
    plt.ylabel('Объем продаж')

    # Настроить метки деления
    plt.xticks([0, 1, 2, 3, 4], 
               ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 1, 2, 3, 4 ,5],
               ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
    
    # Добавить сетку
    plt.grid(True)

    # Показать график
    plt.show()

if __name__ == '__main__':
    main()