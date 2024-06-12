"""

Implemente um algoritmo que declare uma lista de strings e retorne uma
tupla contendo a quantidade de palavras em cada string.

"""

lista = ["elemento 1", "segundo elemento", "elemento da terceira casa", "4"]

palavras = (len(i.split()) for i in lista)

print(tuple(palavras))