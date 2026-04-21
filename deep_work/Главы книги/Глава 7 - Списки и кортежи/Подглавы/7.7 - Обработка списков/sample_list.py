# Демонстрация работы функции sample
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
selected = random.sample(numbers, k=3)
print(selected)