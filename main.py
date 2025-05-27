from random import choice
from game_data import data
from art import logo, vs

def get_random_person():
    return choice(data)

print(logo)
person_1 = get_random_person()
person_2 = get_random_person()
print(person_1)
print(person_2)