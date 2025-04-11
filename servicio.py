# servicio.py - Procesa los datos antes de enviarlos o guardarlos
from datos import agregar_producto_db, obtener_productos_db

def agregar_producto(nombre, precio):
    producto = {
        'id': len(obtener_productos_db()) + 1,
        'nombre': nombre,
        'precio': precio
    }
    agregar_producto_db(producto)
    return producto

def listar_productos():
    return obtener_productos_db()
