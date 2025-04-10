from flask import Flask , render_template , redirect , url_for , request , session
import os

from source.GetBooks import RecommendedBooks

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

@app.route('/')
def HomePage():
    ContextVariables = {
        'Title':'Book Explorer'
    }

    session.clear()
    return render_template("HomePage.html",**ContextVariables)

@app.route('/BookExplorer',methods=['GET','POST'])
def BookExplorer():
    ContextVariables = {
        'Title':'Books Exploration'
    }

    session.setdefault('selections', 0)
    session.setdefault('last_selection', '')

    if request.method == 'GET':
        recommended_books = RecommendedBooks()
        return render_template("BookExplorer.html",**ContextVariables,Recommendations=recommended_books)
    
    if request.method == 'POST':
        if session['selections'] < 4:
            book_isbn = request.form.get('book_isbn')
            session['selections'] += 1
            session['last_selection'] = book_isbn

            recommended_books = RecommendedBooks(book_isbn)
            return redirect(url_for("BookExplorer"))

        else:
            return redirect(url_for("ShowRecommendations"))
        
@app.route('/Recommendations')
def ShowRecommendations():
    ContextVariables = {
        'Title':'Books Recommendations'
    }

    recommended_books = RecommendedBooks(session['last_selection'],False)
    return render_template("ShowRecommendations.html",**ContextVariables,Recommendations=recommended_books)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=bool(os.getenv("DEBUG_MODE")))