from flask import Flask, request

app = Flask(__name__)

#http://localhost:5000/
@app.route('/')
def inicio():
    #app.logger.debug('Mensaje a nivel debug')
    app.logger.info(f'Entramso al path {request.path}')
    #app.logger.warn('Mensaje a nivel warning')
    #app.logger.error('Mensaje a nivel error')
    return 'Hola mundo desde Flask.'

@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre}'

@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tu edad es  {edad}'