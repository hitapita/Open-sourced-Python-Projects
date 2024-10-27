# For all the beginners out there and advanced people. Even a small project works, made this when i was just starting out w python.

'''
Some rulesets for rock paper and scissors:

Rock > scissors.
Paper > rock.
Scissors > paper.

'''

import random
import time

while True:
    user_choice = input("Enter your choice (Rock/Paper/Scissors): ")

    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)

    time.sleep(1)
    print(f"You chose {user_choice.lower()} and the computer chose {computer_choice}...")

    time.sleep(3)
    if user_choice == "rock" and computer_choice == "scissors":
        print("Rock smashed the scissors. User wins")
    elif computer_choice == "rock" and user_choice == "scissors":
        print("Rock smashed scissors. Computer wins")
    elif user_choice == "paper" and computer_choice == "rock":
        print("Paper covered rock. User wins")
    elif computer_choice == "paper" and user_choice == "rock":
        print("Paper covered rock. Computer wins")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("Scissors cut paper. User wins")
    elif computer_choice == "scissors" and user_choice == "paper":
        print("Scissors cut paper. Computer wins")
    elif user_choice == computer_choice:
        print("Unfortunately you and the computer had the same strength. So its a tie :(")

    play_again_input = input("Play again? (y/n): ")
    if play_again_input != "y":
        print("Thanks for playing the game :)")
        break

# Project creation date: 25-10-21
