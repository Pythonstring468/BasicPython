# Basic Input Try and Accept by Wesley Ordille

print ("Please enter a number between one and ten.")
x = input("Enter a number ")
print (type(x))
try :
    y = int(x)
    y = y + 3
    print (y)
    print ("You entered an Interger")
except :
    print("Please enter an Integer")
