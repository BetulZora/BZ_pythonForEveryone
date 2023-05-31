#7.2 Write a program that prompts for a file name, 
#then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines 
#and compute the average of those values and produce an output as shown below. 
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt
# as the file name.

#Write a program that prompts for a file name,
fileName = input("Please enter the file name:")

#then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
count = 0
cumulativeTotal = 0.0
myFile = open(fileName)
for line in myFile:
    if line.startswith("X-DSPAM-Confidence:"):
    #Count these lines and extract the floating point values from each of the lines 
        count = count + 1
        colonposition = line.find(":")
        num = line[colonposition+1:]
        num = num.strip()
        num = float(num)
        cumulativeTotal = cumulativeTotal+num

aveAtEnd = cumulativeTotal / count
    
#and compute the average of those values and produce an output as shown below. 
print ("Average spam confidence:",aveAtEnd)