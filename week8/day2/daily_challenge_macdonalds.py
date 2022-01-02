class Farm:

    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, amount=1):
        if animal_type in self.animals:
            self.animals[animal_type] = self.animals[animal_type] + amount
        else:
            self.animals[animal_type] = amount

    def get_info(self):
        print(f"{self.farm_name}'s name\n")

        for animal_type, animal_amount in self.animals.items():
            print(f"{animal_type} : {animal_amount}")

        return "\n\tE-I-E-I-O!"

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_list = macdonald.get_animal_types()
        return f"McDonald’s farm has {animal_list[0]}s, {animal_list[1]}s and {animal_list[2]}."


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
