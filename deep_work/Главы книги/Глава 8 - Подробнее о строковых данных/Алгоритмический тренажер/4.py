mystring = 'Я открыл бизнес и теперь я топ 30 в списке Forbes'
total = 0
for ch in mystring:
    if ch.islower():
        total += 1
print('Значений в нижнем регистре:', total)