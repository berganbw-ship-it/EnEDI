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
# computes owed taxes
import math
#input
income = float(input("Please input earned income ($): "))
#calculates owed taxes
if income <= 50000:
    owed = income * 0.01
elif income > 50000 and income <= 75000:
    owed = income - 50000
    owed = (owed * 0.02) + 500
elif income > 75000 and income <= 100000:
    owed = income - 75000
    owed = (owed*0.03) + 1000
elif income > 100000 and income <= 250000:
    owed = income - 100000
    owed = (owed*0.04) + 1750
elif income > 250000 and income <= 500000:
    owed = income - 2500000
    owed = (owed*0.05) + 7750
elif income > 500000:
    owed = income - 500000
    owed = (owed*0.06) + 32750
#prints owed taxes
print("taxes owed = {0:.2f}" .format(owed))