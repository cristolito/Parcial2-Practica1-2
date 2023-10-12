from nodo_producto import NodoProducto
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, producto):
        nuevo_nodo = NodoProducto(producto)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

        return producto

    def retirar(self, indice):
        if indice == 0:
            producto_retirado = self.cabeza.producto
            self.cabeza = self.cabeza.siguiente
            return producto_retirado

        actual = self.cabeza
        for i in range(indice - 1):
            if not actual.siguiente:
                return "Índice inválido. No se pudo retirar el producto."
            actual = actual.siguiente

        producto_retirado = actual.siguiente.producto
        actual.siguiente = actual.siguiente.siguiente
        return producto_retirado
    
    def retirar_uno(self, indice):
        actual = self.cabeza

        for i in range(indice):
            if not actual.siguiente:
                return "Índice inválido. No se pudo retirar el producto."
            actual = actual.siguiente
            
        actual.producto.cantidad -= 1
        if actual.producto.cantidad == 0:
            self.retirar(indice)

    def mostrar(self):
        productos = []
        actual = self.cabeza
        while actual:
            productos.append(actual.producto)
            actual = actual.siguiente
            
        return productos
