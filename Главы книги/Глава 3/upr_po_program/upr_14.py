weight = float(input('Введите вес тела в кг '))
height = float(input('Введите рост в метрах '))

IMT = weight / (height ** 2)

print(f'Вес {weight:.2f} кг')
print(f'Рост {height:.2f} м')

if IMT < 18.5:
    print(f'Ваш ИМТ {IMT:.2f}\n'
          f'Вес ниже нормы')
    
elif IMT >= 18.5 and IMT <= 25:
    print(f'Ваш ИМТ {IMT:.2f}\n'
          f'Вес в норме')
    
elif IMT > 25:
    print(f'Ваш ИМТ {IMT:.2f}\n'
          f'Вес выше нормы')