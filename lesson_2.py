print('*' * 50)
print('Задание 1')
lst = ['1', 3, [4, 7, 9, 10, 21], 'abs']
for el in lst:
    print(el, type(el))

print('*' * 50)
print('Задание 2')
el2 = input('Введите значения списка через запятую:').split(',')
lst2 = el2
print(lst2)
if len(lst2) % 2 == 1:
    last = lst2[-1]
    lst2.remove(last)
    num = int(len(lst2) - len(lst2) / 2)
    for i in range(num):
        lst2[i * 2], lst2[i * 2 + 1] = lst2[i * 2 + 1], lst2[i * 2]
    lst2.append(last)
else:
    num = int(len(lst2) - len(lst2) / 2)
    for i in range(num):
        lst2[i * 2], lst2[i * 2 + 1] = lst2[i * 2 + 1], lst2[i * 2]
print(lst2)

print('*' * 50)
print('Задание 3')
