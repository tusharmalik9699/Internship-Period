import sqlite3

conn = sqlite3.connect('test.db')
print ('Opened database successfully')
tempobj  = {'name': 'charan'}
name = "chharan"
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (59, ?, 32, 'California', 20000.00 )", (tempobj["name"],))

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
#
# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
#
# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
cursor = conn.execute("SELECT id, name, address, age, salary from COMPANY")
for row in cursor:
    print('ID = ', row[0])
    print('NAME = ', row[1])

conn.commit()
print('Records created successfully')
conn.close()

