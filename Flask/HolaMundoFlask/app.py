from flask import Flask, request, render_template, url_for, jsonify
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)


# http://localhost:5000/
@app.route('/')
def inicio():
    # app.logger.debug('Mensaje a nivel debug')
    app.logger.info(f'Entramos al path {request.path}')
    # app.logger.warn('Mensaje a nivel warning')
    # app.logger.error('Mensaje a nivel error')
    return 'Hola mundo desde Flask.'


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre}'


@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tu edad es  {edad}'


@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)


@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('inicio'))


@app.route('/salir')
def salir():
    return abort(404)


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return (render_template('error404.html', error=error), 404)


# REST
@app.route('/api/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_json(nombre):
    valores = {
        'nombre': nombre,
        'metodo_http': request.method
    }
    return jsonify(valores)
