class Calculadora:
    """Calculadora represeta uma calculadora
    """
    
    def __init__(self, num_a : float, num_b : float):
        """Criando a calculadora passando os números que serão usados

        Args:
            num_a (float): primeiro número
            num_b (float): segundo número
        """
        self.num_a = num_a
        self.num_b = num_b
        
    @property
    def num_a(self):
        return self.__num_a
    
    @num_a.setter
    def num_a(self, num_a):
        self.__num_a = num_a
        
    @property
    def num_b(self):
        return self.__num_b
    
    @num_b.setter
    def num_b(self, num_b):
        self.__num_b = num_b
        
    def soma(self) -> float:
        """Soma os dois números

        Returns:
            float: retorna a soma dos números
        """
        return self.__num_a + self.__num_b
    
    def subtracao(self) -> float:
        """Subtrai o segundo número do primeiro

        Returns:
            float: resultado da subtração
        """
        return self.__num_a - self.__num_b
    
    def multiplicacao(self) -> float:
        """Multiplica os dois números
        
        Returns:
        float: resultado da multiplicação
        """
        return self.__num_a * self.__num_b
    
    def divisao(self) -> float:
        """Divide o primeiro número pelo segundo
        
        Returns:
        float: resultado da divisão
        """
        return self.__num_a / self.__num_b