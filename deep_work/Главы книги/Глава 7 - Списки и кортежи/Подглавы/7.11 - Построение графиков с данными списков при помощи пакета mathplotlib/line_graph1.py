# Программа выводит простой линейный график
import matplotlib.pyplot as plt

def main():
    # Списки координат
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Построене графика
    plt.plot(x_coords, y_coords)

    # Показать график
    plt.show()

if __name__ == '__main__':
    main()

