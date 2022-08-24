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
        stamps.append( current_stamp)

    return stamps


game_stamps = generate_game()

def get_score(game_stamps, offset):
    a = 'Данного оффсета не найдено'
    if type(game_stamps)!=list or len(game_stamps)!=50001 :
        a = 'Первым аргументом должен быть список, длинной 50001 значений'
        return a
    if type(game_stamps[1])!=dict :
        a = 'Список должен состоять из словарей'
        return a
    if 'offset' not in game_stamps[50000] or 'score' not in game_stamps[50000] :
        a = 'Список не содержит оффсета и/или счета'
        return a
    if type(offset) != int or offset<0 or offset>150000 :
        a = 'Оффсет должен быть числом от 0 до 150000 '
        return a
    for i in game_stamps :
        if offset == i['offset'] :
            home=i['score']['home']
            away=i['score']['away']
            break
    return {'home' : home,'away' :away} if a == 'Данного оффсета не найдено' else a
