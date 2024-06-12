from conta import Conta

class ContaInvestimento(Conta):
    """Classe que representa uma conta investimento"""
    
    def __init__(self, titular):
        TAXA = 0.008
        super().__init__(titular, TAXA)
        self.__valor_investido = 0
        
    @property
    def valor_investido(self):
        return self.__valor_investido
    
    def investir(self, valor: float):
        """Investe um valor definido

        Args:
            valor (float): Valor a ser investido
        """
        if self.sacar(valor):
            self.__valor_investido += valor
        else:
            print("Saldo insuficiente")
    
    def sacar_investimento(self, valor: float):
        """Saca um valor que já foi investido para conta investimento

        Args:
            valor (float): Valor a ser sacado
        """
        
        if self.__valor_investido >= valor:
            self.__valor_investido -= valor
            self.__saldo += valor
            
        else:
            print("investimento insuficiente")
            
    def render_investimento(self, juros: float):
        """Multiplica o valor investido atual por 1 + juros
        
        args:
            juros(float): valor do juros (ex:0.043)
        """
        self.__valor_investido *= 1 + juros
    