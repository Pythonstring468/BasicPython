# Dictionaries basics by Wesley Ordille
# Dictionaries unlike lists have both a value and a key, as opposed to just a value.

xDict = dict()
print (xDict) # Prints a blank dictionary

xDict ['apples']= 500
xDict ['bananas']= 250
xDict ['oranges']= 100
xDict ['kiwi']= 50

print (xDict)

xDict ['apples'] = xDict ['apples'] / 2

print (xDict['apples'])
print (type (xDict))

VegetableDict = {'Potatoes' : 55 , 'Carrots' : 200, 'Kale' : 1 }
print (VegetableDict)
print (type (VegetableDict))

# Errorous code cannot add dictionaries together. FruitandVegetableDict = xDict + VegetableDict
