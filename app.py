# app.py - Maneja las rutas y respuestas HTTP
from flask import Flask, request, jsonify
from servicio import agregar_producto, listar_productos

app = Flask(__name__)

@app.route('/agregar', methods=['POST'])
def agregar():
    data = request.json
    producto = agregar_producto(data['nombre'], data['precio'])
    return jsonify({'mensaje': 'Producto agregado', 'producto': producto})

@app.route('/listar', methods=['GET'])
def listar():
    return jsonify({'productos': listar_productos()})

if __name__ == '__main__':
    app.run(debug=True)
