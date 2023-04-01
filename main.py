"""
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
d = a.union(b)                                      # d = {1, 2, 3, 5, 8, 13, 21}
e = a.intersection(b)                               # e = {8, 2, 5}
f = a.difference(b)                                 # f = {1, 3}
g = b.difference(a)                                 # g = {13, 21}
h = a.union(b).difference(a.intersection(b))        # h = {1, 21, 3, 13}

# Генератор списка
list4 = [i for i in range(1, 101)]                  # list4 = [1, 2, 3 ... 99, 100]
list5 = [i for i in range(1, 101) if i % 2 == 0]    # list5 = [2, 4 ... 98, 100]
list6 = [i*2 for i in range(10) if i % 2 == 0]      # list6 = [0, 4, 8, 12, 16]
"""

#from modul1 import max1

#print(max1(5, 9))

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n -2)

# list1 = []

# for i in range(1, 10):
#     list1.append(fib(i))

# print(list1)
"""
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    
    return quick_sort(less) + [pivot] + quick_sort(greater) 

print(quick_sort([2, 45,6,7,99,5,3,54,65,67,6]))
"""
"""
def math(op, x, y):
    print(op(x, y))


math(lambda a, b: a + b, 5, 45)
"""
"""
def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x ** 2), res))
print(res)
"""

data = '12 4 58 3 79 11 111 5'

data = list(map(int, data.split()))
print(data)