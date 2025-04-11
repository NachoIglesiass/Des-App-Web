from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Lista para almacenar productos
productos = []

# Ruta para la página principal con el formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para agregar un producto
@app.route('/agregar', methods=['POST'])
def agregar_producto():
    data = request.json
    producto = {
        'id': len(productos) + 1,
        'nombre': data['nombre'],
        'precio': data['precio']
    }
    productos.append(producto)
    return jsonify({'mensaje': 'Producto agregado', 'producto': producto})

# Ruta para listar productos en formato JSON
@app.route('/listar', methods=['GET'])
def listar_productos():
    return jsonify({'productos': productos})

if __name__ == '__main__':
    app.run(debug=True)
