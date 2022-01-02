# Exercise 1
# class Pets:
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())


# class Cat:
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'


# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# class Sphynx(Cat):
#     def __missing__(self, sounds):
#         return f'{sounds}'


# cat1 = Bengal("Sammy", 2)
# cat2 = Chartreux("Lola", 5)
# cat3 = Sphynx("Hairless", 3)

# my_cats = [cat1, cat2, cat3]
# my_pets = my_cats[2]

# for cat in my_cats:
#     print(cat.walk())
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 2
# class Dog:
#     def __init__(self, dog_name, dog_age, dog_weight):
#         self.name = dog_name
#         self.age = dog_age
#         self.weight = dog_weight

#     def bark(self):
#         return f'{self.name} is barking.'

#     def run_speed(self):
#         return self.weight / self.age * 10

#     def fight(self, other_dog):
#         if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
#             print(f"{self.name} has won the fight!")
#         else:
#             print(f"{other_dog.name} has won the fight!")


# dog1 = Dog("Buster", 2, 10)
# dog2 = Dog("Menace", 5, 75)
# dog3 = Dog("Milky", 10, 4)

# print(dog3.bark())
# print(dog1.run_speed())
# dog2.fight(dog1)
# dog1.fight(dog3)
# --------------------------------------------------------------------------------------------------------------------------------------------------
# Exercises 3
import random

class Dog:
    def __init__(self, dog_name, dog_age, dog_weight):
        self.name = dog_name
        self.age = dog_age
        self.weight = dog_weight

    def bark(self):
        return f'{self.name} is barking.'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            print(f"{self.name} has won the fight!")
        else:
            print(f"{other_dog.name} has won the fight!")


class PetDog(Dog):
    def __init__(self, dog_name, dog_age, dog_weight, trained=False):
        self.trained = trained
        super().__init__(dog_name, dog_age, dog_weight)

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        print(f"{self.name,', '.join(list(args))} all play together!")

    def do_a_trick(self):
        tricks = [f"{self.name} does a barrel roll.",
                  f"{self.name} stands on his back legs.",
                  f"{self.name} shakes your hand.",
                  f"{self.name} plays dead."]
        print(random.choice(tricks)) if self.trained else print(f"{self.name} is not trained!")


dog1 = PetDog("Buster", 2, 8)
dog2 = PetDog("Lany", 4, 12)
dog1.train()
dog1.play("Menace", "Milky", "Panda")
dog2.play("Buster", "Menace", "Milky", "Panda")
dog1.do_a_trick()
dog2.do_a_trick()