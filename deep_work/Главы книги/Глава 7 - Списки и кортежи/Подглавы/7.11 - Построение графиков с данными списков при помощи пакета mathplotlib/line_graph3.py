import matplotlib.pyplot as plt

def main():
    # Списки координат
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Построене графика
    plt.plot(x_coords, y_coords)

    # Добавить заголовок
    plt.title('Образец данных')

    # Задать границы осей
    plt.xlim(xmin = -1, xmax = 10)
    plt.ylim(ymin = -1, ymax = 10)
    # Добавить описане меток
    plt.xlabel('Это ось Х')
    plt.ylabel('Это ось Y')

    # Добавить сетку
    plt.grid(True)

    # Показать график
    plt.show()

if __name__ == '__main__':
    main()
