import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS EMAILCNT')

cur.execute('CREATE TABLE EMAILCNT(org text, count integer) ')


#file read
fname = input('Enter file name :')
fhandle = open(fname)

for line in fhandle:
    if not line.startswith('From:'): continue
    pieces = line.split()
    temp = pieces[1].split('@')
    org = temp[1]
    cur.execute('SELECT count FROM EMAILCNT WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO EMAILCNT(org, count) VALUES(?, 1) ', (org,))
    else:
        cur.execute('UPDATE EMAILCNT SET count = count + 1 WHERE org = ?', (org,))
    conn.commit()

sqlstr = 'SELECT * FROM EMAILCNT ORDER BY count'

# print(cur.execute(sqlstr))
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])



cur.close()
