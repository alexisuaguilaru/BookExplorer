from flask import Flask , render_template
import os

from GettingBooks import GetRandomBooks

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/explorer')
def explorer():
    query_books = GetRandomBooks()
    return render_template('explorer.html',QueryBooks=query_books)

@app.route('/explorer',methods=['POST'])
def update_explorer():
    query_books = GetRandomBooks()
    return render_template('explorer.html',QueryBooks=query_books)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=bool(os.getenv("DEBUG_MODE")))