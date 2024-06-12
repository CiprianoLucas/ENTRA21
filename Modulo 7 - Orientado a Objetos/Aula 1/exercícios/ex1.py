import re

class Pessoa:
    """Classe que representa uma pessoa
    Args:
        name(str): Nome da pessoa
        tell(str): Telefone da pessoa    
    """
    def __init__(self, nome: str, telefone: str):
        
        self.nome = nome
        self.telefone = telefone
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
        
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone: str):     
        phone_regex = r"\+55\s?(?:\([1-9]{2}\)|[1-9]{2})\s?(?:9\s?\d{4}[-.\s]?\d{4}|\d{4}[-.\s]?\d{4})"
        if not re.match(phone_regex, telefone):
            raise AttributeError("Número inválido")
        
        else:
            self.__telefone = telefone
        

if __name__ == '__main__':
    Lucas = Pessoa('Lucas', '+55 47 99999 8888')      
    print(Lucas.nome)
    print(Lucas.telefone)
    Lucas.nome = 'Vinicius'
    print(Lucas.nome)

        
  


