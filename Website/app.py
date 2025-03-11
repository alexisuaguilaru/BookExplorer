from flask import Flask , render_template , redirect , url_for , request , session
import os

from GettingBooks import GetRandomBooks

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/explorer',methods=['GET','POST'])
def update_explorer():
    session.setdefault('selected_books',[])
    session.setdefault('selections', 0)
    
    if request.method == 'POST':
        if session['selections'] < 4:
            book_isbn = request.form.get('book_isbn')
            if book_isbn:
                session['selected_books'].append(book_isbn)
                session['selections'] += 1
                session.modified = True
            return redirect(url_for('update_explorer'))
        else:
            return redirect(url_for('show_recommendations'))
    
    query_books = GetRandomBooks()
    return render_template('explorer.html',QueryBooks=query_books)

@app.route('/reset-selection')
def reset_selection():
    session['selected_books'] = [] 
    session['selections'] = 0      
    return redirect(url_for('update_explorer')) 

@app.route('/recommendations')
def show_recommendations():
    recommended_books = GetRandomBooks() + GetRandomBooks()[:2]
    session.clear()
    return render_template('recommendations.html',Recommendations=recommended_books)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=bool(os.getenv("DEBUG_MODE")))