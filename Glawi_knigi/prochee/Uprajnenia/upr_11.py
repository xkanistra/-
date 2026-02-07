man = int(input('Введите кол-во парней в группе '))
woman = int(input('Введите кол-во девушек в группе '))
all = man + woman
procent_man = man / all * 100
procent_woman = woman / all * 100
print(f'Процент парней равняется {procent_man:.0f} %\n'
      f'Процент девушек равняется {procent_woman:.0f} %')