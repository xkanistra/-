# Программа расчитывает среднюю оценку отбрасывая самую низкую
from scores import get_scores
from total import get_total

def main():
    # Получить оценки
    scores = get_scores()

    # Расчитать сумму
    total = get_total(scores)

    # Найти минимальное значение
    lowest = min(scores)

    # Вычесть из суммы минимальное значение
    total -= lowest

    # Расчет среднего
    average = total / (len(scores) - 1)

    print(f'Средняя оценка без самой низкой: {average}')

if __name__ == '__main__':
    main()