#!/usr/bin/env python

"""Importing all necessary modules"""
import random as rd
import os


def is_integer(maximum):
    """Check if it's a number and is between the minimum and maximum range"""

    isinteger = True
    number = input("Number: ")

    while isinteger:
        try:
            number = int(number)
            if isinstance(number, int):
                if not 1 <= number <= maximum:
                    print(f"Try a number between 1 and {maximum}")
                    number = input("Number: ")
                else:
                    isinteger = False
                    return int(number)

        except ValueError:
            print("Try only numbers, not letters")
            number = input("Number: ")


def choose_difficulty():
    """Choose difficulty"""

    os.system('clear')
    print("Choose a difficulty between 1 and 10")
    return is_integer(10)


def game_loop():
    """Start the game"""

    difficulty = choose_difficulty()
    play = True
    rndnumber = rd.randint(1, difficulty)
    tries = int(difficulty*0.5)
    dataint = 999
    games = 1
    wins = 0
    played_numbers = []

    os.system('clear')

    def reset(difficulty):
        """Reset the game if player wants to play again"""

        nonlocal play, rndnumber, tries, dataint, played_numbers
        play = True
        rndnumber = rd.randint(1, difficulty)
        tries = int(difficulty*0.5)
        dataint = 999
        played_numbers = []

    while play:

        # WHILE THE NUMBER IS INCORRECT
        while dataint != rndnumber:
            os.system('clear')
            played_numbers.sort()
            # If you lose all your tries
            if tries == 0:
                print(f"You lost! The number was {rndnumber}")
                again = input("Play again? y/n: ").lower() == "y"

                # Play again
                if again:
                    games += 1
                    reset(difficulty)

                # Close the game
                else:
                    os.system('clear')
                    play = False
                    break

            # If number is incorrect and you still have tries
            elif tries > 0:
                print(f"played numbers: {played_numbers}")
                print(
                    f"Give your guess between 1 and {difficulty}, you still have {tries} tries")
                tries -= 1
                dataint = is_integer(difficulty)
                played_numbers.append(dataint)

        # If the number is correct
        if rndnumber == dataint:
            print("Well done! You won!")

            again = input("Play again? y/n: ").lower() == "y"
            wins += 1

            # Play again
            if again:
                games += 1
                reset(difficulty)

            # Close the game
            else:
                os.system('clear')
                play = False
                break

    # Game statistics at the end
    print(f"{games} games played!")
    print(f"{wins} victories!")
    print(f"You won {int(wins/games*100)}% of the games!")


# Start the game
game_loop()
