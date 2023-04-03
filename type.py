from pokemon import *

class Type(Pokemon):

    def __init__(self):
        Pokemon.__init__()
        self.pokemon_type = ""

    def pokemonType(self):
        if self.player == "Salamèche":
            self.pokemon_type = "Fire"
        elif self.player == "Carapuce":
            self.pokemon_type = "Water"
        elif self.player == "Bulbizarre":
            self.pokemon_type = "Earth"
        elif self.player == "Rattata":
            self.pokemon_type = "Normal"
        else:
            return False

    # initialise les points d'attaque et de défense en fonction du type de pokemon.
    def powerpokemonType(self):
        self.pokemonType()
        if self.pokemon_type == "Fire":
            Pokemon.set_pv(self, 100)
            self.start_attack = 50
            self.defense = 10

        if self.pokemon_type == "Water":
            Pokemon.set_pv(self, 100)
            self.start_attack = 30
            self.defense = 20

        if self.pokemon_type == "Earth":
            Pokemon.set_pv(self, 100)
            self.start_attack = 20
            self.defense = 40

        if self.pokemon_type == "Normal":
            Pokemon.set_pv(self, 100)
            self.start_attack = 40
            self.defense = 30

    def getType(self):
        return self.pokemon_type