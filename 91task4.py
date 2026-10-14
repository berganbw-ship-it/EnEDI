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
# computes state of reactor
import math
#inputs
temp = float(input("please input temperature of reactor: "))
pressure = float(input("please input pressure inside reactor: "))
#temp condition calculations
if temp <= 325:
    tempcondition = 1
elif temp > 325 and temp <= 335:
    tempcondition = 2
elif temp > 335 and temp <= 345:
    tempcondition = 3
elif temp > 345 and temp <= 355:
    tempcondition = 4
else:
    tempcondition = 5
#pressure condition calcs
if pressure <= 0.085:
    pressurecondition = 1
elif pressure > 0.085 and pressure <= 0.09:
    pressurecondition = 2
elif pressure > 0.09 and pressure <= 0.095:
    pressurecondition = 3
elif pressure > 0.095 and pressure <= 0.1:
    pressurecondition = 4
else:
    pressurecondition = 5
#finds which is worse
if tempcondition >= pressurecondition:
    important = tempcondition
else:
    important = pressurecondition
#prints the worse one
if important == 1:
    print("reactor is normal")
elif important == 2:
    print("reactor is moderate")
elif important == 3:
    print("reactor is severe")
elif important == 4:
    print("reactor is very severe")
else:
    print ("reactor is melting down")