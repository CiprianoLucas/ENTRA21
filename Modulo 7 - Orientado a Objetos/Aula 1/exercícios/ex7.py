class Universidade:
    """Universidade representa uma universidade
    """
    def __init__(self, n_alunos: int, n_professores: int):
        """Cria a universidade passando o número de alunos e professores

        Args:
            n_alunos (int): número de alunos
            n_professores (int): número de professores
        """
        self.__n_alunos = n_alunos
        self.__n_professores = n_professores
        
    @property
    def n_alunos(self):
        return self.__n_alunos
    
    @property
    def n_professores(self):
        return self.__n_professores
    
    def matricular_aluno(self):
        """Adiciona um aluno na universidade"""
        self.__n_alunos += 1
        
    def contratar_professor(self):
        """Adiciona um professor na universidade"""
        self.__n_professores += 1
        
    def obter_total_pessoa(self):
        """Retorna o total de pessoas na universidade"""
        return self.__n_alunos + self.__n_professores