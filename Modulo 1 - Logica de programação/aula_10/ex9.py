"""

 Escreva uma função chamada "mostrar_informacoes" que recebe um número variável
 de argumentos nomeados e imprime cada argumento no formato "chave: valor".
 Por exemplo: "nome: João", "idade: 25".

"""


def mostrar_informacoes(*args):
    """
    Essa função retorna o argumento impar como chave e o par seguinte como valor
    """
    if len(args) % 2 != 0:
        print("A função deve receber um número par de argumentos.")
        return

    for i in range(0, len(args), 2):
        chave = args[i]
        valor = args[i + 1]
        print(f'{chave}: {valor}')


mostrar_informacoes("Lucas", "Lindo", "Pedro", "Inteligente")
