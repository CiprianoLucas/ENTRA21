"""

Escreva um programa que solicite o tamanho de uma matriz identidade e mostre ela na tela.

"""

tamanho = int(input("Qual o tamanho da matriz identidade?"))
matriz = []
for i in range(tamanho):
    matriz.append([1 if i == j else 0 for j in range(tamanho)])

print(matriz)

for i in matriz:
    for j in i:
        print(j, end=" ")
    print()

