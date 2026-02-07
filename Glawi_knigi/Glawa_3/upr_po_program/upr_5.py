mass = float(input("Введите вашу массу в кг "))
weight = mass * 9.8

print(f"Вес тела состовляет {weight:.2f} H")
if weight > 500:
    print("Тело слишком тяжелое")
elif weight < 100:
    print("Тело слишком легкое")
else:
    print("Тело в норме")
