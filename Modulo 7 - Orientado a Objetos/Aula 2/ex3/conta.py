from __future__ import annotations
from abc import ABC
from random import randint


class Conta(ABC):
    """Superclasse de contas bancárias"""
    
    def __init__(self, titular: str, taxa: float = 0):
        """Cria uma conta

        Args:
            n_conta (int): número da conta
            titular (str): titular
        """
        self.__n_conta = randint(1, 100_000)
        self.titular = titular
        self.taxa = taxa
        self.__saldo = 0
        
    @property
    def n_conta(self):
        return self.__n_conta
    
    @property
    def taxa(self):
        return self.__taxa
    
    @taxa.setter
    def taxa(self, taxa):
        self.__taxa = taxa
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
        
    def depositar(self, valor: float) -> None:
        """Deposita um valor na conta

        Args:
            valor (float): Valor a ser depositado
            
        Returns: Valor depositado
        """
        
        self.__saldo += valor * (1 - self.__taxa)
        
    def sacar(self, valor: float) -> bool:
        """Sacar um valor da conta

        Args:
            valor (float): Valor a ser sacado
        """
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        return False
        
    def transferir(self, conta_destino: Conta , valor: float):
        """Tranfere o valor da conta para uma outra informada

        Args:
            conta_destino (Conta): Conta que irá receber
            valor (float): valor a ser transferido
        """
        
        if self.sacar(valor):
            conta_destino.depositario = valor
        
        else:
            print("Saldo insuficiente")
        
        

