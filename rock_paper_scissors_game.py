#  In this game, you just need to choose one option from rock, paper, and scissors
import random

rock = "0"
paper = "1"
scissors = "2"

choice = [rock, paper, scissors]

user_choice = input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n")


computer_choice = random.choice(choice)

if computer_choice == "0":
    print("Computer choice ROCK")
elif computer_choice == "1":
    print("Computer choice PAPER")
elif computer_choice == "2":
    print("Computer choice SCISSORS")

if user_choice == "0" and computer_choice == "1":
    print("You lose, paper covers rock")
elif user_choice == "0" and computer_choice == "2":
    print("You won, rock crushes scissors")
elif user_choice == "1" and computer_choice == "0":
    print("You won, paper covers rock")
elif user_choice == "1" and computer_choice == "2":
    print("You lose, scissors cuts paper")
elif user_choice == "2" and computer_choice == "0":
    print("You lose, rock crushes scissors")
elif user_choice == "2" and computer_choice == "1":
    print("You won, scissors cuts paper")
elif computer_choice == user_choice:
    print("It's a draw! try again")
