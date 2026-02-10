product1 = float(input('Стоимость товара 1 '))
product2 = float(input('Стоимость товара 2 '))
product3 = float(input('Стоимость товара 3 '))
product4 = float(input('Стоимость товара 4 '))
product5 = float(input('Стоимость товара 5 '))
sum = product1 + product2 + product3 + product4 + product5
PROCENT = 0.07
tax = sum * PROCENT
print(f'Сумма товаров равна {sum:>5.2f} рублей\n'
      f'Сумма налога равна {tax:>5.2f} рублей\n'
      f'Итоговая сумма равна {sum + tax:>5.2f} рублей')