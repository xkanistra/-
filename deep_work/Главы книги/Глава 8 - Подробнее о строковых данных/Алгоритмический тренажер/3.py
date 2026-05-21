mystring = '15000 бел руб выручка от 500 клиентов'
total = 0
for ch in mystring:
    if ch.isdigit():
        total += 1
print(f'Чисев в тексте: {total}')