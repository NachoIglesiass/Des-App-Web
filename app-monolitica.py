from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para almacenar productos
productos = []

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

# Ruta para listar los productos
@app.route('/listar', methods=['GET'])
def listar_productos():
    return jsonify({'productos': productos})

if __name__ == '__main__':
    app.run(debug=True)

""" curl -X POST -H "Content-Type: application/json" -d '{"nombre": "Zapatilla Nike", "precio": 100}' http://127.0.0.1:5000/agregar
para poder agregar producto, tuve un problema no podia hacer /agregar pero era por el post y se hace de esa manera 
"""

