# Задание 1
# print('First lesson! ' *3)
# print('*' *50)
# name='Artur'
# age= 36
# print(f'Name:{name} , age: {age}')
# print('*' *50)
#
# a=int(input('Введите длину нижнего основания трапеции, см :'))
# b=int(input('Введите длину верхнего основания трапеции, см :'))
# h=int(input('Введите высоту трапеции, см:'))
# s=(a+b)*h/2
# print(f'Площадь трапеции, см^2: {s}')
# print('*' *50)
# Задание 2
second=int(input('Введите количество секунд :'))
hour =second//3600
minute = (second-hour*3600)//60
sec = (second-hour*3600)%60
print(f'чч: {hour} мм:{minute} сс:{sec}')




