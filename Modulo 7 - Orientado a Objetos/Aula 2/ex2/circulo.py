from forma_geometrica import FormaGeometrica
from math import pi

class Circulo(FormaGeometrica):
    """Cria uma forma geométrica de círculo"""
   
    def __init__(self, raio: float) -> None:
         """Inicializa um objeto circulo

         Args:
            raio (float): raio da forma geometrica círculo
         """
         self.raio = raio

    def calcular_area(self) -> float:
        """Retorna a área do círculo
        """
        
        return pi * self.raio ** 2
    
    def calcular_perimetro(self) -> float:
        """Retorna o perímetro do círculo
        """
        return 2 * pi * self.raio
    