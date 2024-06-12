from ex1 import Pessoa

class Agenda:
    """Classe que representa uma pessoa
    Args:
        name(str): Nome da pessoa
        tell(str): Telefone da pessoa    
    """
    
    def __init__(self, nome: str):
        self.nome = nome
        self.__pessoas = []
        
        
    def adicionar_pessoa(self, pessoa: Pessoa):
        """Adiciona uma pessoa na agenda

        Args:
            pessoa (Pessoa): pessoa a ser adicionada
        """
        if len(self.__pessoas) < 10:
            self.__pessoas.append(pessoa)
            print("Adicionado com sucesso")
        else:
            print("Agenda cheia")
            
    def remover_pessoa(self, nome: str):
        """Remove uma pessoa fa agenda com base no nome

        Args:
            nome (str): nome da pessoa
        """
        for pessoa in self.__pessoas:
            if pessoa.nome == nome:
                self.__pessoas.remove(pessoa)
                print("Removido com sucesso")
            else:
                print("Pessoa não encontrada")
            
    def procurar(self, nome: str):
        """busca as informações da pessos

        Args:
            nome (str): nome da pessoa  a ser procurada
        """
        for pessoa in self.__pessoas:
            if pessoa.nome == nome:
                print(f"nome: {pessoa.nome} | telefone: {pessoa.telefone}")

            else:
                print("Pessoa não encontrada")
    
    def listar(self):
        """Lista todos os contatos
        """
        for pessoa in self.__pessoas:
            print(f"nome: {pessoa.nome} | telefone: {pessoa.telefone}")
    
        