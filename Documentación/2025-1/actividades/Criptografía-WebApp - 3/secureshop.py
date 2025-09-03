from flask import Flask, render_template, request, redirect, url_for
import requests  # Agregar esta importación

app = Flask(__name__)

# Datos de ejemplo
productos = [
    {'id': 1, 'nombre': 'Collar para Perro', 'precio': 10.0},
    {'id': 2, 'nombre': 'Juguete para Gato', 'precio': 5.0}
]

carrito = []

@app.route('/')
def tienda():
    return render_template('tienda.html', productos=productos)

@app.route('/agregar/<int:producto_id>')
def agregar_al_carrito(producto_id):
    producto = next((p for p in productos if p['id'] == producto_id), None)
    if producto:
        carrito.append(producto)
    return redirect(url_for('tienda'))

@app.route('/carrito')
def ver_carrito():
    total = sum(item['precio'] for item in carrito)
    return render_template('carrito.html', carrito=carrito, total=total)

@app.route('/inscribir', methods=['GET', 'POST'])
def inscribir_mascota():
    if request.method == 'POST':
        mascota_data = {
            'nombre': request.form['nombre'],
            'rut': request.form['rut'],
            'chip': request.form['chip'],
            'edad': request.form['edad'],
            'color': request.form['color'],
            'tipo': request.form['tipo']
        }
        # Enviar datos al web service
        response = requests.post('http://localhost:5001/registrar_mascota', json=mascota_data)
        return redirect(url_for('tienda'))
    return render_template('inscribir.html')

if __name__ == '__main__':
    app.run(debug=True, port=5003)