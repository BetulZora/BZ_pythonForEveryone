#9.4 Write a program to read through the mbox-short.txt 
#and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines 
#and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address 
#to a count of the number of times they appear in the file.
# After the dictionary is produced, 
#the program reads through the dictionary using a maximum loop to find the most prolific committer.

#read through the mbox-short.txt 
handle = open("mbox-short.txt")

senderEmails = dict()

#The program looks for 'From ' lines 
for line in handle :
    if line.startswith('From ') :
        #takes the second word of those lines as the person who sent the mail.
        words = line.split()
        sendersAddress = words[1]
        #Use a Python dictionary that maps the sender's mail address 
        #to a count of the number of times they appear in the file.
        senderEmails[sendersAddress] = senderEmails.get(sendersAddress, 0) +1

#reads through the dictionary using a maximum loop to find the most prolific committer
maxSender = ""
maxCount = 0
for key in senderEmails:
    if senderEmails[key] > maxCount:
        maxSender = key
        maxCount = senderEmails[key]

print (maxSender, maxCount)

