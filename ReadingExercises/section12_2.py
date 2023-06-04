import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

#notice about the command:
# ends with \r\n\r\n is a sequence for the end of line and is the same as a blank line.
#A blank line at the end of a GET request is necessary according to the HTTP protocol
#Also ends with .encode() converting strings into bytes objects and back.


mysock.send(cmd)

# This loop receives the data in 512 character chunks from the socket and prints the data out until there no more data to read
#It determines that there is no more data to read when the len of the 512 character variable is zero
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

# At the end, it is necessary to close the socket.
mysock.close()
# Code: http://www.py4e.com/code3/socket1.py

#PS C:\Users\yazan\OneDrive\Desktop\Dr Chuck\PythonCoding\ReadingExercises> Python3 section12_2.py
#HTTP/1.1 200 OK
#Date: Sun, 04 Jun 2023 19:33:40 GMT
#Server: Apache/2.4.18 (Ubuntu)
#Last-Modified: Sat, 13 May 2017 11:22:22 GMT
#ETag: "a7-54f6609245537"
#Accept-Ranges: bytes
##Content-Length: 167
#Cache-Control: max-age=0, no-cache, no-store, must-revalidate
#Pragma: no-cache
#Expires: Wed, 11 Jan 1984 05:00:00 GMT
#Connection: close
#Content-Type: text/plain

#But soft what light through yonder window breaks
#It is the east and Juliet is the sun
#Arise fair sun and kill the envious moon
#Who is already sick and pale with grief
