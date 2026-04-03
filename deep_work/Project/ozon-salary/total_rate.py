# Расчет общей зп за месяц
TAX = 0.13
FSZN = 0.01
COEF = 216
def main():
    total = 0.0
    rate = read_total_rateFile(total, TAX, COEF, FSZN)
    salary_histryFile(rate)

def read_total_rateFile(total, TAX, COEF, FSZN):
    with open(r'Project/ozon-salary/total_rate.txt', 'r', encoding = 'utf-8') as readFile:
        for line in readFile:
            # Прочитать строку с зп
            num = float(line)
            # Суммировать зп
            total += num
        if total < 1308:
            fszn = total * FSZN
            tax = (total - COEF) * TAX
            clear = total - fszn - tax
            return total
        else:
            clear = total * TAX
            return clear

def salary_histryFile(rate):
    with open(r'Project/ozon-salary/salary_history.txt', 'a', encoding = 'utf-8') as salaryFile:
        salaryFile.write(f'Итоговая ЗП: {rate:.2f} BYN\n')
        print('Данные сохранены в файл salary_history.txt')

if __name__ == '__main__': 
    main()