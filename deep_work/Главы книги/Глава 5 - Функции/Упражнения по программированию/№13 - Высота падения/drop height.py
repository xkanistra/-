# Программа рассчитывает расстояние в метрах, которое пролетел объект
import random

# Константы
G = 9.8


def main():
    total = 0.0
    t = random.randint(1, 10)
    for d in range(t):
        distance = falling_distance(t)
    print(f"Расстояние пройденное за время падения {t} секунд равняется: {distance:.0f} метров")

# Рассчет дистанции падения
def falling_distance(t):
    distance = 1 / 2 * G * t**2
    return distance

main()
