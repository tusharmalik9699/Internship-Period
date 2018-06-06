from bottle import run, get, post, request, delete
import sqlite3


@post('/login')
def login():
    detail = {'id': request.json.get('id'), 'name': request.json.get('name'), 'password': request.json.get('password'), 'phone': request.json.get('phone'), 'dob': request.json.get('dob'), 'email': request.json.get('email')}
    conn = sqlite3.connect('test.db')

    conn.execute("INSERT INTO NEWUSERS (ID,NAME,PASSWORD,PHONE,DOB,EMAIL) \
          VALUES (?, ?, ?, ?,?,? )", (detail["id"], detail["name"], detail["password"], detail["phone"], detail["dob"], detail["email"]))

    conn.commit()
    conn.close()


run(reloader=True, debug=True)

