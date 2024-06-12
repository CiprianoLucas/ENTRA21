"""

Escreva um programa que leia os valores de uma matriz 3x3, conte e mostre quantos valores maiores que 10 ela possui.

"""

matriz = [
    [5, 43, 1],
    [23, 11, 5],
    [1, 9, 19]]

contador = 0

for i in matriz:
    for j in i:
        if j > 10:
            contador += 1

print(contador)