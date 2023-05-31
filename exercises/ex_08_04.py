#8.4 Open the file romeo.txt and read it line by line. 
#For each line, split the line into a list of words using the split() method. 
#The program should build a list of words. 
#For each word on each line check to see if the word is already in the list and if not append it to the list. 
#When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.##
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

#Open the file romeo.txt and read it line by line. 
handle = open('romeo.txt')
romeowords = list()
#For each line, split the line into a list of words using the split() method.
for line in handle:
    linewords = line.split()
    #For each word on each line check to see if the word is already in the list and if not append it to the list.
    for word in linewords:
        if((word in romeowords)):
            continue;
        romeowords.append(word)
    
#sort and print the resulting words
romeowords.sort()
print(romeowords)

