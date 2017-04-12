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

#create_table()
#enter_data()

for i in range(10):
    dynamic_enter_data()
    time.sleep(1)


c.close()
conn.close()
