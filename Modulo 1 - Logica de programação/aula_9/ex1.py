"""

Faça um algoritmo que elimine as duplicatas da lista abaixo e ordene-as de maneira decrescente:
lista = [1, 1, 5, 3, 2, 10, 2, 5, 6, 11, 100, 1000, 900, 900, 10, 5, 534]

"""

lista = [1, 1, 5, 3, 2, 10, 2, 5, 6, 11, 100, 1000, 900, 900, 10, 5, 534]
lista_limpa = list(set(lista))

#print(lista_limpa)

print(sorted(lista_limpa, reverse=True))
