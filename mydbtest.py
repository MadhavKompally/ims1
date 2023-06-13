import sqlite3

conn = sqlite3.connect('mynewsql.db')

cur = conn.cursor()

#cur.execute('CREATE TABLE STUDENT(STD INT,SNAME VARCHAR(20))')
cur.execute('''INSERT INTO STUDENT VALUES(1,'KARTHICK')''')

conn.commit()