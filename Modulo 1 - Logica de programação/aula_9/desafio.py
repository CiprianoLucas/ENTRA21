"""
Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa pode ter um ou mais
telefones e a chave do dicionário é o nome da pessoa. Seu programa deve ter as seguintes funções:

* Adicionar contato: acrescenta um novo nome na agenda com um ou mais telefones.
* Adicionar telefone: acrescenta um novo telefone em um nome já existente na agenda. Caso o nome não exista na agenda,
você deve perguntar se a pessoa deseja incluí-lo.
* Excluir telefone: remove o telefone de uma pessoa que já está cadastrada na agenda.
* Excluir contato: remove o nome de uma pessoa da agenda.
* Consultar contato: obtém as informações de contato de uma pessoa pelo nome.
* Listar contatos: listar todos os contatos (nome e telefones) presentes na agenda.
"""
agenda = {}

# Menu para interação
while True:
    print("""
--- Agenda Telefônica ---
1: Adicionar contato
2: Adicionar telefone
3: Excluir telefone
4: Excluir contato
5: Consultar contato
6: Listar contatos
7: Sair""")

    opcao = input("Digite o número da opção desejada: ")

    match opcao:
        case "1":
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone")
            agenda[nome] = [telefone]

        case "2":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o novo telefone: ")
            if nome in agenda:
                agenda[nome].append(telefone)
            else:
                print(f"O nome {nome} não encontrado")

        case "3":
            nome = input("Digite o nome do contato: ")
            if nome in agenda:
                for indice, telefone in enumerate(agenda[nome]):
                    print(f"{indice + 1}) {telefone}")

                indice_telefone = int(input("Selecione o telefone a ser removido: ")) - 1

                if indice_telefone not in range(len(agenda[nome])):
                    print("O índice selecionado não existe.")
                else:
                    agenda[nome].pop(indice_telefone)
            else:
                print("Nome não foi encontrado na agenda.")

        case "4":
            nome = input("Digite o nome do contato: ")
            if nome in agenda:
                del agenda[nome]
            else:
                print("Nome não foi encontrado na agenda.")

        case "5":
            nome = input("Digite o nome do contato: ")
            if nome in agenda:
                print(f"Contato: {nome} | Telefones: {', '.join(agenda[nome])}")
            else:
                print("Nome não foi encontrado na agenda.")

        case "6":
            for nome, telefones in agenda.items():
                print(f"Contato: {nome} | Telefones: {', '.join(agenda[nome])}")

        case "7":
            break
        case _:
            print("Opção inválida")