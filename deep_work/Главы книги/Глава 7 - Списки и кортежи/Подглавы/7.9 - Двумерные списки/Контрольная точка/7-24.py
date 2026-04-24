# Написать набор вложенных циклов которые выводят на экран содержимое списка чисел
import random
ROW = 3
COLS = 4
def main():
    points =[[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
    
    for r in range(ROW):
        for c in range(COLS):
            points[r][c] = random.randint(1, 100)

    print(points)

if __name__ == '__main__':
    main()