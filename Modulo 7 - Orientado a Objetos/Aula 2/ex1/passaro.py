from animal import Animal

class Passaro(Animal):
    """Passaro representa um animal

    Attributes:
        nome (str): O nome do Passaro
        idade (int): idade do Passaro
        raca (str): A raça do Passaro
    """
    
    def __init__(self, nome: str, idade: int, raca: str) -> None:
        """Inicializa o objeto Passaro
        
        Args:
             nome (str): nome do Passaro
             idade (int): idade do Passaro
             raca (str): raça do Passaro
        """
        
        super().__init__(nome, idade)
        self.raca = raca
        
    def emitir_som():
        """Emitir som do Passaro"""
        super().emitir_som()
        print("Piu piu")
        
    def mover():
        """Fez o Passaro se mover"""
        super().mover()
        print("Saiu voando")