"""

Defina uma função chamada "calcular_area" que recebe dois parâmetros:
"base" e "altura". Adicione anotações de função para indicar que os
parâmetros são números e que a função retorna um número.

"""

def calcular_area(base: float, altura: float) -> float:
    """
    Essa função retorna a área de um triângulo
    """
    return base * altura / 2

print(calcular_area(10,5))