'''
test3.py

TO BE PREPARED....................

MYSQL db is used to store the books' information.

DataGrip (JetBrains) is used to visualize data in tabulate format
and manipulate the table

POSTMAN is used to check the HTTP connections and functoins

Rahat 

'''

from flask import Flask, request, jsonify
import json
import pymysql

app = Flask(__name__)


# it is a view function bsed on the route(URL) 
@app.route("/")
def home():
    return "<b>Hello, World!!!!!!!5556666---7777</b>"

@app.route("/<name>")
def dynamic(name):
    return f"<h1>Hello, {name} {name} {name} !!!!!!!5556666---7777</h1>"
  

def db_connection():
    conn = None

    try:
        conn = pymysql.connect(
                    host = 'sql12.freesqldatabase.com',
                    database = 'sql12735244',
                    user = 'sql12735244',
                    password = '4B33QduBEM',
                    charset = 'utf8mb4',
                    cursorclass = pymysql.cursors.DictCursor,
                    port =  3306
               )

    except pymysql.Error as e:
        print(e) 
    return conn 



@app.route('/books', methods=['GET', 'POST'] )
def books():

    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * from book") # simply execute the cursor, not return any query result
        books = [
            # instead of array, fetchall() returns a dictionary
            # dict(id=row[0], author=row[1], language=row[2], title=row[3]) for row in cursor.fetchall()
            dict(id=row['id'], author=row['author'], language=row['language'], title=row['title']) for row in cursor.fetchall()
        ]
        conn.close() 
        if books is not None:
            return jsonify(books)
        
    
    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        sql = """ INSERT INTO book (author, language, title) VALUES (%s,%s,%s)"""  # instead of ?, %s is placeholder

        cursor.execute(sql, (new_author, new_lang, new_title))

        conn.commit() 
        new_id = cursor.lastrowid

        return f"Book with ID: {new_id} is created successfully.", 201
    

@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    
    conn = db_connection()
    cursor = conn.cursor()

    book = None

    if request.method == 'GET':
        cursor.execute("SELECT * from book WHERE id=%s", (id,))
        rows = cursor.fetchall()

        for r in rows:
            book = r
        
        if book is not None:
            return jsonify(book), 200
        else:
            return "Something is wrong", 404
    
    if request.method == 'PUT':
        
        sql = """
            UPDATE book 
            SET title=%s,
                author=%s,
                language=%s
            WHERE id=%s
            """

        print(request.form)
        
        # author = request.form['author']
        # language = request.form['language']
        # title = request.form['title']
        title = request.form.get('title')
        author = request.form.get('author')
        language = request.form.get('language')

        updated_book = {
            'id' : id,
            'author' : author,
            'language' : language,
            'title' : title
        }

        cursor.execute(sql,(title, author, language, id))
        conn.commit()

        return jsonify(updated_book)
    
    if request.method == 'DELETE':
        sql = """ DELETE FROM book WHERE id=%s"""

        cursor.execute(sql,(id,))
        conn.commit()
        
        return f"The book with the id:{id} has been deleted.", 200




if __name__ == "__main__":
    app.run(debug=True)

