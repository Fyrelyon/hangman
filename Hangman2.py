###################################################################################
#Hangman2.py
#Author:    Gavin Bernard
#Date:      Created 12/05/2017
#Brief:     Simulates a game of Hangman, where the player attempts to guess a word.
###################################################################################
import time
import random
import os

def start_screen():
    file = open('art/start.txt', 'r')
    contents = file.read()
    print(contents)
    
    print("")
    start = input("[Click ENTER to continue...]")

def show_credits():
    file = open("art/credits.txt", 'r')
    contents = file.read()
    print(contents)
    
    print("Author: Gavin Bernard")
    print("Completion Date: 12/xx/2017")
    
def get_puzzle():
    file_names = os.listdir("puzzles")

    for i, f in enumerate(file_names):
        print(str(i+1) + ") " + f[0:len(f)-4])

    print("")
    choice = input("Which list would you like? ")
    choice = int(choice) - 1

    file = "puzzles/" + file_names[choice]
    print("")

    with open(file, 'r') as f:
        lines = f.read().splitlines()

    puzzle = random.choice(lines[1:])
    return puzzle

def friendly():
    while True:
        print("")
        kid = input("Is this game child friendly? (y/n): ")
        if kid == 'y' or kid == 'yes':
            return True
        if kid == 'n' or kid == 'no':
            return False
        else:
            print("")
            print("Please type \"yes\" or \"no\".")
    
def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        elif letter.isalpha() == False:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess(guesses):
    while True:
        guess = input("Guess: ")

        if guess.isalpha() and len(guess) == 1:
            if guess.lower() in guesses:
                print("")
                print("That letter has already been guessed!")
            else: return guess.lower()

        print("")
        print("Incorrect response, try again!")

def display_board(solved,strikes,misses,kid):
    print("")
    print("Solved: " + solved)
    print("Misses: " + misses)
    print("Strikes: " + str(strikes))

    h1 = ""
    h2 = ""
    h3 = ""
    h4 = ""
    h5 = ""
    h6 = ""
    h7 = ""
    h8 = ""

    if kid == False:
        h1 = "      _______ "
        h2 = "     |/      | "
        h3 = "     |      "
        h4 = "     |       "
        h5 = "     |       "
        h6 = "     |      "
        h7 = "     |"
        h8 = "  ___|_____"

    if(strikes >= 1):
        h3 += "(_)"
    if(strikes >= 2):
        if kid:
            h4 += " "
            h5 += " "
        h4 += "|"
        h5 += "|"
    if(strikes >= 3):
        if kid:
            h4 = "\\" + h4[1:]
        else:
            h4 = h4[:12] + "\\" + h4[13:]
    if(strikes >= 4):
        h4 += "/"
    if(strikes >= 5):
        h6 += "/"
    if(strikes >= 6):
        h6 += " \\"

    if kid == False:
        print(h1)

    print(h2)
    print(h3)
    print(h4)
    print(h5)
    print(h6)

    if kid == False:
        print(h7)
        print(h8)

    print("")

def show_result(strikes,limit,puzzle):
    if (strikes >= limit):
        print("You lose! The answer was " + puzzle + "!")
    else:
        print("You win! Congratulations!")

def play_again():
    while True:
        decision = input("Would you like to play again?? (y/n): ")

        if decision == 'n' or decision == 'no':
            return False

        if decision == 'y' or decision == 'yes':
            return True

        else:
            print("Please write \"yes\" or \"no\".")
            print("")
def play():
    kid = friendly()
    print("")
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle,guesses)

    strikes = 0
    misses = ""
    limit = 6

    display_board(solved,strikes,misses,kid)

    while solved != puzzle and strikes < limit:
        letter = get_guess(guesses)

        if letter.lower() not in puzzle:
            strikes += 1
            misses += letter + " "

        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved,strikes,misses,kid)

    show_result(strikes,limit,puzzle)

#This code is the start of the actual game itself.

playing = True

start_screen()

while playing:
    play()
    playing = play_again()

show_credits()
