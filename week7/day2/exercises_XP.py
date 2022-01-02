# Exercise 1
# def display_message():
#     print("In this course, I am learning Python and web development!")
#
# display_message()
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 2
# def favorite_book(title):
#     print(f"One of my favorite books is {title}!")
#
# favorite_book("Game of Thrones")
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 3
# def describe_city(city, country="Argentina"):
#     print(f"{city} is in {country}.")
#
# describe_city("Buenos Aires")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4
# import random
#
# def random_number(a):
#     b = random.randint(1, 101)
#     if a == b:
#         print("We picked the same number!")
#     else:
#         print(f"Failed! We didn't pick the same number, my number is {a} and yours is {b}.")
#
# random_number(22)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 5

# def make_shirt(size, text):
#     print(f"The shirt is a {size} and the text on the shirt is {text}.")
#
# make_shirt("small", "Sailor moon is awesome!")

# def make_shirt(size="large", text="I Love Python"):
#     print(f"The shirt is a {size} and the text on it says {text}.")
#
# make_shirt()
# make_shirt("medium")
# make_shirt("small", "I love food")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 6
magicians = ["harry houdini", "david blaine", "teller"]

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

show_magicians(magicians)

def make_great(magicians):
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + " the Great"
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

make_great(magicians)
show_magicians(magicians)