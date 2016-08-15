import sqlite3 as lite
import sys

facts = (
    (1, 'Markus', 25),
    (2, 'David', 27),
    (3, 'Nagon', 23)
    )

con = lite.connect("nao.db")

with con:

    db = con.cursor()
    db.row_factory = lite.Row
    
    db.execute("drop table if exists info")
    db.execute("create table info (place int, name text, age int)")
    db.executemany("insert into info values(?, ?, ?)", facts)
    # Print out order
    cursor = db.execute("select * from info order by age")
    for row in cursor:
        print (dict(row))

