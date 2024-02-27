# Display art
from art import logo, vs
from game_data import data
import random
import os


def format_data(account):
    """format the account data into printable format"""
    account_name = account["name"]
    account_descrb = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descrb}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_continue = True
account_b = random.choice(data)
while game_continue:
    # generate a random account from the game

    account_a = account_b
    account_b = random.choice(data)
    
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # ask user gor a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if user is correct

    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    os.system('cls')
    if is_correct:
        score += 1
        print(f"YOu right!!!, Current score: {score}.")

    else:
        game_continue = False
        print(f"Sorry, that's wrong! Final score: {score}.")
    # user if statement to check if user is correct
