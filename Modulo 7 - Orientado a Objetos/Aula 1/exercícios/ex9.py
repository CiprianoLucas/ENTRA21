class Pessoa:
    """Classe representa uma pessoa
    """
    
    __total_pessoas = 0
    
    
    def __init__(self, nome: str, idade: int):
        """Cadastra uma pessoa

        Args:
            nome (str): Nome da pessoa
            idade (int): idade da pessoa
        """
        
        self.__nome = nome
        self.__idade = idade
        
        Pessoa.__total_pessoas += 1
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    
    @staticmethod
    def get_total_pessoas():
        """Retorna o total de pessoas já cadastradas
        """
        return Pessoa.__total_pessoas