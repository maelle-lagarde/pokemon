class Pokemon:

    def __init__(self, nom, pv=100, niveau=1, attaque=0, defense=0):
        self.__nom = nom
        self.__pv = pv
        self.niveau = niveau
        self.attaque = attaque
        self.defense = defense

    def get_nom(self):
        return self.__nom

    def get_pv(self):
        return self.__pv

    def set_pv(self, new_pv):
        self.__pv = new_pv

    def display_info(self):
        print("Nom :", self.get_nom())
        print("PV :", self.get_pv())
        print("Attaque : ", self.attaque)
        print("Défense :", self.defense)