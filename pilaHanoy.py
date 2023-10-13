

class NodoPila:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cabeza = None

    def push(self, valor):
        nuevo_nodo = NodoPila(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def pop(self):
        if self.cabeza is None:
            return None
        valor = self.cabeza.valor
        self.cabeza = self.cabeza.siguiente
        return valor

    def __str__(self):
        valores = []
        actual = self.cabeza
        while actual:
            valores.append(str(actual.valor))
            actual = actual.siguiente
        return " -> ".join(valores)



