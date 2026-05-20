again = 'п'
while again.upper() == 'П':
    number1 = int(input('Введите число 1: '))
    number2 = int(input('Введите число 2: '))
    total = number1 + number2
    again = input('Желаете повторить программу или выйти? (П/В) ')
    if again.upper() == 'П':
        again.upper()
    else:
        break