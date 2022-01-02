# Exercise 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# output_dict = {}
# for key, value in zip(keys, values):
#     output_dict.update({key: value})
#
# print(output_dict)
# ----------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# total = 0
#
# for name, age in family.items():
#     if age < 3:
#         continue
#     if 3 <= age <= 12:
#         total += 10
#     if age > 12:
#         total += 15
#
# print(f'The total for the family is {total}.')
# ---------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 3
# brand = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": "men, women, children, home ",
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 2,
#     "major_color": {
#         "France": "blue",
#         "Spain": "red",
#         "US": "pink, green"
#     }
# }

# brand["number_stores"] = 2
# print("Zara's clients are:",brand["type_of_clothes"])
# brand["country_creation"] = "Spain"

# if "international_competitors" in brand.keys():
#     brand["international_competitors"].append("Desigual")

# del brand["creation_date"]
# print(brand["international_competitors"][3])
# print(brand["major_color"]["US"])
# print(len(brand))
# print(brand.keys())

# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000
# }

# brand.update(more_on_zara)
# print(brand["number_stores"])
# it shows the one added
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4
# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# for index, user in enumerate(users):
#     print(user, index)

# for index, user in enumerate(users):
#     print(index, user)

# users.sort()
# print(users)

# for index, user in enumerate(users):
#     print(user, index)

# for index, user in enumerate(users):
#     if user.startswith("I") or user.startswith("M"):
#         print(user, index)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

