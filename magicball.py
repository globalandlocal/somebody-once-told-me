import random
print('Дарова, я магический шар из Чернобыля и предсказываю ебучее будущее.Как звать то?')
n =input()
print(f'Ну здарова {n.title()} ,загадывай желание и напиши "да" как будешь готов.')
while input() == 'да':
    answers = ['У тебя все получится','даже не думай','возможно прокатит','Ты станешь мутантом, но вообще прокатит','Тебя сожрут норки','Да ,но ты поймаешь маслину,возможно даже не одну','это что, анекдот?','для этого тебе понадобится проводник','да, но ты уверен что оно того стоит?','ебать ты извращенец, но да','не чувак,ничем хорошимэто не кончится','этого варианта нет ни в одном из 5 миллионов вариантов будущего, доступных мне']
    c =random.randrange(len(answers))
    print(answers[c])
    print('Попробуешь еще?')
print(f'Ну удачки тебе, если что помни что на самом деле все в твоих руках ,сталкер {n}')
        