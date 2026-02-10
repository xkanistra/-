# Популяция
print('Программа предсказывает приблизительный размер популяции\n' \
'Для расчета заполните следующие поля:')
start = float(input('1.Стартовое кол-во организмов: '))
procent = float(input('2.Среднесуточное увеличение в %: '))
day = int(input('3.Кол-во дней для размножения: '))
print('День\tПопуляция')

procent /= 100

for population in range(1, day + 1):
    print(f'{population:.0f}\t{start:.3f}')
    average_procent = start * procent
    start += average_procent
    