list1 = [20, 50, 60, 150, 100, 200, 65, 500]
list2 = []
list2 = [item for item in list1 if item >= 100]
list2.sort()
print(list2)