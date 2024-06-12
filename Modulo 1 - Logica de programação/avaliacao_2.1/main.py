"""
Escreva uma função chamada compressao_string, que receba uma string como parâmetro e retorne a versão comprimida da mesma.

Exemplo:
Entrada: “AAABBBCCCCAA”
Saída: “A3B3C4A2”
"""

def compressao_string(texto: str) -> str:
    """
    Essa função irá comprimir as letrar repitidas consecutivas
    :param texto: Texto que irá comprimir
    :return: texto comprimido
    """
    contador = 1
    texto_comprimido = ""
    for i, letra in enumerate(texto):
        if i == 0:
            continue

        if letra == texto[i-1]:
            contador += 1
        else:
            texto_comprimido += texto[i-1] + str(contador)
            contador = 1
    texto_comprimido += texto[-1] + str(contador)
    return texto_comprimido

print(compressao_string("AAABBBCAAAEEEEEEEF"))
