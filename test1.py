<<<<<<< HEAD
#собственно сам тест к get_score
import unittest
import random
from get_score import game_stamps , get_score
class Test(unittest.TestCase):

    def test_get_score(self):
        for _ in range(1000):
            offset = random.choice(game_stamps)['offset']
            result = get_score(game_stamps, offset)
            self.assertEqual(len(result), 2, 'Некорректный счет')
        print('Нагрузочная проверка прошла')
        test1 = 'Первым аргументом должен быть список, длинной 50001 значений'
        test2 = 'Список должен состоять из словарей'
        test3 = 'Список не содержит оффсета и/или счета'
        test4 = 'Оффсет должен быть числом от 0 до 150000 '
        if self.assertEqual(get_score([],offset), test1) == None : #если проверка успешна возвращается значение None
            print('Проверка на список длинной 50001 значений прошла')
        if self.assertEqual(get_score([1]*50001,offset) , test2) == None :
            print ('проверка на наличие словарей прошла')
        if self.assertEqual(get_score( [{str(i) : i} for i in range(50001)],offset) , test3) == None :
            print('проверка на содержание оффсета/счета прошла')
        if self.assertEqual(get_score(game_stamps,150001), test4) == None :
            print('Проверка на корректный оффсет прошла')
        print('Все проверки прошли успешно')



if __name__ == '__main__':
    unittest.main()
=======
#собственно сам тест к get_score
import unittest
import random
from get_score import game_stamps , get_score
class Test(unittest.TestCase):

    def test_get_score(self):
        for _ in range(1000):
            offset = random.choice(game_stamps)['offset']
            result = get_score(game_stamps, offset)
            self.assertEqual(len(result), 2, 'Некорректный счет')
        print('Нагрузочная проверка прошла')
        test1 = 'Первым аргументом должен быть список, длинной 50001 значений'
        test2 = 'Список должен состоять из словарей'
        test3 = 'Список не содержит оффсета и/или счета'
        test4 = 'Оффсет должен быть числом от 0 до 150000 '
        if self.assertEqual(get_score([],offset), test1) == None : #если проверка успешна возвращается значение None
            print('Проверка на список длинной 50001 значений прошла')
        if self.assertEqual(get_score([1]*50001,offset) , test2) == None :
            print ('проверка на наличие словарей прошла')
        if self.assertEqual(get_score( [{str(i) : i} for i in range(50001)],offset) , test3) == None :
            print('проверка на содержание оффсета/счета прошла')
        if self.assertEqual(get_score(game_stamps,150001), test4) == None :
            print('Проверка на корректный оффсет прошла')
        print('Все проверки прошли успешно')



if __name__ == '__main__':
    unittest.main()
>>>>>>> 3bd077f8802527e94e1af152ec8f60c6a26688fb
