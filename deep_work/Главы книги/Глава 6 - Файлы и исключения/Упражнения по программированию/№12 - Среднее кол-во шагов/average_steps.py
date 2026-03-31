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
    total_num = 0
    total_sum = 0
    stepsFile = open('steps.txt', 'r')
    
    for line in stepsFile:
        line = int(stepsFile.readline())
        total_num += 1
        total_sum += line
        if total_num == 31:
            totalJAN = total_sum
            averageJAN = totalJAN / JAN
        elif total_num == 59:
            totalFEB = total_sum - totalJAN
            averageFEB = totalFEB / FEB
        elif total_num == 90:
            totalMAR = total_sum - totalJAN
            averageMAR = totalMAR / MAR
        elif total_num == 120:
            totalAPR = total_sum - totalMAR
            averageAPR = totalAPR / APR
        elif total_num == 151: 
            totalMAY = total_sum - totalAPR
            averageMAY = totalMAY / MAY
        elif total_num == 181:
            totalJUN = total_sum - totalMAY
            averageJUN = totalJUN / JUN
        elif total_num == 212:
            totalJUL = total_sum - totalJUN
            averageJUL = totalJUL / JUL
        elif total_num == 243: 
            totalAUG = total_sum - totalJUL
            averageAUG = totalAUG / AUG
        elif total_num == 273:
            totalSEP = total_sum - totalAUG
            averageSEP = totalSEP / SEP
        elif total_num == 304:
            totalOCT = total_sum - totalSEP
            averageOCT = totalOCT / SEP
        elif total_num == 334:
            totalNOV = total_sum - totalOCT
            averageNOV = totalNOV / NOV
        else:
            totalDEC = total_sum - totalNOV
            averageDEC = totalDEC / DEC
    print(f'Среднее кол-во шагов за Январь: {averageJAN}')
    print(f'Среднее кол-во шагов за Февраль: {averageFEB}')
    print(f'Среднее кол-во шагов за Март: {averageMAR}')
    print(f'Среднее кол-во шагов за Апрель: {averageAPR}')
    print(f'Среднее кол-во шагов за Май: {averageMAY}')
    print(f'Среднее кол-во шагов за Июнь: {averageJUN}')
    print(f'Среднее кол-во шагов за Июль: {averageJUL}')
    print(f'Среднее кол-во шагов за Август: {averageAUG}')
    print(f'Среднее кол-во шагов за Сентябрь: {averageSEP}')
    print(f'Среднее кол-во шагов за Октябрь: {averageOCT}')
    print(f'Среднее кол-во шагов за Ноябрь: {averageNOV}')
    print(f'Среднее кол-во шагов за Декабрь: {averageDEC}')

    stepsFile.close()
    # display()

# Заготовки под будущие функции но сначала проверю код выше без функций
#def get_JAN()
#def get_FEB()
#def get_MAR()
#def get_APR()
#def get_MAY()    
#def get_JUN()
#def get_JUL()
#def get_AUG()
#def get_SEP()
#def get_OCT()
#def get_NOV()
#def get_DEC()

#def display():

    
if __name__ == '__main__':
    main()