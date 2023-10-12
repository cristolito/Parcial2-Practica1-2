from lista_enlazada import ListaEnlazada

class SuperMercado:
    def __init__(self):
        self.productos_disponibles = ListaEnlazada()
        self.productos_retirados = ListaEnlazada()

    def agregar_producto(self, producto):
        return f"Producto agregado: {self.productos_disponibles.agregar(producto)}"

    def retirar_producto(self, indice):
        producto_retirado = self.productos_disponibles.retirar(indice)
        if isinstance(producto_retirado, str):
            return producto_retirado
        self.productos_retirados.agregar(producto_retirado)
        return f"Producto retirado: {producto_retirado.nombre}"
    
    def retirar_uno(self, indice):
        self.productos_disponibles.retirar_uno(indice)

    def mostrar_productos_disponibles(self):
        return self.productos_disponibles.mostrar()

    def mostrar_productos_retirados(self): 
        return self.productos_retirados.mostrar()