# Python and JSON basic examples written by Wesley Ordille

print ("JSON and python written by Wesley Ordille text editor used Atom")

import json

# JSON uses curly brackets
DataBlock = '''{
 "name" : "Lassie"

}'''

VetClinc = json.loads(DataBlock)
print('Name:', VetClinc["name"])
print("As you can see JSON has quite a few differences from XML")
