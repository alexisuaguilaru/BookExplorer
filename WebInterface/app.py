from flask import Flask , render_template , redirect , url_for , request
import os

from source.GetBooks import RecommendedBooks

app = Flask(__name__)

@app.route('/')
def HomePage():
    ContextVariables = {
        'Title':'Book Explorer'
    }
    return render_template("HomePage.html",**ContextVariables)

@app.route('/BookExplorer',methods=['GET','POST'])
def BookExplorer():
    ContextVariables = {
        'Title':'Books Exploration'
    }

    if request.method == 'GET':
        recommended_books = RecommendedBooks()
        return render_template("BookExplorer.html",**ContextVariables,Recommendations=recommended_books)
    
    if request.method == 'POST':
        book_isbn = request.form.get('book_isbn')
        recommended_books = RecommendedBooks(book_isbn)
        return redirect(url_for("BookExplorer"))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=bool(os.getenv("DEBUG_MODE")))