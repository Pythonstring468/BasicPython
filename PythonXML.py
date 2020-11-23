# Written by Wesley Ordille

print ("XML and Python example written by Wesley Ordille")

import xml.etree.ElementTree as ET

x = '''
<cat>
 <name>Garfield</name>
 <phone type="intl">
    +1 800 222 1111
 </phone>
 <email hide="no"/> # this line gave me trouble
</cat>'''

y = ET.fromstring(x)
print('Name:', y.find('name').text)
print('Attr:', y.find('email').get('hide'))
 #had some trouble here on line 13, I orignally had <email hide="no"</> gave me a traceback took five minutes to find the error.
