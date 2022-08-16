import random
print('Введите любое целе число от 1 до 100 , у вас 10 попыток :')
i = input()
w = random.randint(1 , 100)
c = 1
while c != 12 :
    if c ==11 :
        print('Вы потратили все попытки !Попробуем заново? Напишите "да" или "нет"')
        if input() == 'да' :
            c =0
            i =input()
        else :
            print('Приятно было играть с вами. Еще увидимся!')
            break  
    def is_digit(i) :
        return i.isdigit() and 1<=int(i)<=100
    while is_digit(i) == False :
        print('Вы нарушили правила игры ! Надо ввести целое число от1 до 100')
        i = input()
    i =int(i)
    if w < i :
        print('слишком большое число , вводите поменьше:')
        i =input()
        c += 1
    elif w > i :
        print('Маловато взял , давай побольше :')
        i = input()
        c += 1
    elif w == i:
        print(f'Поздравляем, вы угадали число с {c} попытки! ')
        print('Хотите сыграть еще? Напишите "да" или "нет".')
        if input() == 'да' :
            c =0
            i =input()
        else :
            print('Приятно было играть с вами. Еще увидимся!')
            break