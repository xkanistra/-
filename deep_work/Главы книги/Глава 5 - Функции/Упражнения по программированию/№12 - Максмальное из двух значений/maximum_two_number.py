# Программа возвращает большее из двух значений

def main():
    num1 = int(input('Введите первое значение: '))
    num2 = int(input('Введите второе значение: '))
    result = max(num1, num2)
    print(result)
   
def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
        
main()