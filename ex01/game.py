class GotCharacter:

    def __init__(self, first_name, is_alive=True,
                 family_name="", house_words=""):
        self.first_name = first_name
        self.family_name = family_name
        self.is_alive = is_alive
        self.house_words = house_words

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


class Stark(GotCharacter):

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"


class Lannister(GotCharacter):

    def __init__(self, first_name=None, is_alive=True, family_name="",
                 house_words=""):
        super().__init__(first_name, is_alive, family_name="Lannister",
                         house_words="A lannister always pays his debts")

    def principe_de_vie(self):
        print("Ca vaaaaa, c'est pas ma soeur c'est ma belle soeuuuuur")


arya = Stark("Arya")
print(arya.__dict__)

Jaime = Lannister("Jaime", "test", "A lannister always pays his debts")
Jaime.print_house_words()
print(Jaime.family_name + Jaime.is_alive)

arya.print_house_words()
print(arya.is_alive)
arya.die()
print(arya.is_alive)
