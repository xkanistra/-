# Вывод простой круговой диаграммы

import matplotlib.pyplot as plt


def main():
    # Создать список
    value = [20, 60, 80, 40]

    slice_labels = ["I квартал", "II квартал", "III квартал", "IV квартал"]

    plt.pie(value, labels=slice_labels)

    plt.title("Продажи с разбивкой по кварталам")

    plt.show()


if __name__ == "__main__":
    main()
