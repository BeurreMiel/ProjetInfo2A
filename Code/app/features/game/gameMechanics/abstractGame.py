
from abc import ABC, abstractmethod

class AbstractGame:

    def __init__(self, players=[], deck=None):
        self.players = list(players)
        self.deck = deck

    @abstractmethod
    def reglesJeu(self):
        """ A implémenter en fonction du jeu demandé"""
        pass