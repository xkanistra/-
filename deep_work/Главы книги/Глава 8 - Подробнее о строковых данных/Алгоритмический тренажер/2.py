mystring = 'Я иду по улице и читаю'
total = 0
for ch in mystring:
    if ch.isspace():
        total += 1

print('Пробелов:', total)