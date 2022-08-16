def generate_password(l):
    import string
    import random
    x=[i for i in string.ascii_uppercase if i not in 'OI']
    y=[i for i in string.ascii_lowercase if i not in 'ol']
    z=[i for i in string.digits if i not in '01']
    c=[]
    while len(c)<l:
        c +=[random.choice(x)]
        if len(c)>=l:
            break
        c +=[random.choice(y)]
        if len(c)>=l:
            break        
        c +=[random.choice(z)]
    random.shuffle(c)
    return ''.join(c)

def generate_passwords(c, l):
    return [generate_password(l) for _ in range(c)]
    

n, m = int(input()), int(input())
print(*generate_passwords(n, m) , sep='\n')