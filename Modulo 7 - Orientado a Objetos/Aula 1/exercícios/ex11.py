class Produto:
    """Produto representa um produto"""
    
    def __init__(self, nome: str, preco: float, estoque: int):
        """cria um produto com seu valor e estoque

        Args:
            nome (str): nome do Produto
            preco (float): preço de venda do produto
            estoque (int): quantidade em estoque do produto
        """
        
        self.nome = nome
        self.preco = preco
        self.__estoque = estoque
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
        
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco: float):
        self.__preco = preco
        
    def vender(self, quantidade: int):
        """Informar quantos do produto irá vender e atualiza o estoque

        Args:
            quantidade (int): quantidades para vender
        """
        if self.__estoque < quantidade:
            raise ValueError("Estoque insuficiente")
        else:
            self.__estoque -= quantidade
            
    def comprar(self, quantidade: int):
        """informa quantos produtos irá comprar e atualiza o estoque

        Args:
            quantidade (int): Quantidades para comprar
        """
        
        self.__estoque += quantidade
        
    def valor_total(self) -> float:
        """Retorna o valor total multiplicando o estoque pelo valor do item

        Returns:
            float: valor total do estoque do item
        """
        
        return self.__estoque * self.__preco