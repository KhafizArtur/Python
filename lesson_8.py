class Date:
        def __init__(self, dt,mm,yyyy):
            self.dt1 = dt
            self.mm1 = mm
            self.yyyy1=yyyy
            print(f'{self.valid_date(self.dt1,self.mm1,self.yyyy1)}')
            print(f' день {self.dt1} месяц {self.mm1} год {self.yyyy1}')
        @staticmethod
        def valid_date(d,m,y):
            if m==2:
                if d >= 1 and d <= 29 and y > 1000:
                    return f'Дата верна'
                else:
                    return f'Дата не верна'
            elif m in range(1,13,2):
                if d>=1 and d <= 31 and y > 1000:
                    return f'Дата верна'
                else:
                    return f'Дата не верна'
            elif m in range(4, 13, 2):
                if d >= 1 and d <= 31 and y > 1000:
                    return f'Дата верна'
                else:
                    return f'Дата не верна'
            else:
                return f'Дата не верна'
        @classmethod
        def date_num(cls,dates):
            cls.date=dates.split('-')
            d,m,y=map(int,cls.date)
            return cls ( d,m,y )

class Zero(Exception):
    def __init__(self, txt):
        self.txt=txt
class Only_int(Exception):
    def __init__(self, txt):
        self.txt=txt

def Expp():
    li=[]
    while True:
        dig = input('Введите числа через пробел, если надо остановить, то наберите stop:').split()
        for i in dig:
            try:
                if i.lower() != 'stop':
                    try:
                        if i.isdigit() == True:
                            d = int(i)
                            li.append(d)
                        else:
                            raise Only_int(f'Элемент {i} не число или введен не через пробел')
                    except Only_int as err:
                        print(err)
                elif i.lower() == 'stop':
                    print(f'Список результат {li}')
                    return
            except ValueError:
                print('Числа введены не через пробел')

        print(f'Промежуточный список {li}')

class Storage:
    storage = {'Принтер':0,'Сканер':0,'Копир':0}
    def __init__(self,equip,count,in_out):
        self.equipment = str(equip)
        self.count = int(count)
        self.in_out = int(in_out)
        if self.in_out == 1:
            self.store()
        elif self.in_out == 0:
            self.transfer()
        else:
            print(f'третий параметр не тот')
    def store(self):
        if self.equipment.lower() =='print':
            p=Print(self.equipment)
            self.storage[p.type_org]+=self.count
        elif self.equipment.lower() == 'scan':
            p = Scan(self.equipment)
            self.storage[p.type_org] += self.count
        elif self.equipment.lower() == 'copy':
            p = Copy(self.equipment)
            self.storage[p.type_org] += self.count
        else:
            print(f'Орг. техники {self.equipment.lower()} на складе не может быть ')
    def transfer(self):
        if self.equipment.lower() == 'print':
            p = Print(self.equipment)
            self.storage[p.type_org] -= self.count
            if self.storage[p.type_org]<=0:
                self.storage[p.type_org] += self.count
                print(f'Орг. техники типа: {p.type_org} не хватает на складе ')
        elif self.equipment.lower() == 'scan':
            p = Scan(self.equipment)
            self.storage[p.type_org] -= self.count
            if self.storage[p.type_org]<=0:
                self.storage[p.type_org] += self.count
                print(f'Орг. техники типа: {p.type_org} не хватает на складе ')
        elif self.equipment.lower() == 'copy':
            p = Copy(self.equipment)
            self.storage[p.type_org] -= self.count
            if self.storage[p.type_org]<=0:
                self.storage[p.type_org] += self.count
                print(f'Орг. техники типа: {p.type_org} не хватает на складе ')
        else:
            print(f'Орг. техники {self.equipment.lower()} нет')
    @classmethod
    def data_in(cls, data):
        cls.data = data.split('-')
        equip, count, in_out = cls.data
        return cls(equip, count, in_out)

class Equipment:
    def __init__(self, name):
        self.name=name
class Print(Equipment):
    def __init__(self, name):
        Equipment.__init__(self, name)
        self.type_org='Принтер'
class Scan(Equipment):
    def __init__(self, name):
        Equipment.__init__(self, name)
        self.type_org = 'Сканер'
class Copy(Equipment):
    def __init__(self, name):
        Equipment.__init__(self, name)
        self.type_org = 'Копир'


class Complex:
    def __init__(self, real, imag):
        self.imag = int(imag)
        self.real = int(real)
        if self.imag > 0:
            print(f'комплесное число {self.real}+{self.imag}i')
        elif self.imag == 0:
                print(f'комплесное число {self.real}')
        else:
            print(f'комплесное число {self.real}{self.imag}i')

    def __add__(self, b):
        if self.imag+b.imag > 0:
            return f'Сумма комплексных чисел = {self.real+b.real}+{self.imag+b.imag}i'
        elif self.imag+b.imag == 0:
            return f'Сумма комплексных чисел = {self.real+b.real}'
        else:
            return f'Сумма комплексных чисел = {self.real + b.real}{self.imag + b.imag}i'

    def __mul__(self, b):
        if self.real*b.imag + self.imag*b.real > 0:
            return f'Произведение комплексных чисел = {self.real*b.real -self.imag*b.imag}+{self.real*b.imag + self.imag*b.real}i'
        elif self.real*b.imag + self.imag*b.real == 0:
            return f'Произведение комплексных чисел = {self.real*b.real -self.imag*b.imag}'
        else:
            return f'Произведение комплексных чисел = {self.real * b.real - self.imag * b.imag}{self.real * b.imag + self.imag * b.real}i'

print('*' * 50)
print('Задание 1')
try:
    d = input('Введите дату в формате дд-мм-гггг: ')
    d1=Date.date_num(d)
except ValueError:
        print(f'Вы ввели не то формат')

print('*' * 50)
print('Задание 2')
try:
    div1 = int(input('Введите делимое:'))
    div2 = int(input('Введите делитель:'))
    if div2 == 0:
        raise Zero(f'делить на ноль нельзя')
    else:
        print(f' результат {div1 / div2}')
except ValueError:
        print(f'Вы ввели не число')
except Zero as err:
    print(err)


print('*' * 50)
print('Задание 3')
Expp()

print('*' * 50)
print('Задание 4,5,6')
while True:
    try:
        d = input('Напишите наименование оргтехники формате тип (print,scan,copy)-количество-1(на склад) или 0(в подразделение), чтобы выйти stop: ')
        if d.lower() != 'stop':
            d1 = Storage.data_in(d)
            print(f' на складе {d1.storage}')
        elif d.lower() == 'stop':
            print(f'Вышли')
            break
    except ValueError:
        print('Данные не в том формате')

print('*' * 50)
print('Задание 7')
try:
    r1 = int(input('Введите действительную часть первого комплескного числа:'))
    im1 = int(input('Введите мнимую часть первого комплескного числа:'))
    r2 = int(input('Введите действительную часть второго комплескного числа:'))
    im2 = int(input('Введите мнимую часть второго комплескного числа:'))
    a = Complex(r1,im1)
    b = Complex(r2, im2)
    print(a+b)
    print(a*b)
except ValueError:
    print('Данные не в том формате')



