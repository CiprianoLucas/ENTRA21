class ConversorMoeda:
    """Representa um conversor de moeda com taxa de câmbio"""

    def __init__(self, taxa: float, moeda: str):
        """
        Inicializa um ConversorMoeda.

        Args:
            taxa (float): Taxa de câmbio para a moeda estrangeira.
            moeda (str): Nome da moeda estrangeira.
        """
        if taxa <= 0:
            raise ValueError("A taxa de câmbio deve ser maior que zero.")
        if not isinstance(moeda, str) or len(moeda.strip()) == 0:
            raise ValueError("O nome da moeda deve ser uma string não vazia.")
        
        self.moeda = moeda
        self.taxa = taxa

    @property
    def moeda(self) -> str:
        return self.__moeda
    
    @moeda.setter
    def moeda(self, moeda):
        self.__moeda = moeda

    @property
    def taxa(self) -> float:
        return self.__taxa
    
    @taxa.setter
    def taxa(self, taxa):
        self.__taxa = taxa

    def converter_para_real(self, valor: float) -> float:
        """Converte o valor para real.

        Args:
            valor (float): Valor na moeda estrangeira.

        Returns:
            float: Valor em real.
        """
        if valor < 0:
            raise ValueError("O valor a ser convertido deve ser maior ou igual a zero.")
        
        return valor / self.__taxa

    def converter_de_real(self, valor: float) -> float:
        """Converte o valor de real para a moeda estrangeira.

        Args:
            valor (float): Valor em real.

        Returns:
            float: Valor na moeda estrangeira.
        """
        if valor < 0:
            raise ValueError("O valor a ser convertido deve ser maior ou igual a zero.")
        
        return valor * self.__taxa