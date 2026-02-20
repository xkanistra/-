# Программа расчитывает доход от продажи билетов

# Константы под каждый класс мест (A, B, C)
A = 20
B = 15
C= 10

def main():
    classA = int(input('Продано билетов в классе А: '))
    classB = int(input('Продано билетов в классе B: '))
    classC = int(input('Продано билетов в классе C: '))
    
    a = get_classA(classA)
    b = get_classB(classB)
    c = get_classC(classC)

    total_sale = get_total_sale(a, b, c)

    print(f'Доход от билетов класса A: {a}$\n'
          f'Доход от билетов класса b: {b}$\n'
          f'Доход от билетов класса C: {c}$\n'
          f'Доход от продажи билетов: {total_sale}$')

# Расчет дохода от класса А
def get_classA(classA):
    result = classA * A
    return result

# Расчет дохода от класса B
def get_classB(classB):
    result = classB * B
    return result

# Расчет дохода от класса C
def get_classC(classC):
    result = classC * C
    return result

# Расчет общего дохода от билетов
def get_total_sale(a, b, c):
    result = a + b + c
    return result

main()
