# Программа выводит простой линейный график с сеткой, заголовком
# и меткой осей
import matplotlib.pyplot as plt

def main():
    # Списки координат
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Построене графика
    plt.plot(x_coords, y_coords)

    # Добавить заголовок
    plt.title('Образец данных')

    # Добавить описане меток
    plt.xlabel('Это ось Х')
    plt.ylabel('Это ось Y')

    # Добавить сетку
    plt.grid(True)

    # Показать график
    plt.show()

if __name__ == '__main__':
    main()

