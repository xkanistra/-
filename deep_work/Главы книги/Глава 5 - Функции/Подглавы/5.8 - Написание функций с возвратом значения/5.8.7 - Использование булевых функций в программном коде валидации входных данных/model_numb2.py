model = int(input('Введите номер модели: '))

def is_invalid(mod_num):
    if mod_num != 100 and mod_num != 200 and mod_num != 300:
        status = True
    else:
        status = False
    return status

while is_invalid(model):
    print('Допустимыми номерами моделей являются: 100, 200, 300')
    model = int(input('Введите допустимый номер модели: '))

print(model)