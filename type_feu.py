from pokemon import *

class Feu(Pokemon):

    def __init__(self, nom, pv=100, niveau=1):
        Pokemon.__init__(nom, pv, niveau)
        self.attaque = 12
        self.defense = 8
        self.attaque_feu = 15