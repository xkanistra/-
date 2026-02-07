IT_pack = 99
buy_pack = int(input('Введите кол-во приобретенных пакетов ПО '))

if buy_pack >= 10 and buy_pack <= 19: 
    price = buy_pack * IT_pack
    sell_price = price * 0.1
    sell = price - sell_price
    print(f'Стоимость всех пакетов составляет {price:.2f} $\n'
          f'Размер скидки {sell_price:.2f} $\n'
          f'Итоговая стоимость {sell:.2f} $')

elif buy_pack >= 20 and buy_pack <= 49: 
    price = buy_pack * IT_pack
    sell_price = price * 0.2
    sell = price - sell_price
    print(f'Стоимость всех пакетов составляет {price:.2f} $\n'
          f'Размер скидки {sell_price:.2f} $\n'
          f'Итоговая стоимость {sell:.2f} $')
    
elif buy_pack >= 50 and buy_pack <= 99: 
    price = buy_pack * IT_pack
    sell_price = price * 0.3
    sell = price - sell_price
    print(f'Стоимость всех пакетов составляет {price:.2f} $\n'
          f'Размер скидки {sell_price:.2f} $\n'
          f'Итоговая стоимость {sell:.2f} $')
    
elif buy_pack > 100: 
    price = buy_pack * IT_pack
    sell_price = price * 0.4
    sell = price - sell_price
    print(f'Стоимость всех пакетов составляет {price:.2f} $\n'
          f'Размер скидки {sell_price:.2f} $\n'
          f'Итоговая стоимость {sell:.2f} $')