import urllib.request, urllib.parse,urllib.error
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the URL - ')
# as example enter http://www.dr-chuck.com/
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a') # gets all of these tags

for tag in tags:
    #this chooses href attribute if there is one
    print(tag.get('href', None))

