# Вывод простой круговой диаграммы

import matplotlib.pyplot as plt

def main():
    # Создать список
    value = [20, 60, 80, 40]

    plt.pie(value)
    plt.show()

if __name__ == '__main__':
    main()