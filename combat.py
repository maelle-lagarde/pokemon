from pokemon import *

class Combat():

    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def check_winner(self):
        if self.pokemon1.get_pv() <= 0:
            return self.pokemon2
        elif self.pokemon2.get_pv() <= 0:
            return self.pokemon1
        else:
            return False

    def get_pokemon_attack(self, attacking_pokemon, defending_pokemon):
        attacking_type = type(attacking_pokemon).__name__
        defending_type = type(defending_pokemon).__name__
        if attacking_type == "Eau":
            if defending_type == "Feu":
                return 2
            elif defending_type == "Terre":
                return 0.5
            else:
                return 1
        elif attacking_type == "Feu":
            if defending_type == "Eau":
                return 0.5
            elif defending_type == "Terre":
                return 2
            else:
                return 1
        elif attacking_type == "Terre":
            if defending_type == "Eau":
                return 2
            if defending_type == "Feu":
                return 0.5
            else:
                return 1
        elif:
            if defending_type == "Eau":
                return 1
            elif defending_type == "Feu":
                return 1
            elif defending_type == "Terre":
                return 1
            else:
                return 1
        else:
            return 0.75

    def attack_pokemon(self, attacking_type, defending_type):
        attacking_pokemon = None
        defending_pokemon = None
        if attacking_type == "pokemon1":
            attacking_pokemon = self.pokemon1
            defending_pokemon = self.pokemon2
        elif attacking_type == "pokemon2":
            attacking_pokemon = self.pokemon2
            defending_pokemon = self.pokemon1
        else:
            return False
        attack_multiplier = self.get_pokemon_attack(attacking_pokemon, defending_pokemon)
        damage = int((attacking_pokemon.attaque * attack_multiplier) - defending_pokemon.defense)
        if damage < 1:
            damage = 1
        defending_pokemon.set_pv(defending_pokemon.get_pv() - damage)
        print(attacking_pokemon.get_nom(), "a infligé", damage, "points de damage à", defending_pokemon.get_nom())
        winner = self.check_winner()
        if winner:
            print(winner.get_nom(), "a gagné le combat !")
        else:
            print(defending_pokemon.get_nom(), "a maintenant", defending_pokemon.get_pv(), "points de vie.")