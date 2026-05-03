ROWS = 5        # Строка
COLS = 3        # Столбец

numbers = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

for r in range(ROWS):
    for c in range(COLS):
        numbers[r][c] = int(input(f'Введите значенение: '))
print(numbers)