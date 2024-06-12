from imovel import Imovel

class VelhoImovel(Imovel):
    """Classe que representa os imóveis velhos"""
    
    def __init__(self, endereco: str, preco: float, desconto: float):
        """Cria um imóvel velho

        Args:
            endereco (str): Endereco do imóvel
            preco (float): Valor do imóvel
            desconto (float): desconto por ser imóvel velho
        """
        super().__init__(endereco, preco)
        self.desconto = desconto
        
    def __str__(self):
        return f"""Endereco: {self.endereco} || preco: R${self.preco:.2f} || desconto: R${self.desconto:.2f} || preco final: R${self.preco - self.desconto:.2f}"""
        
    @property
    def desconto(self):
        return self.__desconto
    
    @desconto.setter
    def desconto(self, desconto):
        self.__desconto = desconto
        
if __name__ == '__main__':
    meu_imovel = VelhoImovel("rua D", 560, 100)
    print(meu_imovel)