from random import choice
from game_data import data
from art import logo, vs

def get_random_person():
    return choice(data)

def turn_to_dict(user_choice, person_1, person_2):
    if user_choice == "A":
        return person_1
    elif user_choice == "B":
        return person_2

def compare_followers(dict_1, dict_2):
    if dict_1["follower_count"] > dict_2["follower_count"]:
        return dict_1
    else:
        return dict_2

def higher_lower():
    score = 0
    while True:
        print(logo)
        if score == 0:
            person_1 = get_random_person()
        else:
            print(f"Yes. You are absolutely RIGHT!\nCurrent Score: {score}")
            person_1 = next_person

        person_2 = get_random_person()
        while person_1 == person_2:
            person_2 = get_random_person()

        print(f"Compare A: {person_1['name']}, a {person_1['description']}, from {person_1['country']}")
        print(vs)
        print(f"Compare B: {person_2['name']}, a {person_2['description']}, from {person_2['country']}")

        user_str = input("Who has more followers? Type 'A' or 'B': ").upper()

        user_choice = turn_to_dict(user_str, person_1, person_2)
        more_followers = compare_followers(person_1, person_2)

        if user_choice == more_followers:
            score += 1
            next_person = choice([person_1, person_2])
        else:
            print(f"Oh no! That's wrong.\nFinal Score: {score}")
            break

game_over = False
while not game_over:
    score = 0
    higher_lower()
    play_again = input("\nDo you want to play again? (Type 'yes' or 'no'): ").lower()
    if play_again == "yes":
        game_over = False
    else:
        game_over = True
