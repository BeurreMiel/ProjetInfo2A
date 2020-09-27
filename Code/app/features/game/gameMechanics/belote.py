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
        """ self.premierJoueur = self.players[0] peu être pas utile"""
        self.atout = Optional[str],
        self.pick = Optional[Joueur] = None

    def checkPlayerNumber(self):
        if len(self.players) != 4:
            raise Exception(
                "La belote ne se joue qu'a 4 joueurs")

    def countPoints(plis, self):
        count = 0
        for card in plis:
            if card.couleur == self.atout:
                count += self.pointAtout[card.valeur]
            else:
                count += self.pointNonAtout[card.valeur]

    @property
    def listCarteAuth(self):
        self.listCarteAuth = "7S,7D,7C,7H,8S,8D,8C,8H,9S,9D,9C,9H,0S,\
        0D,0C,0H,JS,JD,JC,JH,QS,QD,QC,QH,KS,KD,KC,KH,AS,AD,AC,AH"

    @property
    def pointsPerCard(self):
        self.pointAtout = {
            "JACK": 20,
            "9": 14,
            "AS": 11,
            "10": 10,
            "KING": 4,
            "QUEEN": 3,
            "8": 0,
            "7": 0,
        }
        self.pointNonAtout = {
            "JACK": 2,
            "9": 0,
            "AS": 11,
            "10": 10,
            "KING": 4,
            "QUEEN": 3,
            "8": 0,
            "7": 0,
        }

    @staticmethod
    def verifCarteValide(carte, main, plis):
        """ Vérifie si la carte posée par le joueur est valide"""
        pass

    def tour(self, deck: PileCard):
        for player in self.players:
            flag = False
            while not flag:
                print("Veuillez sélectionner la carte à poser: ")
                for i in len(player.hand()):
                    print("[{}] {}".format(i, player.hand()[i]))
                pose = 10000
                while not (pose < len(player.hand())):
                    pose = input("Sélectionnez votre choix: ")
                    try:
                        pose = int(pose)
                    except ValueError:
                        print("Le choix doit être un entier")
                Belote.verifCarteValide(player.hand()[pose], player.hand, self.atout, plis)

            deck.addToPile("BeloteID", player.hand()[pose])
            player.poserCard(player.hand()[pose])

    def gameLoop(self):
        scoreTeam1 = 0
        scoreTeam2 = 0
        while (scoreTeam1 < 80) and (scoreTeam2 < 80):
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
                        player.drawCard(carteAppel)
                        break
                if not self.pick:
                    for player in self.players:
                        rep = ""
                        while not (rep == "y" or rep == "Y" or rep == "n" or rep == "N"):
                            rep = input(
                                "Souhaitez vous appeler ? (Y/N) ")
                        if (rep.upper() == "Y"):
                            player.drawCard(carteAppel)
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
                            break
                        break

            # Fin de la distribution
            for player in self.players:
                if player == self.pick:
                    player.drawCard(deck.drawDeck(deck.id, 2))
                else:
                    player.drawCard(deck.drawDeck(deck.id, 3))

            while len(self.player[0].cards) > 0:
                pass
            # coder le tour de belote
