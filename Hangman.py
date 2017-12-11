###################################################################################
#Hangman.py
#Author:    Gavin Bernard
#Date:      Created 11/09/2017
#Brief:     Simulates a game of Hangman, where the player attempts to guess a word.
###################################################################################
import time
import random

def hangman():
    print("   _   _                                         ")
    print("  | | | |                                        ")
    print("  | |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
    print("  |  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
    print("  | | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("  |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                      __/ |                      ")
    print("                     |___/                       ")

    print("")
    start = input("[Cliquez ENTER pour continuer...]")

def show_credits():
    print("    _____                         ____                 ")
    print("   / ____|                       / __ \                ")
    print("  | |  __  __ _ _ __ ___   ___  | |  | |_   _ ___ _ __ ")
    print("  | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|")
    print("  | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   ")
    print("   \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   ")
    print("")
    print("Écrivain: Gavin Bernard")
    print("Jour D'Achèvement: 11/21/2017")
    
def get_puzzle():
    choice = ["omelette du fromage", "le lundi", "bonjour","salut"
              ,"baguette","parapluie","les gants","le sac","baladeur"
              ,"agenda","le portefeuille","les bequilles","du papier bulle"
              ,"le bus","le bateau a voile"]
    return choice[random.randint(0,len(choice))]

def friendly():
    while True:
        print("")
        kid = input("Est-ce jeu pour les enfants? (o/n): ")
        if kid == 'o' or kid == 'oui':
            return True
        if kid == 'n' or kid == 'non':
            return False
        else:
            print("")
            print("Écrivez \"o\" ou \"n\", s'il vous plait.")
    
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
        guess = input("Devinez: ")

        if guess.isalpha() and len(guess) == 1:
            if guess.lower() in guesses:
                print("")
                print("Cette lettre été choisit!")
            else: return guess.lower()

        print("")
        print("Réponse incorrect. Essayer encore!")

def display_board(solved,strikes,misses,kid):
    print("")
    print("Let Mot: " + solved)
    print("Résponses des Mauvaisses: " + misses)
    print("Résponses Restants: " + str(strikes))

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

def show_result(strikes,limit):
    if (strikes >= limit):
        print("Tu perds! Plus de chance la prochaine fois!")
    else:
        print("Tu gagnes! Toutes mes félicitations!")

def play_again():
    while True:
        decision = input("Veux-tu jouer à encore? (o/n): ")

        if decision == 'n' or decision == 'non':
            return False

        if decision == 'o' or decision == 'oui':
            return True

        else:
            print("Écrivez \"o\" ou \"n\", s'il vous plait.")
            print("")
def play():
    kid = friendly()
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle,guesses)

    strikes = 0
    misses = ""
    limit = 6

    display_board(solved,strikes,misses,kid)

    while solved != puzzle and strikes < limit:
        letter = get_guess(guesses)

        if letter not in puzzle:
            strikes += 1
            misses += letter + " "

        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved,strikes,misses,kid)

    show_result(strikes,limit)

#This code is the start of the actual game itself.

playing = True

hangman()

while playing:
    play()
    playing = play_again()

show_credits()
