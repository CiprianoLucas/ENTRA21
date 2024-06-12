"""
Escreva uma função “formata_cpf” que recebe um número inteiro e converta ele para uma
string no formato do cpf “000.000.000-00”. Caso o número fornecido não seja válido a
função deve retornar o próprio número em formato de string.
"""


def formata_cpf(cpf_int: int) -> str:
    """
    Função retorna o número inteiro do CPF como string formatada
    :param cpf_int: CPF como número inteiro
    :return: string do CPF formatado
    """
    cpf_limpo = str(cpf_int)

    if len(cpf_limpo) != 11:
        return cpf_limpo

    soma = 0

    # Verificando se todos os números são iguais
    if cpf_limpo.count(cpf_limpo[0]) == 11:
        return cpf_limpo

    # Somando a multiplicação dos primeiros 9 dígitos
    for i in range(9):
        soma += int(cpf_limpo[i]) * (10 - i)

    # Validando se resto da soma por 11 é menor que 2, se for o primeiro digito verificador deve ser 0,
    # se não o primeiro dígito verificador deve ser 11 menos esse resto.
    if ((soma % 11 < 2) and (cpf_limpo[9] == "0")) or (
            (soma % 11 >= 2) and (11 - (soma % 11) == int(cpf_limpo[9]))):
        soma = 0

        # Somando a multiplicação dos primeiros 10 dígitos
        for i in range(10):
            soma += int(cpf_limpo[i]) * (11 - i)

        # Validando se resto da soma por 11 é menor que 2, se for o segundo digito verificador deve ser 0,
        # se não o segundo dígito verificador deve ser 11 menos esse resto.
        if ((soma % 11 < 2) and (cpf_limpo[10] == "0")) or (
                (soma % 11 >= 2) and (11 - (soma % 11) == int(cpf_limpo[10]))):

            return f"{cpf_limpo[0:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}:{cpf_limpo[9:11]}"
        else:
            return cpf_limpo

    else:
        return cpf_limpo


print(formata_cpf(10728507960))
