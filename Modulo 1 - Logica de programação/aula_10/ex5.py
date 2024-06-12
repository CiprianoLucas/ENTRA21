"""

Escreva uma função chamada “repetir” que recebe dois parâmetros. O primeiro é o
elemento que repetirá, enquanto o segundo é o número de vezes que haverá a
repetição. Uma lista deve ser retornada.

"""

def repetir(elemento: int, repeticoes) -> list:
    """
    Essa função cria uma lista com o elemento pelo número de repetições
    """
    return [elemento for _ in range(repeticoes)]

print(repetir("haha", 10))