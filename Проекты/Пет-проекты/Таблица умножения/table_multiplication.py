# Программа генерирует таблицу умножения с выбором ее размера

day = int(input("Введите размер таблицы: "))

for r in range(1, day + 1):
    print(r, end=" ")
    for c in range(1, day + 1):
        total = r * c
        print(total, end=" ")
    print()
