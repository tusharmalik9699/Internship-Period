import sqlite3

conn = sqlite3.connect("mydatabase.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE albums(title text, artist text, release_date text, publisher text, media_type text)""")