"""

Escreva um programa que leia os valores de uma matriz 3x3 e um valor X. O programa deverá fazer
uma busca na matriz e, ao final, mostrar a localização (linha e coluna) do valor X. Caso o valor
X não esteja presente na matriz o programa deve mostrar a mensagem “Não encontrado”.

"""

matriz = [
    ["a", "b", "d"],
    ["d", "e", "b"],
    ["b", "d", "i"]
]

x = input("Qual valor deseja buscar? ")

linha = [i for i in range(len(matriz)) if x in matriz[i]]
coluna = [matriz[i].index(x) for i in linha]
enderecos = [[linha[i], coluna[i]] for i in range(len(linha))]

print(enderecos) if len(linha) > 0 else print("Não encontrado")
