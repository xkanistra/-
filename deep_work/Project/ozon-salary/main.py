# Программа для расчета ЗП исходя из пиков и кол-ва смен,
# без учета налога и 

PICK_RATE = 0.06        # Ставка за один пик до вычета налогов
SHIFT_RATE = 55         # Ставка за одну смену до вычета налогов

# Константы для месяцев
JAN = 1
FEB = 2
MAR = 3
APR = 4
MAY = 5
JUN = 6
JUL = 7
AUG = 8
SEP = 9
OCT = 10
NOV = 11
DEC = 12

# Модуль для отображения даты
import datetime

def main():
    found = 'д' 
    mounth = choise_mounth(JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC)
    while found == 'д' or found == 'Д':
        choise = main_menu()
        if choise == 1:
            data = input(f"Введите дату: ")
            data = f'{data}.{mounth}.2026'
            #data = datetime.date.now()
            pick = get_pick(PICK_RATE)
            shift = get_shift(SHIFT_RATE)
            total = get_total(pick, shift)
            save_result(data, pick, total)
            save_result2(total)
            # Удалить нужно
            #found = input('Желаете продолжить? Введите д/Д если да, остальное завершит программу: ')

        elif choise == 2:
            get_read_file()
            # Удалить нужно
            #found = input('Желаете продолжить? Введите д/Д если да, остальное завершит программу: ')

        else:
            print('Программа завершена')
            break

def choise_mounth(JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC):
    print(f'1. Январь')
    print(f'2. Февраль')
    print(f'3. Март')
    print(f'4. Арель')
    print(f'5. Май')
    print(f'6. Июнь')
    print(f'7. Июль')
    print(f'8. Август')
    print(f'9. Сентябрь')
    print(f'10. Октябрь')
    print(f'11. Ноябрь')
    print(f'12. Декабрь')
    mounth = int(input('Выберите нужный месяц (Введите 1 - 12): '))
    while mounth < 1 or mounth > 12:
        mounth = int(input('ОШИБКА! Введите верное значение (1 - 12): '))
    if mounth == 1:
        return '01'
    elif mounth == 2:
        return '02'
    elif mounth == 3:
        return '03'
    elif mounth == 4:
        return '04'
    elif mounth == 5:
        return '05'
    elif mounth == 6:
        return '06'
    elif mounth == 7:
        return '07'
    elif mounth == 8:
        return '08'
    elif mounth == 9:
        return '09'
    elif mounth == 10:
        return '10'
    elif mounth == 11:
        return '11'
    else:
        return '12'
    
# Меню выбора       
def main_menu():
    print("=" * 3, "Какулятор ЗП Ozon", "=" * 3)
    print(f"1. Новый день")
    print(f"2. История")
    print(f"3. Выход")
    choise = int(input("Выберите действие: "))
    while choise < 1 or choise > 3:
        print("ОШИБКА. Не допустимое значение")
        choise = int(input("Введите допустимое значение(1, 2 или 3): "))
    return choise

# Расчет премии из пиков
def get_pick(PICK_RATE):
    accept_pick = int(input('Введите кол-во пиков принятых за смену: '))
    issued_pick = int(input('Введите кол-во пиков выданых за смену: '))
    total_pick = accept_pick + issued_pick
    total = total_pick * PICK_RATE
    return total

# Расчет оклада из смен
def get_shift(SHIFT_RATE):
    print('1 - ДА, 2 - НЕТ')
    duble_rate = int(input('Была ли двойная оплата?: '))
    if duble_rate == 1:
        shift = SHIFT_RATE * 2
        total = shift 
        return total
    else:
        shift = SHIFT_RATE
        total = shift 
        return total
    
# Расчет ЗП за день
def get_total(pick, shift):
    total = pick + shift
    return total

# Сохранение в файл
def save_result(data, pick, total):
    with open(r'Project/ozon-salary/salary_history.txt', 'a', encoding = 'utf-8') as saveResult:
        saveResult.write(f'{data} | Пиков: {pick:.2f} | За смену: {total:.2f} BYN\n ')
        print('Данные сохранены в файл salary_history.txt')

# Сохранение в файл для подсчета общей зп
def save_result2(total):
    with open(r'Project/ozon-salary/total_rate.txt', 'a', encoding = 'utf-8') as saveResult2:
        saveResult2.write(f'{total:.2f}\n')
        print('Данные сохранены в файл total_rate.txt')

# Прочтение информации из файла
def get_read_file():
    with open(r'Project/ozon-salary/salary_history.txt', 'r', encoding = 'utf-8') as readFile:
        file = readFile.read()
        print(file)

if __name__ == '__main__':
    main()