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
# computes if a triangle is a possible triangle
#inputs
s1 = float(input("please input side 1 length: "))
s2 = float(input("please input side 2 length: "))
s3 = float(input("please input side 3 length: "))
#finds longest side
hypotenuse = max(s1,s2,s3)
#determines if triangle is real
if hypotenuse < (s1+s2+s3-hypotenuse):
    print("the triangle is real")
    if s1 == s2 == s3: #determines if the triangle is equilateral
        print("the triangle is equilateral")
    elif s1 == s2 or s2 == s3 or s3 == s1: #determines if the triangle is isosceles
        print("the triangle is isosceles")
    else: #determines if the triangle is scalene
        print("the triangle is scalene")
else:
    print("the triangle doesn't exist")