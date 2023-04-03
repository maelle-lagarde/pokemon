from pokemon import *

class Combat(Pokemon):

    def __init__(self, pokemon1, pokemon2):
        Pokemon.__init__(self, name, pokemon_type)
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def is_dead(self):
        if self.pokemon1.get_pv() <= 0:
            print(f"{self.pokemon1.get_name()} is dead!")
            print(f"{self.pokemon2.get_name()} wins!")
        elif self.pokemon2.get_pv() <= 0:
            print(f"{self.pokemon2.get_name()} is dead!")
            print(f"{self.pokemon1.get_name()} wins!")
        else:
            return False

    def over(self):
        return self.pokemon1.is_dead() or self.pokemon2.is_dead()

    def winner(self):
        if self.pokemon1.is_dead and self.pokemon2.is_dead:
            print("Game over!")
        elif self.pokemon1.is_dead():
            print(f"{self.pokemon2.name} wins!")
        else:
            print(f"{self.pokemon1.name} wins!")

    def power_attack(self):
        type_pokemon1 = self.pokemon1.getType()
        type_pokemon2 = self.pokemon2.getType()
        attack = self.pokemon1.start_attack
        if type_pokemon1 == "Water":
            if type_pokemon2 == "Fire":
                attack *= 2
            elif type_pokemon1 == "Earth":
                attack *= 0.5
            else:
                return 1
        elif type_pokemon1 == "Fire":
            if type_pokemon2 == "Water":
                attack *= 0.5
            elif type_pokemon2 == "Earth":
                attack *= 2
            else:
                return 1
        elif type_pokemon1 == "Earth":
            if type_pokemon2 == "Water":
                attack *= 2
            if type_pokemon2 == "Fire":
                attack *= 0.5
            else:
                attack *= 1
        else:
            if type_pokemon2 == "Water":
                attack *= 1
            elif type_pokemon2 == "Fire":
                attack *= 1
            elif type_pokemon2 == "Earth":
                attack *= 1
            else:
                attack *= 0.75
        self.pokemon1.set_powerAttack(attack)
        return attack

    def loose_pv(self, pv):
        self.__pv = max(self.__pv - pv, 0)

    def round(self, pokemon1, pokemon2):
        damage = self.power_attack
        pokemon2.loose_pv(damage)
        print(f"{pokemon1.name} attacks {pokemon2.name} and inflicted him {damage} points of life!")

    def start_fight(self):
        print("Fight starting !")
        print(f"{self.pokemon1.name} vs. {self.pokemon2.name} !")

        while not self.over():
            self.round(self.pokemon2, self.pokemon2)

            if self.over():
                break

            self.round(self.pokemon2, self.pokemon1)

        print(f"The winner is {self.winner()} !")
        print("End of fight."))