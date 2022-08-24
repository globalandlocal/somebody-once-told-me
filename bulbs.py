# дано поле лампочек 1000*1000, которые по командам 'turn on' включаются(или остаются включенными , 'turn off' выключаются
# (или отаются выключенными, и 'toggle'-переключаются из включенных в выключенные и наоборот.
# Цель : посчитать количество включенных лампочек после всех операций.
# Формат ввода :'toggle 461,550 through 564,900', где числа между 'through' обозначают поле.
def light(s) :
    if s[0]+s[1]=='turnon' : 
        v1,g1=s[2].split(',')
        v2,g2=s[4].split(',')
        for i in range(int(v1),int(v2)+1) :
            for j in range(int(g1),int(g2)+1) :
                x[i][j] = 1
    if s[0]+s[1]=='turnoff' :
        v1,g1=s[2].split(',')
        v2,g2=s[4].split(',')
        for i in range(int(v1),int(v2)+1) :
            for j in range(int(g1),int(g2)+1) :
                x[i][j] = 0
    elif s[0]=='toggle' :
        v1,g1=s[1].split(',')
        v2,g2=s[3].split(',')
        for i in range(int(v1),int(v2)+1) :
            for j in range(int(g1),int(g2)+1) :
                if x[i][j] ==1 :
                    x[i][j]=0
                elif x[i][j]==0 :
                    x[i][j]=1


with open ('06.txt', encoding='utf-8') as n :
    x=[[0 for j in range(1000)] for i in range(1000)]
    c=[[j for j in i.strip().split()] for i in n.readlines()  ]
    for i in c:
        light(i)
    print(sum([sum(i) for i in x]))




