from app.features.game.cardObjects.pileCard import pileCard
from app.features.game.cardObjects.Card import Card

class Joueur: 

    def __init__(self, name=None, cards=[],score =0):
        self.name = name
        self.cards = list(cards)
        self.score = score

    def name(self):
        return self.name
    
    def score(self): 
        return self.score

    def hand(self):
        return self.cards

    def drawCard(self, card):
        self.cards.append(card)

    def poserCard(self, card):
        self.cards.remove(card)