import feet_to_inches

def main():
    feet = int(input('Введите кол-во футов: '))
    inches = feet_to_inches.get_inches(feet)
    print(f'{inches}')
    
main()