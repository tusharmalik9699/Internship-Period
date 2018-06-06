import sqlite3

conn = sqlite3.connect('test.db')
print('Opened database successfully')

cursor = conn.execute("SELECT ID,NAME,PASSWORD,PHONE,DOB,EMAIL from NEWUSERS")
for row in cursor:
   print ('ID = ', row[0])
   print ('NAME = ', row[1])
   print ('PASSWORD= ', row[2])
   print ('PHONE = ', row[3])
   print ('DOB = ', row[4])
   print ('EMAIL = ', row[5], "\n")

print('Operation done successfully')
conn.close()