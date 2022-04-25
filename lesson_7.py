class Matrix:
    def __init__(self, lists):
        self.lists = list(lists)
    def __str__(self):
        try:
            if type(int(self.lists[0][0]) == type(1)):
                self.l = len(self.lists)
                self.w = len(self.lists[0])
                self.n = ''
                for i in self.lists:
                    if len(i) == self.w:
                        self.m = ' '.join(map(str, i))
                        self.n += self.m + '\n'
                    else:
                        return f'количество элементов в сторке не сопадает с предыдущими - это не матрица'
                return self.n
            else:
                return f'stop'
        except SyntaxError:
            return f'Вы ввели недопутсимый символ'
        except ValueError:
            return f'Матрицы разной размерности'

    def __add__(self, matrix2):
        try:
            self.l = len(self.lists)
            self.w = len(self.lists[0])
            self.l2=len(matrix2.lists)
            self.w2 = len(matrix2.lists[0])
            if self.l == self.l2 and self.w == self.w2:
                self.m2=[int(self.lists[i][j])+int(matrix2.lists[i][j]) for i in range(self.l) for j in range(self.w)]
                self.m3 = [self.m2[i:i+self.w] for i in range(0, len(self.m2), self.w)]
                return self.m3
            else:
                return f'Матрицы разной размерности'
        except SyntaxError:
            return f'Вы ввели недопутсимый символ'

from abc import ABC,abstractmethod
class Garb(ABC):
    @abstractmethod
    def cost(self):
        pass
class Clothes(Garb):
    try:
        def __init__(self, val):
            self.val = float(val)
        def cost(self):
            self.clo = self.val / 6.5 + 0.5
            return f'На пальто уйдет {round(self.clo, 2)} м'
    except ValueError:
        print(f'Вы ввели не число')

class Suit(Garb):
    try:
        def __init__(self, h):
            self.h = float(h)

        def cost(self):
            self.suit = self.h * 2 + 0.3
            return f'На костюм уйдет {round(self.suit, 2)} см'
    except ValueError:
        print(f'Вы ввели не число')

class Cell():
    def __init__(self, cnt):
        self.cnt=int(cnt)
        self.cel=[i for i in range(1,self.cnt+1)]
    def cel1(self):
        return f'{self.cel}'
    def __add__(self,b):
        self.l1 = len(self.cel)
        self.l2 = len(b.cel)
        for i in range(1,self.l2+1):
            self.cel.append(self.l1+i)
        return f'{self.cel}'
    def __sub__(self, b):
        self.cel = [i for i in range(1, self.cnt + 1)]
        self.l1=len(self.cel)
        self.l2=len(b.cel)
        self.l3=int(self.l1)-int(self.l2)
        if self.l3>0:
            self.new_cel=[self.cel[i] for i in range(self.l3)]
            return f'{self.new_cel}'
        else:
            return f'Клетка из которой вычитают меньше'
    def __mul__(self,b):
        self.cel = [i for i in range(1, self.cnt + 1)]
        self.l1 = len(self.cel)
        self.l2 = len(b.cel)
        self.l3 = int(self.l1)*int(self.l2)-int(self.l1)
        for i in range(1, self.l3 + 1):
            self.cel.append(self.l1 + i)
        return f'{self.cel}'
    def __truediv__(self,b):
        self.cel = [i for i in range(1, self.cnt + 1)]
        self.l1 = len(self.cel)
        self.l2 = len(b.cel)
        self.l3 = int(self.l1)//int(self.l2)
        if self.l3 > 0:
            self.new_cel = [self.cel[i] for i in range(self.l3)]
            return f'{self.new_cel}'
        else:
            return f'Клетка которую делят меньше'
    def make_order(self,line):
        self.cel = [i for i in range(1, self.cnt + 1)]
        self.l1 = len(self.cel)
        self.l3 = self.l1//line
        self.l2 = self.l1-self.l1%line
        self.n=''
        if self.l1%line > 0:
            for i in range(self.l3):
                self.l_new=self.cel[i*line:i*line+line]
                self.m = ' '.join(map(str, self.l_new))
                self.n+=self.m+'\n'
            self.l_new2 = self.cel[self.l2:self.l1]
            self.m = ' '.join(map(str, self.l_new2))
            self.n+=self.m+'\n'
        else:
            for i in range(self.l3):
                self.l_new = self.cel[i * line:i * line + line]
                self.m = ' '.join(map(str, self.l_new))
                self.n+=self.m+'\n'
        return f'{self.n}'


print('*' * 50)
print('Задание 1')
li=[[1,2,3],[2,7,4],[4,5,5], [3,4,5]]
li2=[[1,2,3],[2,7,4],[4,5,5], [3,4,5]]
li3=Matrix(li)
li4=Matrix(li2)
print(li3)
print(Matrix(li3+li4))

print('*' * 50)
print('Задание 2')
try:
    v = float(input('Введите размер пальто: '))
    h = float(input('Введите рост костюма: '))
    clo = Clothes(v)
    s = Suit(h)
    print(clo.cost())
    print(s.cost())
except ValueError:
        print(f'Вы ввели не число')

try:
    print('*' * 50)
    print('Задание 3')
    c=Cell(2)
    b=Cell(12)
    print(b+c)
    print(b-c)
    print(b*c)
    print(b/c)
    print(b.make_order(5))
except ValueError:
        print(f'Вы ввели не число')


