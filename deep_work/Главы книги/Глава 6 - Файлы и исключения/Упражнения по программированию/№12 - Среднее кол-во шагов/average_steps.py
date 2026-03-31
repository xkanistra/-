# Программа расчитывает среднее кол-во шагов за каждый месяц в году
JAN = 31
FEB = 28
MAR = 31
APR = 30
MAY = 31
JUN = 30
JUL = 31
AUG = 31
SEP = 30
OCT = 31
NOV = 30
DEC = 31

def main():
    # File open for read
    stepsFile = open('steps.txt', 'r')

    average_steps(stepsFile, 'январе', JAN)
    average_steps(stepsFile, 'феврале', FEB)
    average_steps(stepsFile, 'марте', MAR)
    average_steps(stepsFile, 'апреле', APR)
    average_steps(stepsFile, 'мае', MAY)
    average_steps(stepsFile, 'июне', JUN)
    average_steps(stepsFile, 'июле', JUL)
    average_steps(stepsFile, 'августе', AUG)
    average_steps(stepsFile, 'сентябре', SEP)
    average_steps(stepsFile, 'октябре', OCT)
    average_steps(stepsFile, 'ноябре', NOV)
    average_steps(stepsFile, 'декабре', DEC)
      
    stepsFile.close()

def average_steps(file, mounth_name, day):
    sum = 0
    for count in range(day):
        sum += int(file.readline())
    average = sum / day
    print(f'Среднее кол-во шагов в {mounth_name} составило: {average:.0f}')

if __name__ == '__main__':
    main()