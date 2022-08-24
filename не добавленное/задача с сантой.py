c = [[0 for j in range(1401)] for i in range(1401)]
c[700][700] = 1

def santa1(x) :
    iv=700
    ig=700
    for i in x:
        if i == '<':
            ig -= 1
            c[iv][ig] = 1
        elif i == '>':
            ig += 1
            c[iv][ig] = 1
        elif i == '^':
            iv -= 1
            c[iv][ig] = 1
        elif i == 'v':
            iv += 1
            c[iv][ig] = 1


with open ('03.txt' , encoding ='utf-8') as n:
    x=n.readline().strip()
    x1=[]
    x2=[]
    for i in range(len(x)) :
        if i%2 ==0 :
            x1.append(x[i])
        else :
            x2.append(x[i])
santa1(x1)
santa1(x2)
print(sum([sum(i) for i in c]))