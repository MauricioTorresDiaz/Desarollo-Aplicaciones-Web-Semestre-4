from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Bienvenido a mi aplicación Flask!"

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'Bienvenido, {nombre}!'  # Muestra el nombre ingresado en la URL

if __name__ == '__main__':
    app.run(debug=True)

