import random


class Main:

    def __init__(self):
        pass

    def choose_pokemon(self):
        while True:
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("Welcome to the pokemon game !")
            print("Choose your pokemon :")
            print("1. Salamèche (Fire)")
            print("2. Carapuce (Water)")
            print("3. Bulbizarre (Earth)")
            print("4. Rattata (Normal)")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            choix = input("Enter the corresponding number : ")
            if choix == "1":
                return Normal
            elif choix == "2":
                return Water
            elif choix == "3":
                return Earth
            elif choix == "4":
                return Normal
            else:
                print("Invalid choice, try again.")
                break
        return True

    def start(self):
        pokemon1 = Main.choose_pokemon
        pokemon2 = random.choice([Fire, Water, Earth, Normal]) #
        combat = Combat(pokemon1, pokemon2)
        combat.start_fight()

start_the_game = Main
start_the_game.choose_pokemon()