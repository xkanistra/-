# Вывод простой круговой диаграммы

import matplotlib.pyplot as plt


def main():
    # Создать список
    value = [100, 400, 300, 600]

    slice_labels = ["I квартал", "II квартал", "III квартал", "IV квартал"]

    plt.pie(value, labels=slice_labels)

    plt.title("Продажи с разбивкой по кварталам")

    plt.show()


if __name__ == "__main__":
    main()
