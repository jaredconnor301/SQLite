import sqlite3

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

create_table()
enter_data()
