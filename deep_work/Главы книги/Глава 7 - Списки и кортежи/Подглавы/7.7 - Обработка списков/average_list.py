# Программа вычисляет среднее арифметическое
# значение в списке значений

def main():
    # Список 
    scores = [2.5, 7.3, 6.5, 4.0, 5.2]

    # Накопитель
    total = 0.0

    # Вычисление суммы
    for value in scores:
        total += value

    # Среднее арифм
    average = total / len(scores)

    print(f'Среднее арифметическое: {average}')

if __name__ == '__main__':
    main()