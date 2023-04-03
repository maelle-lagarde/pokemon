class Pokemon:

    def __init__(self, name):
        self.__name = name
        self.__pv = 100
        self.level = 1
        self.start_attack = 0
        self.defense = 0
        self.player = ""

    def display_info(self):
        print(f"Name : {self.player}")
        print(f"PV : {self.__pv}")
        print(f"Level : {self.level}")
        print(f"Attack : {self.start_attack}")
        print(f"Defense : {self.defense}")

    def get_powerAttack(self):
        attack = self.power_attack
        return attack

    def set_powerAttack(self, new_power_attack):
        self.power_attack = new_power_attack

    def get_powerDefense(self):
        defense = self.defense
        return defense

    def set_pv(self, new_pv):
        self.__pv = new_pv

    def get_pv(self):
        return self.__pv