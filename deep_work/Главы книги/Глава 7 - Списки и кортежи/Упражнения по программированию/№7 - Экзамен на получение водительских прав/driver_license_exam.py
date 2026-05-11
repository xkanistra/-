# Программа проверяет ответы на вопросы и выдает результат о сдаче/несдаче экзамена
DATA_FILE1= 'Главы книги/Глава 7 - Списки и кортежи/Упражнения по программированию/Условия для задач/student_solution.txt'

MIN_RIGHT_ANSVER = 15
MAX_ANSVER = 20
def main():
    
    right_ansver_list = add_list()
    bad_ansver_list = []
    for i in range(MAX_ANSVER):
        ansver = input(f'Введите ответ на {i + 1} вопрос: ')  
        bad_ansver_list.append(ansver)
    print(right_ansver_list)
    print()
    print(bad_ansver_list)
    total_right, total_bad, bad_ansver, result, number_list = checking_ansvers(right_ansver_list, bad_ansver_list)
    print(f'{result}\n'
          f'\n'
          f'Правильных ответов: {total_right}\n'
          f'Неправильных ответов: {total_bad}\n'
          f'{bad_ansver}\n'
          f'{number_list}')


def add_list():
    index = 0
    with open(DATA_FILE1, 'r', encoding='utf-8') as file:
        ansver = file.readlines()
    
    while index < len(ansver):
        ansver[index] = ansver[index].rstrip('\n')
        index += 1
    return ansver

def checking_ansvers(rightANSV, studentANSV):
    totalR = 0
    totalS = 0
    bad_ansver = []
    number_list = []
    index = 0

    for i in range(len(rightANSV)):
        right = rightANSV[index]
        student = studentANSV[index]
        if right == student:
            totalR += 1
        else:
            totalS += 1
            numberANSV = index + 1
            number_list.append(numberANSV)
            bad_ansver.append(student)
        index += 1

    total_right = totalR
    total_bad = totalS
    if total_right >= MIN_RIGHT_ANSVER:
        result = 'Экзамен сдан!'
    else:
        result = 'Экзамен не сдан!' 
    return total_right, total_bad, bad_ansver, result, number_list


if __name__ == '__main__':
    main()