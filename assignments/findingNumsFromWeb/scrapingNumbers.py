# program will use urllib to read the HTML from the data files below, 
#and parse the data, extracting numbers 
#and compute the sum of the numbers in the file.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1822593.html (Sum ends with 61)

# Retrieve Data that look like this:
# <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
# <tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
# <tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

# You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.

import urllib.request, urllib.parse, urllib.error
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter the URL - ')
url = 'http://py4e-data.dr-chuck.net/comments_1822593.html'
#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1822593.html (Sum ends with 61)
urlInString = urllib.request.urlopen(url, context=ctx).read()
urlBS4 = BeautifulSoup(urlInString, 'html.parser')

# Retrieve all of the span tags from our webpage
tags = urlBS4('span') 

sum = 0
number = list()
# Adapted from class file
for tag in tags:
    #pull out the numbers from the tag and collect them in a list
    number = number + (tag.contents)
    #print(number) #I used this print statement while troubleshootin

# now sum up all the numbers in the list
for num in number:
    sum = sum + int(num)

print(sum)    


