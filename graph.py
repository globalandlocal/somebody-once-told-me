#вообще это копипаста из гугла,но разобрать и написать это я способен
graf={'a':['b','r'],
      'b':['a','v'],
      'c':['r','e'],
      'v':['a','b'],
      'e':['r','a'],
      'r':['b','c']}
def s(a,start) :
    iwer , stack =[] , [start]
    while stack :
        var = stack.pop()
        if var not in iwer:
            iwer.append(var)
            stack.extend(set(graf[var])-set(iwer))
    return iwer
print(s(graf,'a'))