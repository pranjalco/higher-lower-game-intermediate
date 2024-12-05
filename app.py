# importing required modules

import art
from game_data import data
from how_to_play import instructions, name
import random

"""
# Project 10: Higher Lower Game
## Description:
The Higher-Lower Game is a fun and interactive command-line game where players guess which option has more followers 
on social media. The game continues as long as the user guesses correctly, keeping track of their score. It offers a 
simple yet engaging experience, demonstrating core programming concepts like data handling, user interaction, and 
modular design.

### Features:
- Random selection of elements for comparison.
- Validation of user input for better user experience.
- Continuous gameplay until the user makes a wrong guess.
- Keeps track of and displays the user's score.
- Option to replay the game after completion.

# Level: Intermediate
Author: Pranjal Sarnaik
Date: 2024-12-05
"""


def starting_screen():
    """This function setup starting screen for user like logo and prints necessary data required to user to play the
    game"""
    # print(art.logo)
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(art.vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")


def select_from_list(list_name):
    """This function selects a random element from a given list"""
    return random.choice(list_name)


def add_blank_line():
    """This function adds blank line"""
    print("")


def get_num_followers(dict_name):
    """This function returns follower count from the game_data module"""
    return dict_name["follower_count"]


def take_user_answer():
    """This function returns answer entered by user which is going to be 'A' or 'B'"""
    answer = ""
    while answer not in ['A', 'B']:
        answer = input("Who has more followers? type 'A' or 'B': ").upper()
        if answer not in ['A', 'B']:
            print("Please give valid answer, type 'A' or 'B'")
    return answer


def who_has_more_followers(first_a, second_b, answer_by_user):
    """This function takes the answer by user with the followers of two elements compare the followers based on
    user answer and tells whether the answer is correct or not"""

    global FINAL_SCORE

    if answer_by_user == 'A':
        if first_a > second_b:
            FINAL_SCORE += 1
            return True
        else:
            return False

    if answer_by_user == 'B':
        if second_b > first_a:
            FINAL_SCORE += 1
            return True
        else:
            return False


print(instructions)
game_on = False
while not game_on:
    FINAL_SCORE = 0
    A = select_from_list(data)
    B = select_from_list(data)

    # This while loop ensures that A and B will not get same data values
    while A == B:
        B = select_from_list(data)

    A_followers = get_num_followers(A)
    B_followers = get_num_followers(B)
    # print(f"A: {A_followers}, B: {B_followers}")

    print(art.logo)
    starting_screen()

    # Taking user answer and storing it into user_answer variable
    user_answer = take_user_answer()
    print(user_answer)

    # Below we will get True or False based on answer given by user which is stored in user_answer variable
    right_or_wrong = who_has_more_followers(A_followers, B_followers, user_answer)
    print("\n" * 25)

    while right_or_wrong:
        A = B
        B = select_from_list(data)

        while A == B:
            B = select_from_list(data)

        A_followers = get_num_followers(A)
        B_followers = get_num_followers(B)
        # print(f"A: {A_followers}, B: {B_followers}")
        print(art.logo)
        print(f"You're right 😁, Current score: {FINAL_SCORE}")
        starting_screen()
        user_answer = take_user_answer()
        right_or_wrong = who_has_more_followers(A_followers, B_followers, user_answer)
        print("\n" * 25)

    print(art.logo)
    print(f"Sorry 😢, that's wrong. Final score: {FINAL_SCORE}")
    add_blank_line()
    want_to_play = input("Do you want to play again, type 'y' or 'n': ")
    if want_to_play == 'y':
        print("\n" * 20)
    else:
        print("Goodbye! 👋")
        name()
        game_on = True
