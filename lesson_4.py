from sys import argv
from functools import reduce
from itertools import count, cycle
from math import factorial


def pay():
    hour, bet, bonus = map(int, argv[1:4])
    if len(argv) < 4:
        print(f'Вы вели меньше 3 аргументов')
    elif len(argv) > 4:
        print(f'Вы вели больше 3 аргументов')
    else:
        print(f'Зарплата = {hour * bet + bonus}')


def mult(a, b):
    return a * b

def fact(n):
    f=(factorial(i) for i in range(1,n+1))
    for el in f:
        yield el


print('*' * 50)
print('Задание 1')
try:
    pay()
except ValueError:
    print('Вы ввели не тот тип данных, либо не то количество значений. Введите 3 аргумента')
except IndexError:
    print('Введите 3 аргумента')

print('*' * 50)
print('Задание 2')
try:
    li = input('Введите через пробел числа:').split()
    li = list(map(int, li))
    print(li)
    new = [li[i] for i in range(len(li)) if li[i - 1] < li[i]]
    print(new)
except ValueError:
    print('Проверьте правильность ввода. Необходимо вводить числа через пробел')

print('*' * 50)
print('Задание 3')
new = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
print(new)

print('*' * 50)
print('Задание 4')
try:
    li = input('Введите через пробел числа:').split()
    li = list(map(int, li))
    print(li)
    new = [li[i] for i in range(len(li)) if li.count(li[i]) <= 1]
    print(new)
except ValueError:
    print('Проверьте правильность ввода. Необходимо вводить числа через пробел')

print('*' * 50)
print('Задание 5')
new = [i for i in range(99, 1001) if i % 2 == 0]
print(new)
print(reduce(mult, new))

print('*' * 50)
print('Задание 6')
li = [1, 3, 5, 7, 9]
print('Итератор чисел')
for i in count(3):
    print(i)
    if i > 30:
        break
print('Итератор элементов списка')
print(li)
i=0
for el in cycle(li):
    print(el)
    i+=1
    if i > 20:
        break

print('*' * 50)
print('Задание 7')
try:
    n= int(input('Введите одно число:'))
    i=1
    for el in fact(n):
        print(f'factorial {i}! = {el}')
        i+=1
except ValueError:
    print('Необходимо ввести одно число')