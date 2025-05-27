from random import choice
from game_data import data

def get_random_person():
    return choice(data)

person_1 = get_random_person()
person_2 = get_random_person()