from flask import Flask, render_template #estamos importando la libreria flask para poder construir nuestra aplicacion
import requests

app = Flask(__name__)

@app.route('/') #cremos nuestra ruta
def index(): #creamos una funcion que se va llamar index.
    #retornar un string a nuestro navegador
    return "hola xd"

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/personaje')
def personaje():

    api_url = 'https://rickandmortyapi.com/api/character/1'

    respuesta_api = requests.get(api_url).json()

    nombre = respuesta_api['name']
    estado = respuesta_api['status']
    url_imagen = respuesta_api['image']

    return render_template('personaje.html', nombre_html = nombre, estado_html = estado, url_imagen_html = url_imagen)








if __name__ == '__main__':
    app.run (debug=True)