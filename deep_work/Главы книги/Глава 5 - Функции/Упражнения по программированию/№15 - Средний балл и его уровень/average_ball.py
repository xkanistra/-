# Программа расчитывает средний балл исходя из 5 оценок и выводид буквенный уровень каждой оценки

def main():
    ball1 = int(input(f'Введите 1 оценку: '))
    ball2 = int(input(f'Введите 2 оценку: '))
    ball3 = int(input(f'Введите 3 оценку: '))
    ball4 = int(input(f'Введите 4 оценку: '))
    ball5 = int(input(f'Введите 5 оценку: '))
    average = calc_average(ball1, ball2, ball3, ball4, ball5)
    grade_1 = determine_grade_1(ball1)
    grade_2 = determine_grade_2(ball2)
    grade_3 = determine_grade_3(ball3)
    grade_4 = determine_grade_4(ball4)
    grade_5 = determine_grade_5(ball5)
    print(f'Средний балл: {average:.2f}\n'
          f'Оценка 1: {ball1} = {grade_1}\n'
          f'Оценка 2: {ball2} = {grade_2}\n'
          f'Оценка 3: {ball3} = {grade_3}\n'
          f'Оценка 4: {ball4} = {grade_4}\n'
          f'Оценка 5: {ball5} = {grade_5}\n')

def calc_average(b1, b2, b3, b4, b5):
    average = (b1 + b2 + b3 + b4 + b5) / 5
    return average

def determine_grade_1(b1):
    if b1 >= 90:
        return 'A'
    elif b1 >= 80 and b1 <= 89:
        return 'B'
    elif b1 >= 700 and b1 <= 79:
        return 'C'
    elif b1 >= 60 and b1 <= 69:
        return 'D'
    else:
        return 'F'
    
def determine_grade_2(b2):
    if b2 >= 90:
        return 'A'
    elif b2 >= 80 and b2 <= 89:
        return 'B'
    elif b2 >= 700 and b2 <= 79:
        return 'C'
    elif b2 >= 60 and b2 <= 69:
        return 'D'
    elif b2 < 60:
        return 'F'

def determine_grade_3(b3):
    if b3 >= 90:
        return 'A'
    elif b3 >= 80 and b3 <= 89:
        return 'B'
    elif b3 >= 700 and b3 <= 79:
        return 'C'
    elif b3 >= 60 and b3 <= 69:
        return 'D'
    else:
        return 'F'

def determine_grade_4(b4):
    if b4 >= 90:
        return 'A'
    elif b4 >= 80 and b4 <= 89:
        return 'B'
    elif b4 >= 700 and b4 <= 79:
        return 'C'
    elif b4 >= 60 and b4 <= 69:
        return 'D'
    else:
        return 'F'

def determine_grade_5(b5):
    if b5 >= 90:
        return 'A'
    elif b5 >= 80 and b5 <= 89:
        return 'B'
    elif b5 >= 700 and b5 <= 79:
        return 'C'
    elif b5 >= 60 and b5 <= 69:
        return 'D'
    else: 
        return 'F'
    
main()