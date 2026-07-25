# Программа читает результат контрольных работ из
# файла CSV и вычисляет средний балл для каждого ученика

CSV_FILE = 'Главы книги/Глава 8 - Подробнее о строковых данных/Подглавы/8.3 - Проверка, поиск и манипуляция строковыми данными/В ЦЕНТРЕ ВНИМАНИЯ 3/test_score.csv'
def main():
    # Открыть файл
    with open(CSV_FILE, 'r', encoding='utf-8') as csv_file:
        lines = csv_file.readlines()

    for line in lines:
        # Получить результаты контрольных
        tokens = line.split(',')

        # Подсчитать общее кол-во баллов
        total = 0.0
        for token in tokens:
            total += float(token)

        # Вычислить средний балл
        average = total / len(tokens)
        print(f'Средний балл: {average}')

if __name__ == '__main__':
    main()