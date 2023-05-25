#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and smallest of the numbers. 
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
#Enter 7, 2, bob, 10, and 4 and match the output below.

ask = " "
min = None
max = None
something = ""
while something is not 'done':
    query = input("Please either enter an integer or the word done")
    try:
        ask = int(query)
    except:
        if query is 'done':
            break
        else:
            print("Invalid input")
    
    if min is None:
        min = ask

    if max is None:
        max = ask
    
    if ask < min:
        min = ask

    if ask > max:
        max = ask

print ("Maximum is", max)
print ("Minimum is", min)

