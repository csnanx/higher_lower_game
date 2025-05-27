from random import choice
from game_data import data
from art import logo, vs

def get_random_person():
    return choice(data)

print(logo)
person_1 = get_random_person()
person_2 = get_random_person()

print(f"Compare A: {person_1['name']}, a {person_1['description']}, from {person_1['country']}")
print(f"Compare B: {person_2['name']}, a {person_2['description']}, from {person_2['country']}")

user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

if user_choice == "A":
    user_choice = person_1
elif user_choice == "B":
    user_choice = person_2

print(user_choice)