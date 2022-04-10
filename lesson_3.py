def my_div(div_1, div_2):
    try:
        res = div_1 / div_2
        return print(round(res, 2))
    except ZeroDivisionError:
        print('Делить на ноль нельзя')
    except NameError:
        print('Вы ввели не число')


def inf(name, fam, birthday, city, email, tel):
    print(f'Name: {name} Family: {fam} Birthday: {birthday} City:{city} Email: {email}r Telephone: {tel}')

def my_func(num1, num2, num3):
    try:
        m1 = 0
        if num1 > num2:
            m1 += num1
            if num2 > num3:
                m1 += num2
            else:
                m1 += num3
        elif num1 <= num2:
            m1 += num2
            if num1 > num3:
                m1 += num1
            else:
                m1 += num3
        print(f' Сумма наибольших двух аргументов {m1}')
    except NameError:
        print('Вы ввели не число')


def rank(num1, num2):
    m = num1 ** num2
    print(f'Степень числа 1 вариант {round(m,2)}')


def rank2(num1, num2):
    if num2 > 0:
        min = num1
        for i in range(num2 - 1):
            min *= num1
            m = min
    elif num2 == 0:
        m = 1
    else:
        mod = abs(num2)
        min = 1 / num1
        for i in range(mod - 1):
            min *= 1 / num1
            m = min
    print(f'Степень числа 2 вариант {round(m,5)}')
def sum_li():
    sum=0
    while True:
        dig=input('Введите числа через пробел, если надо остановить, то q:').split()
        for i in dig:
            try:
                if i!='q':
                    d = int(i)
                    sum = sum + d
                elif i=='q':
                   print(sum)
                   return
            except ValueError:
                print('Один из элементов не число и не спец.символ')
        print(sum)

def int_func(text):
    uptext=text.title()
    return uptext

print('*' * 50)
print('Задание 1')
try:
    div1 = int(input('Введите делимое:'))
    div2 = int(input('Введите делитель:'))
    my_div(div1, div2)
except ValueError:
    print('Вы ввели не число')

print('*' * 50)
print('Задание 2')
name = input('Введите имя:')
fam = input('Введите фамилию:')
birthday = input('Введите дату рождения:')
city = input('Введите город:')
email = input('Введите email:')
tel = input('Введите телефон:')
inf(name, fam, birthday, city, email, tel)

print('*' * 50)
print('Задание 3')
try:
    num1 = int(input('Введите 1 число:'))
    num2 = int(input('Введите 2 число:'))
    num3 = int(input('Введите 3 число:'))
    my_func(num1, num2, num3)
except ValueError:
    print('Вы ввели не число')

print('*' * 50)
print('Задание 4')
try:
    num1 = int(input('Введите число:'))
    num2 = int(input('Введите степень в которую надо возвезсти:'))
    rank(num1, num2)
    rank2(num1, num2)
except ValueError:
    print('Вы ввели не число')

print('*' * 50)
print('Задание 5')
sum_li()

print('*' * 50)
print('Задание 6, 7')
try:
    text = input('Введите текст через пробел:')
    print(int_func(text))
except ValueError:
    print('Это не текст')