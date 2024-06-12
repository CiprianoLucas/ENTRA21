from animal import Animal

class Gato(Animal):
    """Gato representa um animal

    Attributes:
        nome (str): O nome do Gato
        idade (int): idade do Gato
        raca (str): A raça do Gato
    """
    
    def __init__(self, nome: str, idade: int, raca: str) -> None:
        """Inicializa o objeto Gato
        
        Args:
             nome (str): nome do Gato
             idade (int): idade do Gato
             raca (str): raça do Gato
        """
        
        super().__init__(nome, idade)
        self.raca = raca
        
    def emitir_som():
        """Emitir som do Gato"""
        super().emitir_som()
        print("Miau")
        
    def mover():
        """Fez o gato se mover"""
        super().mover()
        print("Escalando com as garras")