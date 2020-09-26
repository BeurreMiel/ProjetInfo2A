class Card:

    def __init__(self, valeur=None, couleur=None,code =None):
        self.valeur = valeur,
        self.couleur = couleur, 
        self.code = code

    def __str__(self): 
        data = (self.valeur,self.couleur)
        return("{} de {}".format(*data))

    def __eq__(self,autrecarte): 
        if isinstance(autrecarte, Card):
            return(self.valeur == autrecarte.valeur) and (self.couleur == autrecarte.couleur)
        raise TypeError("La comparaison n'est possible qu'entre deux cartes")

    def compareRank(self, autrecarte):
        if isinstance(autrecarte, Card):
            return(self.valeur < autrecarte.valeur)
        raise TypeError("La comparaison n'est possible qu'entre deux cartes")

    def compareColor(self, autrecarte):
        if isinstance(autrecarte, Card):
            return(self.couleur == autrecarte.couleur)
        raise TypeError("La comparaison n'est possible qu'entre deux cartes")
