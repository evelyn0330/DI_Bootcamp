from typing import List

class Human:
    def __init__(self, name: str, age: int, living_place = None):
        self.name = name
        self.age = age
        self.living_place = living_place

    def move(self, new_building):
        # remove from current building
        if self.living_place:
            self.living_place.remove_inhabitant(self)

        self.living_place = new_building
        new_building.inhabitants.append(self)


class Building:
    def __init__(self, address:str, inhabitants = List[Human]):
        self.address = address
        self.inhabitants = inhabitants

    def show_inhabitants_info(self):
        for inhabitant in self.inhabitants:
            print(inhabitant.name, inhabitant.age)
    
    def remove_inhabitant(self, inhabitant: Human):
        self.inhabitants.remove(inhabitant)

    def get_number_of_citizens(self):
        return len(self.inhabitants)

    def get_total_ages_of_citizens(self):
        total_ages = 0

        for inhabitant in self.inhabitants:
            total_ages += inhabitant.age

        return total_ages


class City:
    def __init__(self, name:str, buildings: List[Building]):
        self.name = name
        self.buildings = buildings

    def construct(self, address):
        new_building = Building(address, [])
        self.buildings.append(new_building)

    def info(self, address):
        counter = 0
        total_ages_of_citizens = 0
        number_of_citizens = 0

        for building in self.buildings:
            if building.address == address:
                counter += 1
                number_of_citizens += building.get_number_of_citizens()
                total_ages_of_citizens += building.get_total_ages_of_citizens()
            

        print(f" The number of buildings at the address {address} is {counter}")
        print(f"The mean age of the citizens {total_ages_of_citizens/ number_of_citizens}")

    
building1 = Building("Shoreline 46", [])
building2 = Building("Washington 1245", [])

evelyn = Human("Evelyn", 28)
adriel = Human("Adriel", 18)
maria = Human("Maria", 48)
claudio = Human("Claudio", 49)

evelyn.move(building1)
adriel.move(building1)
maria.move(building2)
claudio.move(building2)

seattle = City("Seattle", [building1, building2])
seattle.info("Shoreline 46")
seattle.info("Washington 1245")