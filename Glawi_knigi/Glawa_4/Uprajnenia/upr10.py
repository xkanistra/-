# Плата за обучение.

SEMESTER = 145000
year = SEMESTER * 2

for i in range(1, 5 + 1):
    procent = year * 0.03
    year += procent
    print(f'{i}\t{year:.2f}')
