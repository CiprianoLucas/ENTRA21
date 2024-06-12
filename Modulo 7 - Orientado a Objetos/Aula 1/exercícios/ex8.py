from datetime import datetime

class Veiculo:
    """Veiculo representa um veiculo
    """
    def __init__(self, marca: str, ano: int, valor: float):
        """Cria um veículo com  valores para calculo de imposto

        Args:
            marca (str): marca do veículo
            ano (int): ano do veículo
            valor (float): valor base do veículo
        """
        
        self.__marca = marca
        self.__ano = ano
        self.__valor = valor
        
    @property
    def marca(self):
        return self.__marca
        
    @property
    def ano(self):
        return self.__ano
    
    @property
    def valor(self):
        return self.__valor
    
    def calcular_imposto(self) -> float:
        """Calcula o imposto a ser pago naquele ano

        Returns:
            float: valor do imposto
        """
        depreciado = self.__valor * (0.95 ** (datetime.now().year - self.ano))
        return depreciado * 0.02 