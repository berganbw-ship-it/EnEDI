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
# calculates fibbonachi sequence starting at f0
import math
x = int(input("please input your number: "))

if x < 1:
    while x <1:
        x = int(input("please input a positive value for x: "))
term1 = 0
term2 = 1
termx = 1
print(term1)
print(term2)
for i in range(x-2):
    termx = term1+term2
    term1 = term2
    term2 = termx
    print(termx)


