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
# computes if an alloy of tin and lead is all, partially, or not at all molten
import math

temp = float(input("please input temp (C): "))
tin = float(input("please input percent tin as a whole #: "))

if temp <= 183:
    print("both solid")
else:
    if tin > 62:
        if temp <= (49/38 * (tin-62)) + 183:
            print("solid tin, molten lead")
        else: 
            print("both molten")
    else:
        if temp <= (-144/62 * (tin)) + 327:
            print("molten lead, solid tin")
        else:
            print("both molten")