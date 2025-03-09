from abc import ABC, abstractmethod

class Pedido(ABC):
    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.itens = itens

    @abstractmethod
    def calcular_total(self):
        pass