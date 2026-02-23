# Программа расчитывает кинетическую энергию

def main():
    m = float(input('Введите массу тела в кг: '))
    v = float(input('Вветиде скорость тела в м/с: '))
    KinetikEnergy = kinetik_energy(m, v)
    print(f'Кинетическая энергия объекта с массой {m:.2f} кг и скоростью {v:.2f} м/с равняется: {KinetikEnergy / 1000000:,.2f} МДж')
def kinetik_energy(m, v):
    K = 1 / 2 * m * v ** 2
    return K

main()