"""

Crie uma função chamada "somar" que recebe uma quantidade variável de
números como argumentos e retorna a soma deles.

"""

def somar(*args: float) -> float:
    """
    Essa função retorna a soma dos argumentos
    """
    return sum(args)

print(somar(1,3,10,100))