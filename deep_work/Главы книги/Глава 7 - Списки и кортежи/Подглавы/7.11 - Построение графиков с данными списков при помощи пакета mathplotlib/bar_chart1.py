# Выводит гистограмму

import matplotlib.pyplot as plt

def main():
    # Список с координатами Х левого края
    left_edges = [0, 10, 20, 30, 40]

    # Список Y высоты 
    heights =[100, 200, 300, 400, 500]

    # Построить гистограмму
    plt.bar(left_edges, heights)

    plt.show()

if __name__ == '__main__':
    main()