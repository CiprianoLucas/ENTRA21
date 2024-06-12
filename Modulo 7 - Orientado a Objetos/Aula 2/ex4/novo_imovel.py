from imovel import Imovel

class NovoImovel(Imovel):
    """Classe que representa os imóveis novos"""
    
    def __init__(self, endereco: str, preco: float, adicional: float):
        """Cria um imóvel novo

        Args:
            endereco (str): Endereco do imóvel
            preco (float): Valor do imóvel
            adicional (float): Adicional por ser imóvel novo
        """
        super().__init__(endereco, preco)
        self.adicional = adicional
        
    def __str__(self):
        return f"""Endereco: {self.endereco} || preco: R${self.preco:.2f} || adicional: R${self.adicional:.2f} || preco final: R${self.preco + self.adicional:.2f}"""
        
    @property
    def adicional(self):
        return self.__adicional
    
    @adicional.setter
    def adicional(self, adicional):
        self.__adicional = adicional
        
if __name__ == '__main__':
    meu_imovel = NovoImovel("rua D", 560, 100)
    print(meu_imovel)