from forma_geometrica import FormaGeometrica

class Triangulo(FormaGeometrica):
    """Cria uma forma geométrica de triangulo"""
   
    def __init__(self, lado_a: float, lado_b: float, lado_c: float) -> None:
         """Inicializa um objeto triangulo

         Args:
            lado_a (float): tamanho do lado A do triângulo
            lado_b (float): tamanho do lado B do triângulo
            lado_c (float): tamanho do lado C do triângulo
         """
         
         self.lado_a = lado_a
         self.lado_b = lado_b
         self.lado_c = lado_c

    def calcular_area(self) -> float:
        """Retorna a área do triangulo
        """
        p = self.calcular_perimetro() / 2
        
        
        return (p * (p - self.lado_a) * (p - self.lado_b) * (p - self.lado_c)) ** 0.5

    def calcular_perimetro(self) -> float:
        """Retorna o perímetro do triangulo
        """
        return self.lado_a + self.lado_b + self.lado_c
    

if __name__ == '__main__':
    meu_triangulo = Triangulo(10, 15, 20)
    print(meu_triangulo.lado_a)
    print(meu_triangulo.lado_b)
    print(meu_triangulo.lado_c)
    print(meu_triangulo.calcular_area())
    