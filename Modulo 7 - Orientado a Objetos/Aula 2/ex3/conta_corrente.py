from conta import Conta

class ContaCorrente(Conta):
    """Classe que representa uma conta corrente"""
    
    def __init__(self, titular, limite: float):
        TAXA = 0.002
        super().__init__(titular, TAXA)
        self.limite = limite
        
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        
    def sacar(self, valor: float) -> bool:
        """Sacar um valor da conta

        Args:
            valor (float): Valor a ser sacado
        """
        if self.__saldo + self.__limite < valor:
            return False
        
        if self.__saldo < valor:
            self.__limite -= valor - self.__saldo
            self.__saldo = 0
        else:
            self.__saldo -= valor
        
        return True
    