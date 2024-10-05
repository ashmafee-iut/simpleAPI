'''
test1.py

in-memory list (static db) to store the books' information
db can be only modified during runtime and that modification will not
change the static db created during initialization.

POSTMAN is used to check the HTTP connections and functoins

Rahat

'''

from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)


# it is a view function bsed on the route(URL) 
@app.route("/")
def home():
    return "<b>Hello, World!!!!!!!5556666---7777</b>"

@app.route("/<name>")
def dynamic(name):
    return f"<h1>Hello, {name} {name} {name} !!!!!!!5556666---7777</h1>"
  
# app.run(debug=True)


# in-memory list to store the books information 

books_list=[
     {
         'id':0,
         "author":"chinua achebe",
         "language":"english",
         "title":"things fall apart",
     },
     {
         'id': 1,
         "author": "hans christian andersen",
         "language": "danish",
         "title": "fairy tales",
     },
     {
         'id': 2,
         "author": "samuel beckett",
         "language": "french,english",
         "title": "molloy,malone dies,the unnamable,the triology",
     },
     {
         'id': 3,
         "author": "jorge luis borges",
         "language": "spanish",
         "title": "ficciones",
     },
     {
         'id': 4,
         "author": "giovanni boccaccio",
         "language": "italian",
         "title": "the decameron",
     },
     {
         'id': 5,
         "author": "emily bront",
         "language": "english",
         "title": "wuthering heights",
     },
 ]


@app.route('/books', methods=['GET', 'POST'] )
def books():

    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            'Nothing is found', 404
        
    
    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        id = books_list[-1]['id']+1

        new_obj = {
            'id': id,
            'author': new_author,
            'language': new_lang,
            'title': new_title    
        }
        books_list.append(new_obj)

        return jsonify(books_list), 201
    
    

@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):

    if request.method == 'GET':

        for book in books_list:
            if book['id'] == id:
                return jsonify(book)
            pass 
        
        
    
    if request.method == 'PUT':
        
        for book in books_list:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['language'] = request.form['language']
                book['title'] = request.form['title']
                updated_book = {
                    'id' : id,
                    'author' : book['author'],
                    'language' : book['language'],
                    'title' : book['title']
                }  
      
        return jsonify(updated_book)
    
    if request.method == 'DELETE':
        
        for index, book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
        
        return jsonify(books_list), 200




if __name__ == "__main__":
    app.run(debug=True)

