#это к задачка  из одной компании,требовалось  разобрать , написать get_score(вывести счет) и протестировать с unittest
# на кой черт тут нужен offset я не понял:),но оставил код без изменений.
# я не могу сказать что хорошо разобрался с unittest ,но кое что для себя вынес.

from pprint import pprint
import unittest
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP]
    current_stamp = INITIAL_STAMP
    for i in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append( current_stamp)   #здесь можно было сделать привязку к i : current_stamp , тогда в get_score  можно было сократить время до O-большое(времени выполнения)==(1), но как я писал вверху по заданию исходный код менять было нельзя.

    return stamps


game_stamps = generate_game()

def get_score(game_stamps, offset):
    for i in game_stamps :
        if offset == i :
            home=i['score']['home']
            away=i['score']['away']
    return home, away

class Test(unittest.TestCase) :
    
    def test_get_score(self) :
        for _ in range(10000):
            offset =random.choice(game_stamps)
            a=get_score(game_stamps,offset)

            assert len(game_stamps)==50001
            self.assertEqual(len(a),2) #разницы между обычным ассертом и юниттестом особо не вижу,в unittest есть удобные функции,но тут их вроде нет смысла использовать

if __name__ == '__main__' :
    unittest.main()


