class Ponto2D:
    """A classe Ponto2D reperenta um ponto 2d em um plano cartesiano
    """
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x: int):
        self.__x = x
        
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y: int):
        self.__y = y
        
    def tem_eixo_comum(self, a : int, b: int):
        """Verifica se o ponto tem o mesmo eixo comum com outro ponto.
        
        Args:
            a (int): eixo x ser comparado.
            b (int): eixo y ser comparado.
        
        Returns:
            bool: True se o ponto tem o mesmo eixo comum com outro ponto.
        """
        return self.x == a or self.y == b
        