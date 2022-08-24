# типичный вариант задачки с коммивояжером
# условия : стартуешь из любого города,нужно посетить все города по наикратчайшему пути.
# пытался не использовать словари, просто так захотелось)
with open('09.txt' , encoding='utf=8') as n :
    x=[i.strip().split() for i in n.readlines()]
    x=[[ i[0] , i[2] , int(i[4]) ] for i in x ]
    d=[]
    for i in x :
        c=[i[1],i[0],i[2]]
        d.append(i)
        d.append(c)
    d=sorted(d)


def graph(h) :
    c=0
    z1=[h]
    for w in d:
        z = []
        if w not in z :
            for i in d:
                if z1[-1] == i[0] and i[1] not in z1:
                    z.append([i[1], i[2]])
            if z == []:
                break
            z = sorted(z, key=lambda x: x[1])
            z1.append(z[0][0])
            c += z[0][1]
    return c
for i in d:
    print(graph(i[0]))