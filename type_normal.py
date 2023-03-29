from pokemon import *

class Normal(Pokemon):

    def __init__(self, nom, pv=100, niveau=1):
        Pokemon.__init__(nom, pv, niveau)
        self.attaque = 10
        self.defense = 10