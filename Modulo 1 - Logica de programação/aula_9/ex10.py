"""

Crie um algoritmo que leia o nome, cpf e idade de várias pessoas e salve essas informações em uma lista
de dicionários. No final o programa deverá mostrar uma lista com os dados das pessoas classificadas em:
pessoas maiores de idade e pessoas menores de idade.

"""

lista = [{"nome": "Alice", "cpf": "123.456.789-00", "idade": 25},
         {"nome": "Rodrigo", "cpf": "987.654.321-99", "idade": 7},
         {"nome": "Lucas", "cpf": "222.222.222-33", "idade": 16},
         {"nome": "Maria", "cpf": "454.545.454-77", "idade": 45}]

novo_nome = input("Deseja um novo nome? ")

while novo_nome == "Sim":
    lista.append({"nome": input("Escreva o nome ")})
    lista[-1].update({"cpf": input("Escreva o CPF ")})
    lista[-1].update({"idade": int(input("Escreva a idade "))})
    novo_nome = input("Deseja um novo nome? ")

maior = [lista[i] for i in range(len(lista)) if lista[i]["idade"] >= 18]
menor = [lista[i] for i in range(len(lista)) if lista[i]["idade"] < 18]
print(f"Maiores de idade são: {[maior[i]['nome'] for i in range(len(maior))]}")
print(f"Maiores de idade são: {[menor[i]['nome'] for i in range(len(menor))]}")