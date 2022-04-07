# Задание 1
print('*' *50)
print('Задание 1')
name='Artur'
age= 36
print(f'Name:{name} , age: {age}')
print('*' *50)

a=int(input('Введите длину нижнего основания трапеции, см :'))
b=int(input('Введите длину верхнего основания трапеции, см :'))
h=int(input('Введите высоту трапеции, см:'))
s=int((a+b)*h/2)
print(f'Площадь трапеции, см^2: {s}')
print('*' *50)
#Задание 2
print('*' *50)
print('Задание 2')
second=int(input('Введите количество секунд :'))
hour =second//3600
minute = (second-hour*3600)//60
sec = (second-hour*3600)%60
print(f'чч: {hour} мм:{minute} сс:{sec}')
# Задание 3
print('*' *50)
print('Задание 3')
n=input('Введите число :')
nn = n*2
nnn = n*3
n= int(n)
nn = int(nn)
nnn = int(nnn)
print(f'Сумма {n} + {nn} + {nnn} = {n+nn+nnn}')
# Задание 4
print('*' *50)
print('Задание 4')
num=int(input('Введите целое число :'))
max=0
while num>0:
    last=num%10
    num=num//10
    if last>max:
        max=last
    else:
        max=max
print(f'Самая большая цифра в числе: {max} ')
# Задание 5, 6
print('*' *50)
print('Задание 5, 6')
income=int(input('Введите сумму выручки :'))
cost=int(input('Введите сумму издержек :'))
profit=income-cost
if profit>0:
    print(f'Ваша прибыль: {profit}')
    print(f'Рентабельность в процентах: {round((profit/income)*100, 2)}')
    emp = int(input('Сколько сотрудников у фирмы :'))
    print(f'Прибыль в расчете на каждого сотрудника: {round(profit/emp,2)}')
elif profit == 0:
    print(f'Производство не рентабельно, издержки равны выручке')
else:
    print(f'Ваш убыток составляет {profit} , производство не рентабельно')
# Задание 7
print('*' *50)
print('Задание 7')
a=int(input('Начальные значения, км :'))
b=int(input('Цель, которую стремимся достигнуть, км :'))
day=1
if a>b:
    print(f'Начальные значения больше цели, вам некуда стремиться')
elif a==b:
    print(f'Вы уже достигли своей цели')
else:
    print(f'день {day} км {a}')
    while a<b:
        day = day + 1
        a=a+a/10
        print(f'день {day} км {round(a, 2)}')
        print(f'На {day} день спортсмен достигнет цели не менее {b} км')







