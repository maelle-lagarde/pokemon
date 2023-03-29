from pokemon import *

class Eau(Pokemon):

    def __init__(self, nom, pv=100, niveau=1):
        Pokemon.__init__(nom, pv, niveau)
        self.attaque = 8
        self.defense = 12
        self.attaque_eau = 20