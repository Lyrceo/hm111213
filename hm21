import sqlite3

connection = sqlite3.connect('shop.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS film (id INTEGER PRIMARY KEY,
title VARCHAR(100) UNIQUE NOT NULL,
genre VARCHAR(100) NOT NULL,
year DATE NOT NULL,
director VARCHAR(100));""")
cursor.execute("""CREATE TABLE IF NOT EXISTS
directors (id INTEGER PRIMARY KEY,
name VARCHAR(100) UNIQUE NOT NULL,
birth DATE NOT NULL);""")
cursor.execute("""INSERT INTO film (title, genre, year, director) VALUES ('Avatar', 'science fiction', '2009-12-18', 'James Cameron')""")
cursor.execute("""INSERT INTO film (title, genre, year, director) VALUES ('Inception', 'sci-fi', '2010-07-16', 'Christopher Nolan')""")
connection.commit()
connection.close()

connection = sqlite3.connect('shop.db')
cursor = connection.cursor()
cursor.execute("""SELECT * FROM film WHERE id = 1; """)
data = cursor.fetchall()
print(data)
connection.close()
