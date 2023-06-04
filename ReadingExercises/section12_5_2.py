# Use this program to read large non text files in chunks.
# this will help avoid crashing programs if the file gets too pig.

import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('coverName.jpg', 'wb')
size = 0
while True:
        #This line determines what the size of the block to be read is
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()
