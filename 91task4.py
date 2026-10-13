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
temp = float(input("please input temperature of reactor: "))
pressure = float(input("please input pressure inside reactor: "))

temp = (temp-325) / 30
pressure = (pressure-0.085) / 0.015

if temp >= pressure:
    important = temp
else:
    important = pressure

if important <= 0.2:
    print("reactor is normal")
elif important > 0.2 and important <= 0.4:
    print("reactor is moderate")
elif important > 0.4 and important <= 0.6:
    print("reactor is severe")
elif important > 0.6 and important <= 0.8:
    print("reactor is very severe")
else:
    print ("reactor is melting down")