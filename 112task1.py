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
#flips a coin a number of time and records the outcome 
import random

i = int(input("please input the number of coin flips: "))

heads = 0
tails = 0

for int in range(i):
    flip = random.randint(0,1)
    if flip == 1:
        heads += 1
    else:
        tails += 1

print("total number of heads is {0}, total number of tails is {1}" .format(heads,tails))