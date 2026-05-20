mystring = 'Я Люблю Лизу Очень Сильно'
total = 0
for upper in mystring:
    if upper.isupper():
        total += 1
print(total)