class Aluno:
    """Classe que representa um aluno
    Args:
        matricula(str): Nome da pessoa
        nome(str): Telefone da pessoa 
        notas(list): Notas do aluno   
    """
    
    def __init__(self, matricula: str, nome: str, notas : list = []):
        
        self.__matricula = matricula
        self.nome = nome
        self.notas = notas
        
    @property
    def matricula(self) -> str:
        return self.__matricula
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
        
    @property
    def notas(self) -> list:
       return self.__notas
        
    @notas.setter
    def notas(self, notas: list):
       self.__notas = notas
        
    @property
    def get_media(self) -> float:
        """método para descobrir a média do aluno

        Returns:
            float: média da nota
        """
        if len(self.__notas) == 0:
            return 0 
        else:
            return sum(self.__notas) / len(self.__notas)
        
    @property
    def get_situacao(self) -> str:
        """método para descobrir a situação do aluno

        Returns:
            str: retorna a situação entre Reprovado, recuperação ou aprovado
        """
        if self.get_media < 4:
            return "Reprovado"
        elif self.get_media < 7:
            return "Recuperação"
        else:
            return "Aprovado"
        
        
if __name__ == '__main__':
    Lucas = Aluno('9652', 'Lucas')      
    print(Lucas.nome)
    print(Lucas.matricula)
    Lucas.notas = [2,4,3]
    print(Lucas.get_media)
    print(Lucas.get_situacao)