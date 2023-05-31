ipsum = open('ipsum.txt','r')
count = 0
for line in ipsum:
    count = count+1
    if count ==4:
        print(line)
print(count)

