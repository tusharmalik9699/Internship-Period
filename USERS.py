import sqlite3

conn = sqlite3.connect('test.db')
print ('Opened database successfully')
conn.execute('''CREATE TABLE USERS
          (ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL,
           PASSWORD       VARCHAR(25) NOT NULL,
           PHONE          INT     NOT NULL,
           DOB            DATE,
           EMAIL          VARCHAR(25))''')
print ('Table created successfully')

conn.close()