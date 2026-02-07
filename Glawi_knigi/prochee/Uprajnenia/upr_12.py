STOK_1 = 2000
PRICE_1 = 40
PROCENT_1 = 0.03

STOK_2 = 2000
PRICE_2 = 42.75
PROCENT_2 = 0.03

potratil = STOK_1 * PRICE_1
commisiya_1 = potratil * PROCENT_1

prodal = PRICE_2 * STOK_2
commisiya_2 = prodal * PROCENT_2

print(f'Сумма уплаченная за акции {potratil:.2f}\n'
      f'Сумма комиссии при покупке {commisiya_1:.2f}\n'
      f'Сумма за которую продал акции {prodal:.2f}\n'
      f'Сумма комиссии при продаже {commisiya_2:.2f}\n'
      f'Осталось денег {prodal - (commisiya_1 + commisiya_2):.2f}')

if prodal - (commisiya_1 + commisiya_2) < 0 :
    print(f'Джо понес убытки')
if prodal - (commisiya_1 + commisiya_2) > 0:
    print(f'Джо получил прибыль')