number = int(input('Введите кол-во книг купленых в этом месяце '))

if number == 0:
    print('Вы заработали 0 очков')
elif number >= 2:
    print('Вы заработали 5 очков')
elif number >= 4:
    print('Вы заработали 15 очков')
elif number >= 6:
    print('Вы заработали 30 очков')
elif number >= 8:
    print('Вы заработали 60 очков')