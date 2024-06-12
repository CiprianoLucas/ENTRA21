from abc import ABC # Precisamos utilizar ABC para definir uma classe abstrata

class Animal(ABC):
    """Animal representa um animal
    
    Atributes:
        nome (str): Nome do animal
        idade (int): Idade do animal
    """
    
    def __init__(self, nome: str, idade: int) -> None:
         """Inicializa um objeto Animal

         Args:
             nome (str): nome do animal
             idade (int): idade do animal
         """
         
         self.nome = nome
         self.idade = idade
         
    def emitir_som():
        """Faz o animal emitir o som"""

        print("o {self.nome} faz: ")
        
    def mover():
        """Faz o animal se mover"""

        print("o {self.nome} moveu")
        
        
