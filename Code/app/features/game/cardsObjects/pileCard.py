from Card import Card

class PileCard:
    def __init__(self, id=None, cards=None):
        # cards représente une liste de cartes et id correspond à l'id de l'api
        self.id = id
        self.cards = cards
    
    def len(self): 
        return(len(self.cards))

    def topCard(self): 
        return self.cards[0]
    
    def shuffle(self): 
        pass

    def draw(self): 
        pass