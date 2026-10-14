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
# computes if a pH is basic, neutral, or acidic
#inputs
pH = float(input("please input pH: "))
#calculate if pH is basic, neutral, or acidic
if pH < 7 and pH > 0:
    print("pH is acidic")
elif pH > 7 and pH < 14:
    print("pH is basic")
elif pH == 7:
    print("pH is neutral")
else:
    print("invalid input")