with open('07.txt' , encoding='utf-8') as n :
    x=n.readlines()
    c=0
    for i in range(len(x)) :
        x[i]=x[i].replace(']','[')
        x[i]=x[i].strip().split('[')
        f = 0
        for j in range(len(x[i])) :
            if f==1:
                break
            if j%2==1 :
                for k in range(len(x[i][j])-2) :
                    if x[i][j][k]!= x[i][j][k+1] and x[i][j][k:k+2] == x[i][j][k+3:k+1:-1] :
                        x[i]=['0987612345','123450986']
                        f=1
                        break
    for i in x:
        f=0
        for j in i:
            if f==1 :
                break
            for k in range(len(j)-2):
                if j[k] != j[k+1] and j[k:k+2] == j[k+3:k+1:-1] :
                    f=1
                    c +=1
                    break
print(c)
