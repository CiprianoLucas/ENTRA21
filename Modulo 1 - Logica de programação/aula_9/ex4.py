"""
Escreva um algoritmo que receba um texto e retorne um dicionário com a contagem de cada palavra na string
Entrada:
“aprenda python, Python é divertido.”

Saída:
{"aprenda": 1, "python": 2, "é": 1, "divertido": 1}

"""

entrada = "aprenda python, Python é divertido."
entrada_formatada = entrada.replace(",","").lower()
saida = {}


for palavra in (entrada_formatada.split()):
    if palavra not in saida.keys():
        saida[palavra] = 0
    saida[palavra] += 1

print(saida)