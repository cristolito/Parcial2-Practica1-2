from nodo import Nodo
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_elemento(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def get_lista(self):
        actual = self.cabeza
        lista = []
        while actual:
            lista.append(actual.valor)
            actual = actual.siguiente
        return lista
