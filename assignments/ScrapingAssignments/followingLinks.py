# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
# scan for a tag that is in a particular position relative to the first name in the list, 
# follow that link and repeat the process a number of times and report the last name you find.

# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 and Follow that link.
# Repeat this process 4 times.
# The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah


# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Jamaal.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. 
# The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: M

import urllib.request, urllib.parse, urllib.error
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Jamaal.html



url = 'http://py4e-data.dr-chuck.net/known_by_Jamaal.html'

number_to_repeat = 7
studentNumber = 18
current = 0

while current<number_to_repeat:
    current = current +1
    print(current)
    pageAsString = urllib.request.urlopen(url, context=ctx).read()
    urlBS4 = BeautifulSoup(pageAsString, 'html.parser')
    # Retrieve all of the anchor tags 
    tags = urlBS4('a')
    count = 0
    tagURL = ""
    friend = ""
    for tag in tags:
        # can I print all the names? yes I can using tag.text
        count = count+1
        # this condition block will allow me to get the student I'm looking for
        if count == studentNumber:
            friend = tag.text
            print("Friend:", friend)
            tagURL =tag.get('href')
        

    url = tagURL
    print("Url:", url)




    
    
    


