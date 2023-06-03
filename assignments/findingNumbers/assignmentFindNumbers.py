# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.

#The basic outline of this problem is to read the file, look for integers using the re.findall(), 
# looking for a regular expression of '[0-9]+' 
# and then converting the extracted strings to integers 
# and summing up the integers.

import re

total = 0

fileName = input("Enter the file name desired:\n")
handle = open(fileName)

for line in handle:
    line= line.rstrip()
    # in this line, I am looking for any number anywhere in the line and storing in a list
    listNumbers = re.findall( "[0-9]+", line)
    # in this line, I'm going through the list and adding the numbers to total
    for num in listNumbers:
        total = total + int(num)
    
print(total)