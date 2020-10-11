# Written by Wesley Ordille
#If Else and elif

print ("Hello")

NewInput = input("Please enter an integer between 1 and 100 ")

try :
    IntInput = int(NewInput)

except :
    print ("Try again")

print ("You entered an Integer")

if IntInput > 50 :

    print ("You picked a high number")

elif IntInput > 25 :

   print ("You picked a medium number")

else :

    print ("You picked a low number")
