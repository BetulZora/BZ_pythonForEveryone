#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
#If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

ask = input("Please enter a score between 0.0 and 1.0")
try:
    grade = float(ask)
except:
    print("Entry error. You have entered " + ask +". Please enter a valid numeric value.")
    print("Given the entry, grade cannot be determined")

if grade < 0.0:
    print("Entry Error, please enter a number between 0.0 and 1.0")
elif grade > 1.0:
    print("Entry Error, please enter a number between 0.0 and 1.0")
else :
    if grade >= 0.9 :
        lgrade = "A"
    elif grade >= 0.8 :
        lgrade = "B"
    elif grade >= 0.7 :
        lgrade = "C"
    elif grade >= 0.6 :
        lgrade = "D"
    else :
        lgrade = "F"

print(lgrade)