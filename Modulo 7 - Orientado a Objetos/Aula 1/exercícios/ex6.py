class Carro:
    """Carro representa um carro
    """
    def __init__(self, marca: str, modelo: str, ano: int):
        """Criando o carro passando principais informações  

        Args:
            marca (str): marca do carro
            modelo (str): modelo do carro
            ano (int): ano do carro
        """
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__velocidade = 0
        
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    def acelerar(self):
        """Aumenta a velocidade em 10
        """
        self.__velocidade += 10
        
    def frearia(self):
        """Diminui a velocidade em 5
        """
        if self.__velocidade <=5:
            self.__velocidade = 0
        else:
            self.__velocidade -= 5
        
