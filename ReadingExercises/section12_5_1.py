#Open the URL and use read to download the entire contents of
#the document into a string variable (img) then write that information to a local
#file as follows:

import urllib.request, urllib.parse, urllib.error

# Recall the .read() records the entire document as a single string
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
# the 'wb' parameter allows us to write to the handle
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()