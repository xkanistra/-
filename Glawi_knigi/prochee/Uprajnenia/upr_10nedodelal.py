sugar = 1.5
oil = 1
muka = 2.75
Bulka = 48
bs_1 = 48 * 0.0015
bo_1 = 48 * 0.001
muka = 48 * 0.00275
BULKA = int(input('Введите кол-во булочек: '))
print(f'Для {BULKA} булочек понадобится\n'
      f'{BULKA * bs_1:.0f} стакана сахара\n'
      f'{BULKA * bo_1:.0f} стакана масла\n'
      f'{BULKA * muka:.0f} стакана муки')