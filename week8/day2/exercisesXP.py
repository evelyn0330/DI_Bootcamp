# Exercise 1
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# cat1 = Cat("Inky", 6)
# cat2 = Cat("Luna", 8)
# cat3 = Cat("Artemis", 9)

# def oldest_cat(cat1,cat2,cat3):
#     cats = [cat1.age,cat2.age,cat3.age]
#     return max(cats)

# print(f"The oldest cat is {oldest_cat(cat1,cat2,cat3)} years old.")
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 2
# class Dog:
#     def __init__(self, dog_name, dog_height):
#         self.name = dog_name
#         self.height = dog_height

#     def bark(self):
#         print(f"{self.name} goes woof!")

#     def jump(self):
#         print(f"{self.name} jumps {self.height * 2} cm high!")


# davids_dog = Dog("Rex", 50)
# print(davids_dog.name, davids_dog.height)
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dogs = Dog("Teacup", 20)
# print(sarahs_dogs.name, sarahs_dogs.height)
# sarahs_dogs.bark()
# sarahs_dogs.jump()

# if davids_dog.height > sarahs_dogs.height:
#     print(f"{davids_dog.name} is the is the bigger dog!")
# else:
#     print(f"{sarahs_dogs.name} is the bigger dog!")
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 3
# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for item in self.lyrics:
#             print(item)


# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4
import string


class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
       for item in self.animals:
            print(item)

    def sell_animal(self, sold_animal):
        if sold_animal in self.animals:
            self.animals.remove(sold_animal)
        else:
            print("This animals does not exist in this zoo!")

    def sort_animals(self):
        for letter in list(string.ascii_uppercase):
            animals_list = [animal for animal in self.animals if animal.startswith(letter)]
            sorted_list = sorted(animals_list)
            if sorted_list:
                print(sorted_list)


ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Ape")
ramat_gan_safari.get_animals()
ramat_gan_safari.sort_animals()
