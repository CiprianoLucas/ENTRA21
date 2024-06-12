"""

 Crie uma função chamada "apresentacao" que recebe o nome de uma pessoa como parâmetro e
 imprime uma saudação  personalizada. Se nenhum nome for fornecido,
 a saudação deve ser genérica como "Olá, amigo!".

"""

def apresentacao(nome: str = "Amigo") -> None:
    """
    Essa função faz uma saudação com o nome dos parâmetros
    """
    print(f"Olá! {nome}")

apresentacao()