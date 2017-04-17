import sqlite3
import time
import datetime
import random

#init
conn = sqlite3.connect('learning.db')
c = conn.cursor()

#Create Table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS plotstuff(unix REAL, timestamp TEXT, keyword TEXT, value REAL)')

#Insert Data
def enter_data():
    c.execute("INSERT INTO plotstuff VALUES ('2017:4:11', '4/1/2017', 'Testing','6')")

    #Save & Commit
    conn.commit()
    conn.close()

#Create Table that dynamically enters data
def dynamic_enter_data():
    unix = time.time()
    date = str((datetime.datetime.fromtimestamp(unix)).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = "Python"
    value = random.random()

    #Insert Data
    c.execute("INSERT INTO plotstuff(unix, timestamp, keyword, value) VALUES(?, ?, ?, ?)",
                (unix, date, keyword, value))

    #Save & Commit
    conn.commit()

#Reading data from data base
def read_data():
    c.execute("SELECT keyword, value, timestamp FROM plotstuff WHERE keyword='Python'")

    for row in c.fetchall():
        print(row)

#Updating and deleting file
def del_and_update():


    t = int(random.randint(1,100))
    c.execute("UPDATE plotstuff SET value = ? WHERE value = 't'", t)
    conn.commit()

    c.execute("DELETE FROM plotstuff WHERE ")
    conn.commit()

    c.execute("SELECT * FROM plotstuff")
    [print(row) for row in c.fetchall()]


#testing functions. Blocked out for nonuse
'''
create_table()
enter_data()
for i in range(10):
    dynamic_enter_data()
read_data()
del_and_update()
'''

c.close()
conn.close()
