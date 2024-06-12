"""

Crie uma função chamada "dobro" que recebe um número como parâmetro e retorna o dobro desse número.
Inclua uma docstring que explique o propósito da função.

"""

def dobro(a: float)-> float:
    """
    Essa função dobra o valor do parâmetro
    """
    return a * 2

print(dobro(float(input("Qual o número? "))))


