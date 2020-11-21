# Regular expressions
# Written by Wesley Ordille
# As I understand regular expressions are shortcut keys like control + c to copy and control + v to paste.

import re # This imports regular expressions, won't work without this line of code.

LargeTextBlock = "The quick brown fox jumps over the lazy dog"

print (LargeTextBlock)

fido = re.findall('d([^ ]*)',LargeTextBlock) #prints dog if done correctly
print (fido) # prints og skipping the d hmmmm needs work.

fido2 = re.findall('y+',LargeTextBlock) #this only prints the y. Regular expressions are giving me trouble.
print (fido2)

fido3 = re.findall('^d',LargeTextBlock) # returns nothing I am stumped for now.
print (fido3)

fido4 = re.findall('^d.a+g' ,LargeTextBlock)
print (fido4)

fido5 = re.findall('dog' ,LargeTextBlock)
print (fido5) # well I got the correct answer, not sure if this involved regular expressions.


fido6 = re.findall('\S+o\S+', LargeTextBlock)
print (fido6) # now I get all words that have an o in them. brown, fox, and dog.

fido7 = re.findall('\S+d\S+', LargeTextBlock)
print (fido7) # blank again I give up for now. 

print ("Regular Expressions finished written by Wesley Ordille")
