# The program will prompt for a URL, read the JSON data from that URL using urllib 
# and then parse and extract the comment counts from the JSON data, 
# compute the sum of the numbers in the file and enter the sum 

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1822596.json (Sum ends with 90)

# The data consists of a number of names and comment counts in JSON

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors -- These lines were copied from geojson.py
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sample_data = "http://py4e-data.dr-chuck.net/comments_42.json"
actual_data = "http://py4e-data.dr-chuck.net/comments_1822596.json"
ask = input("Enter location: ")
if len(ask)<1:
    ask = sample_data
# I'm sorry, I didn't want to copy paste the URL every time.    
elif ask=="Actual data":
    ask = actual_data

# I will use this variable to sum all the counts
total_comment_counts = 0

# this line enetered to matach the Sample Execution
print("Retrieving", ask)

# after this line, data will contain the URL as a single string that has the JSON object
data = urllib.request.urlopen(ask, context=ctx).read()

json_object = json.loads(data)
# this prints that there are two object
print('Retrieved:', len(data))
print('Total objects in JSON:', len(json_object))

comments_object = json_object["comments"]
# print(comments_object) #confirmed that object is successfully accessed.
# print("===========================================================") #line not needed after troubleshooting is completed.

for each in comments_object:
    # print( each["count"]) # this line was used for troubleshooting
    total_comment_counts += each["count"]
 
print("Sum:",total_comment_counts)