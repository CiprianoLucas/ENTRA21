from forma_geometrica import FormaGeometrica


class Retangulo(FormaGeometrica):
    """Cria uma forma geométrica de retangulo"""
   
    def __init__(self, largura: float, altura: float) -> None:
         """Inicializa um objeto retangulo

         Args:
            largura (float): largura da forma geometrica retangulo
            altura (float): altura da forma geometrica retangulo
         """
         
         self.largura = largura
         self.altura = altura

    def calcular_area(self) -> float:
        """Retorna a área do retangulo
        """
        
        return self.largura * self.altura

    def calcular_perimetro(self) -> float:
        """Retorna o perímetro do retangulo
        """
        return 2 * (self.largura + self.altura)
    