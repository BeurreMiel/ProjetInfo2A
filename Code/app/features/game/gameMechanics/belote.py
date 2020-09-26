from typing import Optional
from app.features.users.joueur import Joueur
import app.features.utils as utils
from abstractGame import abstractGame
from app.features.cardObjects.pileCard import PileCard


class Team:
    def __init__(self, name: str, players: list[Joueur]) -> None:
        self.name = name

        if len(players) != 2:
            raise Exception(
                "Une équipe ne peut être composée que de deux joueurs")
        self.players = players.copy()
        self.score = 0

    def __str__(self) -> str:
        return ("{ name: " + str(self.name) + ", players: " + utils.listString(self.players)
                + ", score: " + str(self.score) + "}")


class Belote(abstractGame):
    def __init__(self, players, deck):
        super().__init__(players, deck)
        self.premierJoueur = self.players[0]
        self.atout = Optional[str],
        self.pick = Optional[Joueur] = None

    def checkPlayerNumber(self):
        if len(self.players) != 4:
            raise Exception(
                "La belote ne se joue qu'a 4 joueurs")

    @property
    def listCarteAuth(self):
        self.listCarteAuth = "7S,7D,7C,7H,8S,8D,8C,8H,9S,9D,9C,9H,0S,\
        0D,0C,0H,JS,JD,JC,JH,QS,QD,QC,QH,KS,KD,KC,KH,AS,AD,AC,AH"

    def gameLoop(self):
        while not self.pick:
            deck = PileCard.generateNewCustomDeck(self.listCarteAuth)
            deck.shuffleDeck()
            # Distribution de carte
            for player in self.players:
                player.drawCard(deck.drawDeck(deck.id, 3))
            for player in self.players:
                player.drawCard(deck.drawDeck(deck.id, 2))
            # Tour d'appel
            carteAppel = deck.drawDeck(deck.id)
            for player in self.players:
                rep = ""
                while not (rep == "y" or rep == "Y" or rep == "n" or rep == "N"):
                    rep = input(
                        "La couleur proposée est {}, voulez vous prendre ? (Y/N) ".format(carteAppel.couleur))
                if (rep == "y" or rep == "Y"):
                    self.atout = carteAppel.couleur
                    break
            if not self.pick:
                for player in self.players:
                    rep = ""
                    while not (rep == "y" or rep == "Y" or rep == "n" or rep == "N"):
                        rep = input(
                            "Souhaitez vous appeler ? (Y/N) ")
                    if (rep.upper() == "Y"):
                        color = ""
                        while not (color == "S" or color == "H" or color == "C" or color == "D"):
                            color = input(
                                "Quelle couleur souhaitez vous appeler ? (S/H/C/D) ")
                        if (rep == "S"):
                            self.atout = "SPADES"
                        elif (rep == "H"):
                            self.atout = "HEARTS"
                        elif (rep == "C"):
                            self.atout = "CLUBS"
                        else:
                            self.atout = "DIAMONDS"
                            
        # Fin de la distribution
        for player in self.players:
            if player == self.pick:
                player.drawCard(deck.drawDeck(deck.id, 2))
            else:
                player.drawCard(deck.drawDeck(deck.id, 3))
                
