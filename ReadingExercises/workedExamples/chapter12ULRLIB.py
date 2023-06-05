import urllib.request, urllib.parse, urllib.error


#using urlopen() from the urllib library,
# we can treat any webpage as a file
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# this is another word frequency exercise
counts = dict()
for line in fhand:
    # need the .decode() to convert to local unicode
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) +1

print(counts)

