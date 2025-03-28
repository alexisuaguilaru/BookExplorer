from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def HomePage():
    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=bool(os.getenv("DEBUG_MODE")))