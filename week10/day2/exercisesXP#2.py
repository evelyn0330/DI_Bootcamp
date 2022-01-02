# Exercise 1
# from datetime import datetime

# print(datetime.date(datetime.now()))
# -----------------------------------------------------------------------------------------------------------
# Exercise 2

# import datetime

# date_now = datetime.datetime.now()
# jan_1 = datetime.datetime(2022,1,1)
# time_left = jan_1 - date_now
# print(f"{time_left} till New years!")
# ------------------------------------------------------------------------------------------------------------
# Exercise 3

# import datetime

# def time_alive():
#     birthday = datetime.datetime(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))
#     now = datetime.datetime.now()
#     difference = now - birthday
#     print(f"You've been alive for {difference}")


# time_alive()
#-------------------------------------------------------------------------------------------------------------
# Exercise 4 

# import datetime

# def today():
#     now = datetime.datetime.today()
#     next_holiday = datetime.datetime(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))
#     difference = next_holiday - now
#     print(f"Today's date is {now}\nand the next holiday is in {difference}")

# today()
# -----------------------------------------------------------------------------------------------------------
# Exercise 5

# age = int(input("How old are you in seconds? "))
# earth = age / 31557600
# mercury = earth * 0.2408467
# venus = earth * 0.61519726
# mars = earth * 1.8808158
# jupiter = earth * 11.862615
# saturn = earth * 29.447498
# uranus = earth * 84.016846
# neptune = earth * 164.79132

# print(f"You are {round(earth, 2)} Earth-years old.")
# print(f"You are {round(venus, 2)} Venus-years old")
# print(f"You are {round(mars, 2)} Mars-years old")
# print(f"You are {round(jupiter, 2)} Jupiter-years old")
# print(f"You are {round(saturn, 2)} Saturn-years old")
# print(f"You are {round(uranus, 2)} Uranus-years old")
# print(f"You are {round(neptune, 2)} Neptune-years old")
# -----------------------------------------------------------------------------------------------------------
# Exercise 6
from faker import Faker
fake = Faker()

users = []


def add_new_dict():
    user = {}
    user['name'] = fake.name()
    user['address'] = fake.address()
    user['language code'] = fake.language_code()
    users.append(user)


add_new_dict()
add_new_dict()
add_new_dict()
for user in users:
    print(user)
