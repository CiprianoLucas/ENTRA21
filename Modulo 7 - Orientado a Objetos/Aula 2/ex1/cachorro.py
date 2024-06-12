from animal import Animal

class Cachorro(Animal):
    """Cachorro representa um animal

    Attributes:
        nome (str): O nome do cachorro
        idade (int): idade do cachorro
        porte (str): A porte do cachorro
    """
    
    def __init__(self, nome: str, idade: int, porte: str) -> None:
        """Inicializa o objeto Cachorro
        
        Args:
             nome (str): nome do cachorro
             idade (int): idade do cachorro
             porte (str): porte do cachorro
        """
        
        super().__init__(nome, idade)
        self.porte = porte
        
    def emitir_som():
        """Emitir som do cachorro"""
        super().emitir_som()
        print("Au Au Au")
        
    def mover():
        super().mover()
        print("Correndo em 4 patas")