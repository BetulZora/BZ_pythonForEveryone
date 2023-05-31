#7.1 Write a program that prompts for a file name, 
#then opens that file and reads through the file, 
# and print the contents of the file in upper case. 
#Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

#Write a program that prompts for a file name
fileName = input("Enter the name of the file: ")
# opens that file
myfile = open(fileName)
# and reads through the file, 
# and print the contents of the file in upper case. 
fileUpperCase = myfile.read().upper()
print(fileUpperCase)


