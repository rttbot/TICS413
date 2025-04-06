from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

usuarios = {
    'admin': 'colocolo'
}

@app.route('/')  # Agregar esta ruta
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        if usuario in usuarios and usuarios[usuario] == password:
            return redirect(url_for('estadisticas'))
        else:
            return 'Credenciales incorrectas'
    return render_template('login.html')

@app.route('/estadisticas')
def estadisticas():
    # Obtener datos de la API
    response = requests.get('http://localhost:5001/mascotas')
    mascotas = response.json()
    return render_template('estadisticas.html', mascotas=mascotas)

if __name__ == '__main__':
    app.run(debug=True, port=5002)