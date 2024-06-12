"""
9. Construa um algoritmo que some todas os valores numéricos do dicionário abaixo e mostre o resultado na tela:

animais = {
"gatos": "Miaw",
"cachorros": 22,
"zebra": 10,
"girafa": 15,
"panda": 23,
"coala": 3
}
"""

animais = {
    "gatos": "Miaw",
    "cachorros": 22,
    "zebra": 10,
    "girafa": 15,
    "panda": 23,
    "coala": 3
}

soma = 0

for i in animais.values():
    if isinstance(i, int):
        soma += i

print(soma)