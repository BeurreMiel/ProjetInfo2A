from Card import Card
from app.features.game.apiInteractions.cardAPI import cardAPI


class PileCard:
    def __init__(self, id=None, cards=None):
        # cards représente une liste de cartes et id correspond à l'id de l'api
        self.id = id
        self.cards = cards

    def len(self):
        return(len(self.cards))

    def topCard(self):
        return self.cards[0]

    def shuffleDeck(self):
        self.id = cardAPI.shuffleDeck(self.id)

    def drawDeck(self):
        result = cardAPI.drawDeck(self.id)
        self.id = result[1]
        return(result[0][0])

    @staticmethod
    def generateNewDeck(self):
        self.id = cardAPI.newDeck()

    def shufflePile(self):
        pass

    def drawPile(self):
        pass

    # Todo : Implement custom pile drawing and shuffling
