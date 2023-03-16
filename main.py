list1 = [1, 2, 3]
print(list1)
print(*list1)

for i in list1:
    print(i)

print(len(list1))
print(list1[1])

list1.append(4)
print(*list1)

list2 = []
for i in range(1, 6):
    list2.append(i)

print(*list2)

# Удаление последнего элемента списка
print(list1.pop())
print(list1)

# Удаление последнего элемента списка с переменной
a = list1.pop()
print(a)
print(list1)

# Удаление элемента списка по индексу
print(list2.pop(0))
print(list2)

# Добавление элемента списка по индексу
list1.insert(1, 3)
print(list1)

# Создание кортежа
tuple1 = (1, 4, )

list3 = [1, 3, 5]
print(list3)
tuple2 = tuple(list3)
print(tuple2)

a, b, c = tuple2
print(a, b, c)

# Создание словаря
dic1 = {}

dic1['q'] = 'qwerty'
print(dic1)

dic1['w'] = 'werty'
print(dic1)

print(dic1['q'])

# Создание множества
colors = {'red', 'green', 'blue'}
print(colors)
colors.add('grey')
print(colors)

colors.remove('red')
print(colors)

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()
d = a.union(b)                                  # d = {1, 2, 3, 5, 8, 13, 21}
e = a.intersection(b)                           # e = {8, 2, 5}
f = a.difference(b)                             # f = {1, 3}
g = b.difference(a)                             # g = {13, 21}
h = a.union(b).difference(a.intersection(b))    # h = {1, 21, 3, 13}