import math
import os
from random import *

range_input_start = 0
range_input_end = 0
decision = ""
user_guess = 0
ans = 0
game_round = 1
end_game = 0
result = 0
divide_check = False
guess_count = 0


def setup_game_properties():
    global range_input_start, range_input_end, decision
    decision_possible = ["y", "n"]
    while True:  # define range size of range for random number
        try:
            while decision != 'y':
                range_input_start = int(input("Input \"start\" number you wanna guess: "))
                range_input_end = int(input("Input \"end\" number you wanna guess: "))
                decision = input("Are you sure?(y/n): ")
                while decision not in decision_possible:
                    print("Only \"y\" and \"n\"")
                    decision = input("Are you sure?(y/n): ")
                if decision == 'n':
                    print("*" * 20)
                    continue
            print("-" * 20)
        except ValueError:
            print("Input number please!")
            print("*" * 20)
            continue
        else:
            break


def hint_divided():  # this hint gives to user once
    global divide_check
    if not divide_check:
        # Can be divided by ...(prime number)
        prime_num = []
        for num in range(range_input_start, range_input_end + 1):  # Build a prime number lst
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    prime_num.append(num)
        can_divided = 0
        for p in prime_num:
            if ans % p == 0:
                can_divided = p
                break
        print("_" * 10, "HINT", "_" * 10)
        print(f"Answer can be divided by {can_divided}")
        print("" * 20)
        divide_check = True


def Game_run():
    global ans, game_round, user_guess, divide_check, guess_count
    print("Game Developed by Ratanon Khamrong")
    print(f"Welcome to \"Number Guessing\" game! round {game_round}")
    print("-" * 20)
    setup_game_properties()
    ans = randint(int(range_input_start), int(range_input_end))
    guess_limit = round(math.log(range_input_end - range_input_start + 1, 2))
    print(f"You have only {guess_limit} chance to guess!")

    while True:
        if not divide_check and randint(1, 2) == 2:
            hint_divided()
        try:
            print(guess_limit - guess_count, "guess left")
            user_guess = int(input(f"Please guess the number from {range_input_start} to {range_input_end}: "))
            guess_count += 1
        except ValueError:
            print("Not number")
        else:
            if user_guess == ans or guess_count == guess_limit:
                break
            print(user_guess, "is incorrect answer")
            if user_guess > ans:
                print("_" * 20)
                print("Your guess is too high!\n")
            elif user_guess < ans:
                print("_" * 20)
                print("Your guess is too low!\n")
            continue
    if user_guess == ans:
        print("-" * 20)
        print(f"{ans} is the correct answer!")
    else:
        print(f"OUT OF GUESSES! the answer is {ans} Better luck next time")


Game_run()
while end_game != "n":
    end_game = input("Play again? y/n: ")
    while end_game not in ["y", "n"]:
        print("Only \"y\" and \"n\"")
        end_game = input("Play again? y/n: ")
    if end_game == "y":  # define all variable to default
        game_round += 1
        range_input_start = 0
        range_input_end = 0
        decision = ""
        user_guess = 0
        hint_count = 0
        ans = 0
        end_game = 0
        divide_check = False
        guess_count = 0
        Game_run()
print("_" * 10, "GAME ENDED", "_" * 10)
os.system("pause")
