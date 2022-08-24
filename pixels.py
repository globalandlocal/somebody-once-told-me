# дано поле пикселей 6*50 , по команде 'rect' в верхнем левом углу поле пиксели меняются(на что именно значения не имеет)
# по команде rotate пиксели должны быть смещены (не перемещены, а именно смещены все пиксели в ряду/столбе соответственно
# row/column. Цель: каково количество включенных лампочек после выполнения всех операций(по идее можно было попросить
# написать выведенное слово с помощью пикселей)
#формат ввода: 'rect 1x1' или 'rotate row y=0 by 7', где y (или x) отмечали нужную строку/столбец, а by 7 - шаг смещения
# на выводе соответственно вся матрица
with open ('08.txt' , encoding ='utf-8' ) as n :
    z=[i.strip().split() for i in n.readlines()]
    s=[ [ 0 for j in range(50) ] for i in range(6)]

def pixels(w) :
    if w[0] =='rect' :
        y,y1=w[1].split('x')
        for i in range(int(y1)) :
            for j in range(int(y)) :
                s[i][j]=1
    elif w[0]=='rotate' :
        if  w[1] == 'row' :
            y=int(w[2][2])
            step=int(w[4])
            s1=s[y][:]
            for i in range(50) :
                if i +step >49 :
                    i=i-50
                s[y][i+step] =s1[i]
        elif  w[1] == 'column' :
            x=int(w[2][2:])
            step=int(w[4])
            s1=[[j for j in i ] for i in s]
            for i in range(6) :
                if i + step > 5 :
                    i = i - 6
                s[i+step][x] =s1[i][x]

for i in z:
    pixels(i)
for i in s :
    print(*i)
print(sum([sum(i) for i in s]))