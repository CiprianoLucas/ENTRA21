from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    """FormaGeometrica representa uma forma geométrica"""
    
    @abstractmethod
    def calcular_area(self) -> float:
        """Calcula a área da forma geométrica"""
        
    @abstractmethod
    def calcular_perimetro(self) -> float:
        """Calcula a área da forma geométrica"""
    