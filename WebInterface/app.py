from flask import Flask , render_template
import os

app = Flask(__name__)

@app.route('/')
def HomePage():
    ContextVariables = {
        'Title':'Book Explorer'
    }
    return render_template("HomePage.html",**ContextVariables)

@app.route('/BookExplorer')
def BookExplorer():
    ContextVariables = {
        'Title':'Books Exploration'
    }
    return render_template("BookExplorer.html",**ContextVariables)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=bool(os.getenv("DEBUG_MODE")))