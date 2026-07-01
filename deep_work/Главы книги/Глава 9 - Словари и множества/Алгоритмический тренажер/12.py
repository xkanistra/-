test_average = {'Джанель':98, 'Сэм':87, 'Дженнифер':92,
                'Томас':74, 'Салли':89, 'Зеб':84}
high_score = {}
high_score = {k:v for k, v in test_average.items() if v > 90 }
print(high_score)