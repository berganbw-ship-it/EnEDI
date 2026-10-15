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
#angle input
type = int(input("please input the units of the angle, 0 for rad 1 for deg: "))
theta = float(input("please input your angle: "))

if type == 1:
    theta = theta * math.pi / 180

if theta <= (math.pi / 2) and theta > 0:
    theta = (math.sin(theta)) ** 2 / (1 - ((math.sin(theta)) ** 2))
    print("y(theta) = {0:.3f}".format(theta))
elif theta <= math.pi and theta > (math.pi) / 2:
    theta = math.sqrt(1 - (math.cos(theta)) ** 4)
    print("y(theta) = {0:.3f}".format(theta))
elif theta <= (math.pi * 1.5) and theta > math.pi:
    theta = - (math.sqrt(1 + (math.tan(theta) ** 2))) / math.tan(theta)
    print("y(theta) = {0:.3f}".format(theta))
elif theta <= (math.pi *2) and theta > (math.pi * 1.5):
    theta = -1 / (math.sqrt(1 - (math.sin(theta)) ** 2))
    print("y(theta) = {0:.3f}".format(theta))
else:
    print("invalid input")