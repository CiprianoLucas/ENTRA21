from __future__ import annotations
from abc import ABC

class Imovel(ABC):
    """Classe que representa imóveis"""
    
    def __init__(self, endereco: str, preco: float):
        """Args:
            endereco (str): Endereco do imóvel
            preco (float): Valor do imóvel
        """
        self.endereco = endereco
        self.preco = preco
        
    def __str__(self):
        return f"Endereco: {self.endereco}   ||   preco: R${self.preco:.2f}"
        
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        self.__preco = preco
        
if __name__ == '__main__':
    meu_imovel = Imovel("rua D", 560.00)
    print(meu_imovel)