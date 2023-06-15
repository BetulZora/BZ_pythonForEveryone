# write a Python program that will prompt for a location, 
# contact a web service and retrieve JSON for the web service 
# and parse that data, and retrieve the first place_id from the JSON

# Make sure to check that your code is using the API endpoint as shown above. 
# You will get different results from the geojson and json endpoints 
# so make sure you are using the same end point as this autograder is using.

# This API uses the same parameter (address) as the Google API. 
# This API also has no rate limit so you can test as often as you like. 
# If you visit the URL with no parameters, you get "No address..." response.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = "http://py4e-data.dr-chuck.net/json?"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# To call the API, you need to include a key= parameter 
# and provide the address that you are requesting as the address= parameter 
# that is properly URL encoded using the urllib.parse.urlencode() function 

# You can test to see if your program is working with a location of 
# "South Federal University" which will have a place_id of "ChIJNeHD4p-540AR2Q0_ZjwmKJ8".

location = input("Enter location: ")
if len(location)<1:
    location = "South Federal University"
elif location == "Actual place":
    location = "University of London"

# I am adapting the parms dictionary given in geojson.py
#Turned out I misunderstood the instructions. I still dunno how I was supposed to get 42.
#parms = dict()
#parms['address'] = location
#url = serviceurl + urllib.parse.urlencode(parms)
#key = url
#print("key is", key)

newparms = dict()
newparms['key']= 42
newparms['address']=location
url = serviceurl + urllib.parse.urlencode(newparms)
print("Retreiving", url)  

# Recieving the response object
response_object = urllib.request.urlopen(url, context=ctx)
data = response_object.read().decode()
print('Retrieved', len(data), 'characters')
#print(data)

try:
    js = json.loads(data)
except:
    js = None

place_id = js["results"][0]['place_id']
# Needed this print statement in order to troubleshoot
# #print("FROM JS:", place_id)

print("Place id",place_id)





