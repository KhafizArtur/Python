import time
class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']
    __n = 0
    def running(self):
        while self.__n < 2:
            for i in range(3):
                if i == 0:
                    print(self.__color[i])
                    time.sleep(7)
                elif i == 1:
                    print(self.__color[i])
                    time.sleep(2)
                else:
                    print(self.__color[i])
                    time.sleep(7)
            self.__n += 1
        return f'stop'


class Road:
    def __init__(self, length, width):
        self._len = int(length)
        self._wid = int(width)
        self.kg = 25
        self.cm = 5
        print(f'Расчет асфальта по ширине и длине {self._len}м*{self._wid}м*{self.kg}кг*{self.cm}см={self._len * self._wid * self.kg * self.cm} кг')

class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict(wage=200000, bonus=20000)

class Position(Worker):
    def get_full_name(self):
        Worker.__init__(self, self.name, self.surname, self.position)
        return f'Фамилия: {self.surname} Имя:{self.name} должность:{self.position}'
    def get_total_income(self):
        self.w=int(self._income['wage'])
        self.b = int(self._income['bonus'])
        return f'Доход: {self.w+self.b} '

class Car:
    def __init__(self, speed,color, name):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = False
        self.type='транспорт'
    def info(self):
        return f'Машина :{self.name} цвет: {self.color} тип транспорта: {self.type}'
    def show_speed(self):
        return f'Скорость машины:{self.speed}'
    def go(self):
        return 'Поехали!'
    def stop(self):
        return 'Стоп'
    def turn(self,direction):
        return f'Повернули {direction}'
    def police(self):
        if self.is_police==True:
            return 'Вы едете на полицейской машине!'
        else:
            return 'Вы едете на обычной машине!'
class TownCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self.type='городской'
    def show_speed(self):
        if self.speed>=60:
            return f'Превышение скорости для городского транспорта'
        else:
            return f'Скорость машины:{self.speed}'
class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self.name = 'Феррари'
        self.color = 'Красный'
        self.type = 'спортивный'
    def police(self):
        if self.is_police == True:
            return 'Вы едете на полицейской машине!'
        else:
            return 'Вы едете на спортивной машине!'
class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self.type = 'рабочий'
    def show_speed(self):
        if self.speed >= 40:
            return f'Превышение скорости для городского транспорта'
        else:
            return f'Скорость машины:{self.speed}'
    def police(self):
        if self.is_police == True:
            return 'Вы едете на полицейской машине!'
        else:
            return 'Вы едете на рабочей машине!'
class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self.type = 'полиция'
        self.is_police = True

class Stationery:
    title= ['канц.товар','ручка','карандаш','маркер']
    def draw(self):
        return f'Запуск отрисовки {self.title[0]}'
class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title[1]}'
class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title[2]}'
class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title[3]}'
print('*' * 50)
print('Задание 1')
try:
    light=TrafficLight()
    print(light.running())
except TypeError:
    print('Что-то пошло не так')

print('*' * 50)
print('Задание 2')
try:
    l = int(input('Введите длину в метрах: '))
    w = int(input('Введите ширину в метрах: '))
    asphalt = Road(l, w)
except TypeError:
    print('Вы не ввели параметры')

print('*' * 50)
print('Задание 3')

try:
    f = input('Введите фамилию: ')
    n = input('Введите имя: ')
    d = input('Введите должность: ')
    p = Position(n, f, d)
    print(p.get_full_name())
    print(p.get_total_income())
except TypeError:
     print('Вы не ввели параметры')


print('*' * 50)
print('Задание 4')

try:
    s = int(input('Ваша скорость: '))
    c = input('Цвет машины: ')
    n = input('Наименование машины: ')
    p = input('Куда повернем?: ')
    car1=TownCar(s,c,n)
    print(car1.info())
    print(car1.go())
    print(car1.turn(p))
    print(car1.stop())
    print(car1.police())
    print(car1.show_speed())
    car2 = PoliceCar(s, c, n)
    print(car2.info())
    print(car2.go())
    print(car2.turn(p))
    print(car2.stop())
    print(car2.police())
    print(car2.show_speed())
    car3 = SportCar(s, c, n)
    print(car3.info())
    print(car3.go())
    print(car3.turn(p))
    print(car3.stop())
    print(car3.police())
    print(car3.show_speed())
    car4 = WorkCar(s, c, n)
    print(car4.info())
    print(car4.go())
    print(car4.turn(p))
    print(car4.stop())
    print(car4.police())
    print(car4.show_speed())
except TypeError:
     print('Вы не ввели параметры')
except ValueError:
     print('Не тот тип данных')

print('*' * 50)
print('Задание 5')
try:
    pen = Pen()
    pencil = Pencil()
    handle = Handle()
    print(pen.draw())
    print(pencil.draw())
    print(handle.draw())
except TypeError:
     print('Вы не ввели параметры')
except ValueError:
     print('Не тот тип данных')