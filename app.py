# Create a python game of scisors, rock, paper.
# The user will play against the computer.
# The computer will randomly choose one of the options.
# The user will choose one of the options.
# The game will be played until the user decides to stop playing.

import random

user = 0
computer = 0

while True:
    user_choice = input("Choose 'r' for rock, 'p' for paper, 's' for scissors or 'q' to quit: ")
    computer_choice = random.choice(['r', 'p', 's'])

    if user_choice == 'q':
        break

    if user_choice == computer_choice:
        print("It's a tie!")
        continue

    if user_choice == 'r':
        if computer_choice == 's':
            print("You won!")
            user += 1
        else:
            print("You lost!")
            computer += 1

    elif user_choice == 'p':
        if computer_choice == 'r':
            print("You won!")
            user += 1
        else:
            print("You lost!")
            computer += 1

    elif user_choice == 's':
        if computer_choice == 'p':
            print("You won!")
            user += 1
        else:
            print("You lost!")
            computer += 1

    else:
        print("Invalid input. Try again!")

print(f"Final score: You: {user} vs Computer: {computer}")


