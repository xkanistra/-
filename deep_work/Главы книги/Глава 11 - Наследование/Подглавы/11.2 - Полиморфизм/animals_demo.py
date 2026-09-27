# Демонстрация работы полиморфизма

import animals

mammal = animals.Mammal("обычное млекопитающее")
mammal.show_special()
mammal.make_sound()
print()

dog = animals.Dog()
dog.show_special()
dog.make_sound()
print()

cat = animals.Cat()
cat.show_special()
cat.make_sound()
