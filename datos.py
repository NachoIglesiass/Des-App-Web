# datos.py - Maneja el almacenamiento de productos
productos = []

def agregar_producto_db(producto):
    productos.append(producto)

def obtener_productos_db():
    return productos
