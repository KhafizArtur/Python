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
#список
month = int(input('Введите номер месяца от 1 до 12:'))
lst = ['Зима',[12,1,2], 'Весна',[3,4,5],'Лето',[6,7,8],'Осень',[9,10,11]]
for el in range(3) :
    if month == lst[1][el]:
        print(lst[0])
    elif month == lst[3][el]:
        print(lst[2])
    elif month == lst[5][el]:
        print(lst[4])
    elif month == lst[7][el]:
        print(lst[6])
# словарь
di ={'Зима':[12,1,2],'Весна':[3,4,5],'Лето':[6,7,8],'Осень':[9,10,11]}
month = int(input('Введите номер месяца от 1 до 12:'))
for el in di :
    if month in di[el]:
        print(el)

print('*' * 50)
print('Задание 4')
words = input('Введите несколько слов через пробел:').split()
for el in range(len(words)):
    if len(words[el])>10:
        st=words[el]
        print(el + 1, st[0:10])
    else:
        print(el + 1, words[el])

print('*' * 50)
print('Задание 5')
my_list=[7,5,3,3,2]
num = int(input('Введите натуральное число: '))
l=len(my_list)
for el in range(l):
    if num > my_list[el]:
        my_list.insert(el , num)
        break
    elif num<= my_list[el] and my_list[el] == my_list[l-1]:
        my_list.insert(el+1 , num)
print(my_list)
