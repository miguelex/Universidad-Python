from flask import Flask

app = Flask(__name__)

#http://localhost:5000/
@app.route('/')
def inicio():
    return 'Hola mundo desde Flask.'