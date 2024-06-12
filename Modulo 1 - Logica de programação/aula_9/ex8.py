"""

Crie um algoritmo que mapeie palavras em inglês para a sua tradução em um dicionário, após isso peça para
o usuário digitar um texto em inglês com as palavras contidas no dicionário e mostre o texto traduzido.

"""

tradutor = {"I": "Eu",
            "dance": "danço",
            "at": "a",
            "night": "noite"}

texto = "I dance at night"

traducao_vetor = [tradutor[i] for i in texto.split()]
traducao = ""

for i in traducao_vetor:
    traducao += i + " "

print(traducao)