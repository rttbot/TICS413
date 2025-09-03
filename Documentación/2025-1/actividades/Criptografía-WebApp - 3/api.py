from flask import Flask, request, jsonify
from flask_cors import CORS  # Agregar esta importación

app = Flask(__name__)
CORS(app)  # Habilitar CORS

mascotas = []

@app.route('/registrar_mascota', methods=['POST'])
def registrar_mascota():
    data = request.json
    mascotas.append(data)
    return jsonify({'message': 'Mascota registrada'}), 201

@app.route('/mascotas', methods=['GET'])
def get_mascotas():
    return jsonify(mascotas)

if __name__ == '__main__':
    app.run(debug=True, port=5001)