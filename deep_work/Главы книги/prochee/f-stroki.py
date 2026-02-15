# Тут треню работу с f строками
name = "Лиза"
year = "года"
expenses = 1800.0
print(
    f"I love {name} и мы встречаемся {2025 - 2022} {year}\n"
    f"и мы тратим в месяц {expenses / 2.5:.2f} BYN\n"
    f"{expenses + 750:>10,.0f} BYN наша общая зп"
)

# 2.41
PROCENT = 0.1
price = 125.6
print(f"С учетом скидки стоимость товара составит {price * PROCENT:^10.2f} рублей")
