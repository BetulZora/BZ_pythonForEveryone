# The program will prompt for a URL, read the XML data from that URL using urllib 
# and then parse and extract the comment counts from the XML data, 
# compute the sum of the numbers in the file.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1822595.xml (Sum ends with 87)

# look through all the <comment> tags and find the <count> values sum the numbers.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

hand = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1822595.xml", context=ctx)
data = hand.read()
# print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

myXML = tree.findall('comments/comment')

sum = 0

for comment in myXML:
    sum = sum + int(comment.find('count').text)
    
print(sum)

