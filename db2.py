import pymysql
import pymysql.cursors

conn = pymysql.connect(
    host = 'sql12.freesqldatabase.com',
    database = 'sql12735244',
    user = 'sql12735244',
    password = '4B33QduBEM',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor,
    port =  3306
)

cursor = conn.cursor()

sql_query_drop = """ DROP TABLE book """

sql_query_create = """
    
    create table book(
        id integer AUTO_INCREMENT PRIMARY KEY,
        author text NOT NULL,
        language text NOT NULL,
        title text NOT NULL
    )
"""

sql_query_alter = """ ALTER TABLE book MODIFY COLUMN id INT AUTO_INCREMENT PRIMARY KEY """


cursor.execute(sql_query_drop)
cursor.execute(sql_query_create)

conn.close()    
