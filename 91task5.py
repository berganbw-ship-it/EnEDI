# Activity Python 1: Task 3
# File: ACT_Python_HeaderTemplate_TeamXXX_UCusername.py 
# Date:    9/24/26
# By:      Ben Bergan
# Section: Your Section
# Team:    Your Team Number
# 
# ELECTRONIC SIGNATURE
# Ben Bergan
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# plays rock paper scissors
import random
computer_choice = random.randint(1,3) #computer random choice
#player input
player_choice = int(input("please input 1 for rock, 2 for paper, and 3 for scissors"))
#computes and prints
if (computer_choice + player_choice) % 2 == 0 and player_choice + computer_choice != 4:
    print("tie game")
if (computer_choice + player_choice == 4):
    if computer_choice == 1:
        print("computer wins")
    elif computer_choice == 2:
        print("tie game")
    else:
        print("player wins")
if computer_choice + player_choice == 5:
    if computer_choice == 2:
        print("player wins")
    else:
        print("computer wins")
if computer_choice + player_choice == 3:
    if computer_choice == 1:
        print("computer wins")
    else:
        print("player wins")
