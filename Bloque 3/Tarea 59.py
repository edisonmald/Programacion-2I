# Diccionario de productos
tienda = {
    "martillo": 10.5,
    "clavos": 2.0,
    "cinta métrica": 4.75,
    "nivel": 8.0,
    "taladro": 45.99
}

# Mostrar productos
print("Productos disponibles:")
for producto, precio in tienda.items():
    print(producto.title(), ":", "$", precio)

# Buscar un producto
busqueda = input("\n¿Qué producto deseas buscar?: ").lower()

if busqueda in tienda:
    print(busqueda.title(), "cuesta", "$", tienda[busqueda])
else:
    print("Producto no encontrado.")
