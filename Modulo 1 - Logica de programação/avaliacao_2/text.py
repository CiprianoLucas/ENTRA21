"""
Avaliação 2

Neste desafio, você e sua equipe irão construir um sistema básico para gerenciar livros em uma biblioteca.
Os livros serão armazenados em um dicionário, onde cada chave é um ID único do livro (um número inteiro)
e o valor é outro dicionário contendo informações sobre o livro.
Informações do Livro:
Título
Autor
Ano de publicação
Gênero
Avaliações
Status (Emprestado ou Disponível)

Funções requeridas:
adicionar_livro(id, titulo, autor, ano, genero): Adiciona um livro ao sistema. - Lucas
remover_livro(id): Remove um livro do sistema usando o ID. - Lucas
emprestar_livro(id): Altera o status do livro para “Emprestado”. - Lucas
devolver_livro(id): Altera o status do livro para “Disponível”. - Gustavo
listar_livros(): Retorna uma lista de todos os livros e suas informações. - Gustavo
buscar_livro(titulo): Busca um livro pelo título e retorna as suas informações. - Gustavo
livros_por_autor(autor): Retorna uma lista de todos os livros de um determinado autor. - Tamires
livros_por_genero(genero): Retorna uma lista de todos os livros de um determinado gênero. - Tamires
livros_emprestados(): Lista todos os livros que estão emprestados. - Tamires
avaliar_livro(id): Permite adicionar uma avaliação para o livro (1 a 5 estrelas). - Abner
obter_media_avaliacoes(id): Retorna a média de avaliações de um livro. - Abner

Regras adicionais:
Não é possível adicionar um livro com um ID que já existe.
Não é possível remover ou emprestar um livro que não existe.
Não é possível emprestar um livro que já foi emprestado.
Não é possível devolver um livro que já está disponível.


biblioteca = {
    1: {"titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "ano": 1937, "genero": "Fantasia", "status": "Disponível", "avaliações": [5, 5, 4]},
    2: {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "genero": "Ficção", "status": "Emprestado"},
    # ...


def nomes(nome: str="amigo") -> None

"""

biblioteca = {
    1: {"titulo": "O Hobbit", "autor": "George Orwell", "ano": 1937, "genero": "Fantasia", "status": "Disponível", "avaliações": [5, 5, 4]},
    2: {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "genero": "Ficção", "status": "Emprestado", "avaliações": []},}


#Lucas


def adicionar_livro(identificador: int, titulo_livro: str, autor_livro: str, ano_livro: int, genero_livro: str) -> None:
    """
    :param identificador: Número de identificação do livro
    :param titulo_livro: Título do livro
    :param autor_livro: Nome do autor do livro
    :param ano_livro: Ano de lançamento do livro
    :param genero_livro: Gênero do livro
    :return: None

    Essa função irá inserir um novo livro na biblioteca de livros
    """

    if ano_livro > 2023:
        print("Ano inválido")
        return

    if identificador in biblioteca:
        print("Já existe esse ID")
        return
    biblioteca.update({identificador: {"titulo": titulo_livro, "autor": autor_livro, "ano": ano_livro, "genero": genero_livro, "status": "Disponível"}})
    print(f"Livro '{biblioteca[identificador]['titulo']}' cadastrado com sucesso")


def remover_livro(identificador: int) -> None:
    """
    :param identificador:  Insira o número de identificação do livro
    :return: None

    Essa função irá remover o livro da biblioteca
    """

    if identificador not in biblioteca:
        print("Número de identificação não localizado")
        return
    print(f"Livro '{biblioteca[identificador]['titulo']}' excluido com sucesso")
    del biblioteca[identificador]


def emprestar_livro(identificador: int) -> None:
    """
    :param identificador:  Insira o número de identificação do livro
    :return: None

    Essa função irá constatar o livro da biblioteca como emprestado
    """

    if identificador not in biblioteca:
        print("Número de identificação não localizado")
        return

    if biblioteca[identificador]["status"] == "Emprestado":
        print(f"Desculpas! O livro '{biblioteca[identificador]['titulo']}' já foi emprestado")
        return

    biblioteca[identificador]["status"] = "Emprestado"
    print(f"O livro '{biblioteca[identificador]['titulo']}' emprestado com sucesso!")







#Gustavo


def devolver_livro(identificador: int) -> None:
    """ Função para devolver um livro, caso esteja com a situação: Emprestado"""

    if not biblioteca[identificador]["status"] == "Emprestado":
        print("Não é possível devolver um livro já disponível!")
    else:
        biblioteca[identificador]["status"] = "Disponível"
        print("Livro devolvido à biblioteca!")


def listar_livros() -> None:
    """ Função para listar todos os livros na biblioteca """

    for chave, dicionario in biblioteca.items():
        print(f"""
ID: {chave}
Título: {dicionario["titulo"]}
Autor: {dicionario["autor"]}
Ano: {dicionario["ano"]}
Gênero: {dicionario["genero"]}
Situação: {dicionario["status"]}""")
    return


def buscar_livro(titulo: str) -> None:
    """ Função para buscar um livro pelo título e printá-lo caso exista. """
    for chave, dicionario in biblioteca.items():
        if biblioteca[chave]["titulo"].lower() == titulo.lower():
            print(
f"""
Título: {dicionario["titulo"]}
Autor: {dicionario["autor"]}
Ano: {dicionario["ano"]}
Gênero: {dicionario["genero"]}
Situação: {dicionario["status"]}""")

            return
    print("Título não encontrado!")
    return



#Tamires


def livros_por_autor(autor: str) -> None:
    """Retorna uma lista de todos os livros de um determinado autor"""
    existe = False
    livros_autor = []
    for identificador, livro in biblioteca.items():

        if livro["autor"] == autor:
            livros_autor.append(livro['titulo'])
            existe = True

    if not existe:
        print(f"Autor não localizado.")
    else:
        print(f"A listagem de livros do autor {livro['autor']}: {' - '.join(livros_autor)}")


def livros_por_genero(genero: str) -> None:
    """Retorna uma lista de todos os livros de um determinado gênero."""
    livros_do_genero = []

    for identificador, livro in biblioteca.items():
        if livro["genero"] == genero:
            livros_do_genero.append((identificador, livro))
            print(f"A listagem de livros do gênero {livro['genero']} é {livros_do_genero}")
            return
    else:
        print("Gênero não localizado na biblioteca")


def livros_emprestados() -> None:
    """Lista todos os livros que estão emprestados."""

    for identificador, livro in biblioteca.items():
        if livro["status"] == "Emprestado":
            print(f"A listagem de livros emprestados é {livro['titulo']}")
            return


#Abner
def avaliar_livro(identificador: int) -> None:
    """Adiciona a avaliação do livro dada pelo usuário"""
    while True:
        if not identificador in biblioteca:
            print("O ID não é válido!")
            break

        nota = input("Digite a quantidade de estrelas de 1 - 5 para a avaliação do livro: ")
        if not nota.isdigit():
            print("A avaliação deve ser de 1 - 5, não digite texto.")
            continue

        nota = int(nota)
        if nota < 1 or nota > 5:
            print("A avaliação deve ser de 1 - 5.")
            continue

        biblioteca[identificador]["avaliações"].append(nota)
        print("Avaliação salva com sucesso!")
        break


def obter_media_avaliacoes(identificador: int) -> None:
    """Obtem a média das aváliações do livro"""
    if not identificador in biblioteca:
        print("O ID não é válido!")
        return None

    lista_avaliacoes = biblioteca[identificador]["avaliações"]
    media_livros = sum(lista_avaliacoes) / len(lista_avaliacoes)
    print(f"A mídia das avaliações do livro é: {media_livros}.")


















while True:
    funcao_desejada = int(input("""
    0 - Sair
    1 - Adicionar
    2 - Remover
    3 - Emprestar
    4 - Devolver
    5 - Listar
    6 - Buscar
    7 - Livros do autor
    8 - Livros do gênero
    9 - Livros emprestados
    10 - Avaliar
    11 - Avaliação média
    Escreva a função desejada: 
    """))

    match funcao_desejada:
        case 0:
            print("Volte sempre!")
            break
        case 1:
            id_livro = int(input("Insira um número de identificação para o livro: "))
            while id_livro in biblioteca:
                id_livro = int(input("Insira outro número, esse está em uso: "))
            titulo = input("Nome do livro: ")
            autor = input("Nome do autor: ")
            ano = int(input("Ano do livro: "))
            genero = input("Gênero do livro: ")

            adicionar_livro(id_livro, titulo, autor, ano, genero)

        case 2:
            id_livro = int(input("Insira o número de identificação do livro: "))
            remover_livro(id_livro)

        case 3:
            id_livro = int(input("Insira o número de identificação do livro: "))
            emprestar_livro(id_livro)

        case 4:
            id_livro = int(input("Insira o número de identificação do livro: "))
            devolver_livro(id_livro)

        case 5:
            listar_livros()

        case 6:
            titulo = input("Nome do livro: ")
            buscar_livro(titulo)

        case 7:
            autor = input("Nome do autor: ")
            livros_por_autor(autor)

        case 8:
            genero = input("Gênero do livro: ")
            livros_por_genero(genero)

        case 9:
            livros_emprestados()

        case 10:
            id_livro = int(input("Insira o número de identificação do livro: "))
            avaliar_livro(id_livro)

        case 11:
            id_livro = int(input("Insira o número de identificação do livro: "))
            obter_media_avaliacoes(id_livro)

        case _:
            print("Função não encontrada")




























































