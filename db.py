import sqlite3

conn = sqlite3.connect("books.sqlite")

cursor = conn.cursor()



sql_query = """
    create table book(
        id integer PRIMARY KEY,
        author text NOT NULL,
        language text NOT NULL,
        title text NOT NULL
    )
"""

# integer PRIMARY KEY is an alias of rowID that is uniquely handled by SQLite
# So, each time a new row is created, ID is copied form rowID


cursor.execute(sql_query)