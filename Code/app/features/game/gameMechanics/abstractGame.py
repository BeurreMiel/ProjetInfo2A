
from abc import ABC, abstractmethod

class AbstractGame(metaclass=ABC):

    def __init__(self, players=[], deck=None):
        self.players = list(players)
        self.deck = deck

    @property
    @abstractmethod
    def listCarteAuth(self):
        pass

    @abstractmethod
    def gameLoop(self):
        """ A implémenter en fonction du jeu demandé"""
        pass

    @abstractmethod
    def checkPlayerNumber(self): 
        pass