class Triangulo:
    """Triangulo representa um triangulo"""
    
    def __init__(self, lado1: float, lado2: float, lado3: float):
        """Cria um triangulo passando o tamanho de cada lado

        Args:
            lado1 (float): tamanho lado 1
            lado2 (float): tamanho lado 2
            lado3 (float): tamanho lado 3
        """
        
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3
        self.verificar_tipo()
        
    def verificar_tipo(self):
        if self.__lado1 <= 0 or self.__lado2 <= 0 or self.__lado3 <= 0:
            raise ValueError("Os lados do triângulo devem ser maiores que zero.")
        elif self.__lado1 + self.__lado2 <= self.__lado3 or self.__lado2 + self.__lado3 <= self.__lado1 or self.__lado1 + self.__lado3 <= self.__lado2:
            raise ValueError("Os lados fornecidos não formam um triângulo válido.")
    
    def verificar_tipo(self) -> str:
        """Verifica qual tipo do trângulo

        Returns:
            str: pode retornar equilátero, isósceles ou escaleno
        """
        
        if self.__lado1 == self.__lado2 == self.__lado3:
            return "Equilátero"
        
        elif self.__lado1 == self.__lado2 or self.__lado2 == self.__lado3 or self.__lado1 == self.__lado3:
            return "Isósceles"
        
        else:
            return "Escaleno"
        