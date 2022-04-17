import json
def text_write():
    with open(r'Wite_text.txt', 'w', encoding='utf-8') as ft:
        while True:
            dig=input('Введите строку для записи, если хотите выйти, то ничего не вводите нажмите enter :')
            try:
                if dig != '':
                    ft.writelines(f'{dig}\n')
                elif dig == '':
                    return
            except ValueError:
                print('Ошибка вводимого значения')

print('*' * 50)
print('Задание 1')
text_write()

print('*' * 50)
print('Задание 2')
with open(r'words.txt', 'r', encoding='utf-8') as w:
    print(f'Файл: {w.name}')
    text=w.readlines()
    cnt=len(text)
    words=0
    for i in text:
        s=i.split()
        word=len(s)
        words+=word
    print(f'Количество строк: {cnt}')
    print(f'Количество слов: {words}')

print('*' * 50)
print('Задание 3')
try:
    with open(r'Info_empl.txt', 'r', encoding='utf-8') as w:
        print(f'Файл: {w.name}')
        text = w.readlines()
        cnt = len(text)
        summa = 0
        for i in text:
            s = i.split()
            pay = [s[p] for p in range(1, len(s), 2)]
            empl = [s[e] for e in range(0, len(s), 2)]
            pay = float(pay[0])
            summa += pay
            if pay < 20000:
                print(f'Сотрудник с окладом ниже 20000 {empl[0]}')
        print(f'Средний оклад: {round(summa / cnt, 2)}')
except ValueError:
    print(f'Проверьте правильность введенных данных в файле')

print('*' * 50)
print('Задание 4')
di= dict(One='Один', Two='Два', Three='Три', Four='Четыре', Five='Пять')
key = list(di.keys())
try:
    with open(r'number.txt', 'r', encoding='utf-8') as num:
        print(f'Файл: {num.name}')
        text = num.readlines()
        cnt = len(text)
        with open(r'number1.txt', 'w', encoding='utf-8') as num3:
            for i in text:
                s = i.split()
                s1 = str(s[0])
                for k in key:
                    if k.lower()==s1.lower():
                        s[0]=di[k]
                with open(r'number1.txt', 'a', encoding='utf-8') as num2:
                    j=' '.join(s)
                    num2.writelines(f'{j}\n')
    print(f'Новый файл: {num2.name}')
except ValueError:
    print(f'Проверьте правильность введенных данных в файле')

print('*' * 50)
print('Задание 5')
try:
    with open(r'sum_num.txt', 'w+', encoding='utf-8') as s:
        print(f'Файл: {s.name}')
        new = [i for i in range(1, 15) if i % 2 == 0]
        r=map(str,new)
        j=' '.join(r)
        print(f'Будут записаны числа: {j}')
        s.writelines(f'{j}\n')
        s.seek(0)
        text = s.readlines()
        summa=0
        for i in text:
            nums = map(int,i.split())
            for p in nums:
                summa+=p
    print(f'Файл записан: {s.name}')
    print(f'Сумма чисел из файла: {summa}')
except ValueError:
    print(f'Проверьте правильность введенных данных в файле')

print('*' * 50)
print('Задание 6')
try:
    with open(r'Hour_lesson.txt', 'r', encoding='utf-8') as h:
        di={}
        print(f'Файл: {h.name}')
        text = h.readlines()
        for i in text:
            sp = i.split(':')
            print(f'Строки: {sp}')
            h1=str(sp[1]).split(')')
            h2=[''.join(filter(str.isdigit, num)) for num in h1]
            h2.remove('')
            summa = 0
            for n in h2:
                nums = map(int, n.split())
                for p in nums:
                    summa += p
            di[sp[0]]=summa
    print(f'Словарь: {di}')
except ValueError:
    print(f'Проверьте правильность введенных данных в файле')

print('*' * 50)
print('Задание 7')
try:
    with open(r'firms.txt', 'r', encoding='utf-8') as firm:
        profit={}
        avg_profit = {}
        loss={}
        avg=0
        cnt=0
        summa = 0
        print(f'Файл: {firm.name}')
        text = firm.readlines()
        for i in text:
            pr = i.split()
            diff=int(pr[2])-int(pr[3])
            if diff>0:
                profit[pr[0]]=diff
                cnt+=1
                summa+=diff
                avg=(summa)/cnt
                avg_profit['average_profit']=round(avg,2)
            else:
                loss[pr[0]]=diff
    new=[profit, avg_profit, loss]
    print(f'Словарь: {new}')
    with open(r'avg_firms.json', 'w', encoding='utf-8') as firm2:
        json.dump(new,firm2)
except ValueError:
    print(f'Проверьте правильность введенных данных в файле')
