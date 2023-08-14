import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

#GOAL: This application will read the mailbox data (mbox.txt) 
# and count the number of email messages per organization (i.e. domain name of the email address) 
# using a database with the following schema to maintain the counts.

cur.execute('DROP TABLE IF EXISTS Counts') 

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname)<1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
	if not line.startswith('From: '): continue
	pieces = line.split('@')
	domain = pieces[1]
	cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,)) # using the '?' prevents sql injection. It is a placeholder.
	row = cur.fetchone() # FETCH ONE gets the result of the execute function like the ResultSet
	if row is None:
		cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (domain,))
	else:
		cur.execute('UPDATE Counts SET count = count +1 WHERE org = ?', (domain,))
	

conn.commit()

#https://www.sqlite.ord/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    
cur.close()