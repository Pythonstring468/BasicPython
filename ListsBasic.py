# This program demonstrates a basic profenciency with lists in Python
# This program was written by Wesley Ordille

print("Lists")
FirstList = ["Apple", "Orange", "Banana"]
print (FirstList)
SecondList = ['Kiwi', 'Grapefruit', 'Tomato']
print (SecondList)
ThirdList = FirstList + SecondList
print (ThirdList)
print (type (ThirdList))

for num in [10,9,8,7,6,5,4,3,2,1] :
    print (num)
print ("Nothing happened when I counted down to one")

# Index of list
print (ThirdList[0])
print (ThirdList[5])

# Length of lists
print (len(ThirdList))
NumbersList = (1,2,3,5,7,11,13)
print (len(NumbersList))
for num in NumbersList :
    print (num)
print (NumbersList)

# Asking if something or value is in a list?

print (4 in NumbersList)
print (3 in NumbersList)
print (4 not in NumbersList)

# Average and Sum
print (sum (NumbersList))
print (sum (NumbersList) / len (NumbersList))

# Appending List
BlankList = list()
print (BlankList)
BlankList.append ("Paradox")
print (BlankList)
BlankList [0] = ("Grinch")
print (BlankList)

LongWinded = 'This is a very long list of strings     with no meaning'
print (LongWinded)
ShortWinded = LongWinded.split()
print (ShortWinded)
print (ShortWinded[4])
