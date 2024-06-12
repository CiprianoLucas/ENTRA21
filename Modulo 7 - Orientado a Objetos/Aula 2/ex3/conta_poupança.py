from conta import Conta

class ContaPoupanca(Conta):
    """Classe que representa uma conta poupança"""
    
    def __init__(self, titular):
        TAXA = 0.005
        super().__init__(titular, TAXA)
        
    def render(self, juros: float):
        """Multiplica o saldo atual por 1 + juros
        
        args:
            juros(float): valor do juros (ex:0.043)
        """
        self.__saldo *= 1 + juros