from pokemon import *
from combat import *
from type_normal import *
from type_eau import *
from type_feu import *
from type_terre import *

class Main:

    def __init__(self):
        self.pokemon1 = None
        self.pokemon2 = None
        self.finished = False

    def start(self):
        while not self.finished:
            print("Bienvenue dans le jeu Pokemon !")
            print("Que souhaitez-vous faire ?")
            print("1. Choisir le Pokemon")
            print("2. Lancer le combat")
            print("3. Quitter le jeu")
            choice = input("Entrez le numéro correspondant :")

            if choice == "1":
                self.choose_pokemon()
            elif choice == "2":
                self.start_combat()
            elif choice == "3":
                self.finished = True
            else:
                print("Choix invalide, veuillez réessayer.")

    def choose_pokemon(self):
        print("Choix du premier Pokemon :")
        nom1 = input("Entrez le nom du Pokemon :")
        type1 = input("Entrez le type de Pokemon (normal/feu/eau/terre) :")
        self.pokemon1 = self.create_pokemon(nom1, type1)

        print("Choix du deuxième Pokemon :")
        nom2 = input("Entrez le nom du Pokemon :")
        type2 = input("Entrez le type de Pokemon (normal/feu/eau/terre) :")
        self.pokemon2 = self.create_pokemon(nom2, type2)

    def create_pokemon(self, nom, type):
        if type == "normal":
            return Normal(nom)
        elif type == "feu":
            return Feu(nom)
        elif type == "eau":
            return Eau(nom)
        elif type == "terre":
            return Terre(nom)
        else:
            print("Type de pokemon invalide, le Pokemon sera donc NORMAL.")
            return Normal(nom)

    def start_combat(self):
        if self.pokemon1 is None or self.pokemon2 is None:
            print("Veuillez choisir les Pokemon avant de lancer le combat.")
            return

        combat = Combat(self.pokemon1, self.pokemon2)

        while True:
            attacking_pokemon, defending_pokemon = combat.get_attacking_pokemon()
            attacking_type = type(attacking_pokemon).__name__.lower()
            defending_type = type(defending_pokemon).__name__.lower()

            eficacite = combat.get_pokemon_attack(attacking_pokemon, defending_pokemon)

            print(attacking_pokemon.get_nom(), "attaque", defending_pokemon.get_nom(), "et lui inflige", attacking_pokemon.attaque * eficacite, "points de damage.")
            defending_pokemon.set_pv(defending_pokemon.get_pv() - attacking_pokemon.attaque * eficacite)

            winner = combat.check_winner()
            if winner:
                print(winner.get_nom(), "a gagné le combat !")
                break

            input("Appuyer sur Entrée pour continuer le combat.")