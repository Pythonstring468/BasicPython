# This program was written by Wesley Ordille
# For the purposes of showing my skills at programming in order to get a job.


HW = "Hello World"
print ("Hello World")
print (HW)
print ("123")
# Adding of strings together
# Also known as string concatenation
Numbers = "123"
print (Numbers)
Concatenation = HW + Numbers
print (Concatenation)

# Converting Strings to Ints and visa versa
IntNumbers = int (Numbers)
print (IntNumbers)
print (type (IntNumbers))
strNumbers = str (IntNumbers)
print (type (strNumbers))
print (strNumbers)
# Splitting strings
PartofStringOne = Concatenation [0 : 11]
print (PartofStringOne)

PartofStringTwo = Concatenation [11 : 14]
print (PartofStringTwo)
print (Concatenation)
# Finding within strings

EndLetter = Concatenation.find("d")
print(EndLetter)
EndNum = Concatenation.find("3")
print(EndNum)
FindOne = Concatenation[0 : EndLetter+1]
print (FindOne)
FindTwo = Concatenation[EndLetter + 1 : EndNum+1]
print (FindTwo)
# This program was written by Wesley Ordille and is his very first python program.
# The purpose of this program was to increase my skills in Python and
# hopefully get a job using Python.
