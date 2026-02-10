score = int(input())
A_score = 90
B_score = 80
C_score = 70
D_score = 60
F_score = 50
if score >= A_score:
    print('Ваш уровень - А')
else:
    if score >= B_score:
        print('Ваш уровень - B')
    else:
        if score >= C_score:
            print('Ваш уровень - С')
        else:
            if score >= D_score:
                print('Ваш уровень - D')
            else:
                print('Ваш уровень - F')