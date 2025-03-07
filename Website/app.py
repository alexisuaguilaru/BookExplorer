from flask import Flask , render_template , request , redirect , url_for
import os

from GettingBooks import GetRandomBooks

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/explorer',methods=['GET','POST'])
def update_explorer():
    global selected_books
    global selections
    if request.method == 'GET':
        selected_books = []
        selections = 1
        query_books = GetRandomBooks()
        return render_template('explorer.html',QueryBooks=query_books)
    else:
        if selections < 5:
            book_isbn = request.form.get('book_isbn')
            selected_books.append(book_isbn)
            selections += 1
            query_books = GetRandomBooks()
            return render_template('explorer.html',QueryBooks=query_books)
        else:
            book_isbn = request.form.get('book_isbn')
            selected_books.append(book_isbn)
            return redirect(url_for('show_recommendations'))

#@app.route('/recommendations')
#def show_recommendations():
#    recommended_books = GetRandomBooks() + GetRandomBooks()[:2]
#    return render_template('recommendations.html',Recommendations=recommended_books)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=bool(os.getenv("DEBUG_MODE")))