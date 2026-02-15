mass = int(input('Введите массу пакета '))
tarif = 0

if mass <= 200:
    tarif = 150
    total = tarif * (mass / 100)
    print(f'Плата за доставку составит {total:.2f} рублей')

elif mass >= 200 and mass <= 600:
    tarif = 300
    total = tarif * (mass / 100)
    print(f'Плата за доставку составит {total:.2f} рублей')

elif mass >= 600 and mass <= 1000:
    tarif = 400
    total = tarif * (mass / 100)
    print(f'Плата за доставку составит {total:.2f} рублей')

elif mass >= 1000:
    tarif = 475
    total = tarif * (mass / 100)
    print(f'Плата за доставку составит {total:.2f} рублей')