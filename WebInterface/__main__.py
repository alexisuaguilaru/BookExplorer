from flask import Flask , render_template , redirect , url_for , request , session
from flask_wtf.csrf import CSRFProtect
import os

from WebInterface import RecommendedBooks , BookSelectionForm , Run_gunicorn 

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
app.config.update(
    SESSION_COOKIE_SECURE = True,     
    SESSION_COOKIE_HTTPONLY = True,   
    SESSION_COOKIE_SAMESITE = 'Lax',  
    PERMANENT_SESSION_LIFETIME = 3600, 
)
csrf = CSRFProtect(app)


@app.route('/')
def HomePage():
    ContextVariables = {
        'Title':'Book Explorer'
    }

    session.clear()
    return render_template("HomePage.html",**ContextVariables)

@app.route('/BookExplorer',methods=['GET','POST'])
def BookExplorer():
    form_selection = BookSelectionForm()
    ContextVariables = {
        'Title':'Books Exploration',
        'FormSelections': form_selection,
    }

    session.setdefault('selections', 0)
    session.setdefault('last_selection', '')

    if request.method == 'GET':
        recommended_books = RecommendedBooks()
        return render_template("BookExplorer.html",**ContextVariables,Recommendations=recommended_books)
    
    if request.method == 'POST' and form_selection.validate_on_submit():
        if session['selections'] < 4:
            book_isbn = form_selection.book_isbn.data
            session['selections'] += 1
            session['last_selection'] = book_isbn

            recommended_books = RecommendedBooks(book_isbn)
            return render_template("BookExplorer.html", **ContextVariables,Recommendations=recommended_books)

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
    if (debug_mode:=int(os.getenv("DEBUG_MODE"))):
        app.run(host='0.0.0.0',port=5000,debug=debug_mode)
    else:
        Run_gunicorn()