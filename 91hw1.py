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
# computes hooke's law
import math
resistors = [] #creates list of spring constants

n = int(input("please input # of resistors: ")) #asks how many springs are in the system

for i in range(n): #asks spring constants for each spring
    newResistor = float(input(f"please input spring constant for spring {i+1}: "))
    resistors.append(newResistor) #adds each resistance to the end of the list
#other inputs
type = int(input("please input 1 for series and 2 for parallel: "))
#calculations and print
if type == 1:
    rtotal = sum(resistors)
    print("total resistance = {0:.3f}" .format(rtotal))
elif type == 2:
    rtotal = 1 / sum(1 / i for i in resistors if i != 0)
    print("total resistance = {0:.3f}" .format(rtotal))
else:
    print("invalid input")