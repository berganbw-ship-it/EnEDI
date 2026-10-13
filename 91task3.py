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
springs = [] #creates list of spring constants

n = int(input("please input # of springs: ")) #asks how many springs are in the system

for i in range(n): #asks spring constants for each spring
    newSpringConstant = float(input(f"please input spring constant for spring {i+1}: "))
    springs.append(newSpringConstant) #adds each spring constant to the end of the list
#other inputs
type = int(input("please input 1 for series and 2 for parallel: "))
force = float(input("please input total force in newtons: "))
#calculations and print
if type == 1:
    ktotal = 1 / sum(1 / num for num in springs if num != 0) 
    print("total force = {0:.3f}" .format(ktotal))
    print("force = {0:.3f}" .format(force))
    xtotal = force/ktotal
    print("total stretcch = {0:.3f}" .format(xtotal))
elif type == 2:
    ktotal = sum(springs)
    print("total spring constant = {0:.3f}" .format(ktotal))
    perspringforce = force / len(springs)
    print("force per spring = {0:.3f}" .format(perspringforce))
    displacement = force / ktotal
    print("total stretch = {0:.3f}" .format(displacement))
else:
    print("invalid input")