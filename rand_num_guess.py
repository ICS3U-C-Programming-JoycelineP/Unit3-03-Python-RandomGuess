#!/usr/bin/env python3
# Created by: Joyceline
# Created on: Oct 15 2026
# This program asks the user to guess a random number between 7 and 12 and checks if it is correct or not.

import random


def main():
    # Get random number between 7 and 12 as an integer
    random_number = random.randint(7, 12)

    # Get the user's guess
    user_input = int(input("Enter a number between 7 and 12: "))

    # Guess if user_input == random number
    if user_input == random_number:

        # Display you got it right
        print("You are correct")

    # Guess if user_input != random number
    if user_input != random_number:

        # Display you got it wrong, the correct answer was random_number
        print("You got it wrong, the correct answer was {}".format(random_number))


if __name__ == "__main__":
    main()
