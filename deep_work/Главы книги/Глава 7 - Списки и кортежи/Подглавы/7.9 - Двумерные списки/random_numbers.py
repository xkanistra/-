# Демонстрация присваивания случ числа двумерному списку
import random

# Константы строк и столбцов
ROW = 3
COLS = 4
def main():
    # Список
    value = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    
    # Заполнить списки случайными числами
    for r in range(ROW):
        for c in range(COLS):
            value[r][c] = random.randint(1, 100)

    print(value)

if __name__ == '__main__':
    main()
             