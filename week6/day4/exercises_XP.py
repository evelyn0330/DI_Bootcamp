# Exercise 1
# my_fav_numbers = {2, 3, 30, 93}
# my_fav_numbers.add(12)
# my_fav_numbers.add(24)
# friend_fav_numbers = {5, 34, 26, 73}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)
# -----------------------------------------------------------------------------------------------------------------------
# Exercise 2
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

# No, because tuples are immutable.
# ----------------------------------------------------------------------------------------------------------------------- 
# Exercise 3
# numbers = range(1,21)
# for number in numbers:
#     print(number)
# -----------------------------------------------------------------------------------------------------------------------
# Exercise 4
# Recap – What is a float? What is the difference between an integer and a float?
# A float is a number with a decimal, while an integer is a whole number.
# num_list = []

# for num in range(3,10):
#     new_num = num/2
    
#     if str(new_num)[-1] == '0':
#         new_num = num//2
 
#     num_list.append(new_num)
# print(num_list)
# -----------------------------------------------------------------------------------------------------------------------
# Exercise 5
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# basket_count = basket.count("Apples")
# print(f"There are {basket_count} apples in the basket.")
# basket.clear()
# print(basket)
# ----------------------------------------------------------------------------------------------------------------------
# Exercise 6
# name = ''
# while name != "Evelyn":
#   name = input('What is your name? ')

# print('You put the right name!')
# ---------------------------------------------------------------------------------------------------------------------
# Exercise 7
# my_list = ["hello", "how", "are", "you", "today?"]

# for i in range(1, len(my_list),2):
#     print(my_list[i])
# --------------------------------------------------------------------------------------------------------------------
# Exercise 8
# for x in range(1500,2501):
#   if (x%5==0) and (x%7==0):
#    print(x)
# ---------------------------------------------------------------------------------------------------------------------
# Exercise 9
# user_favorite_fruits = input("Give me a list of your favorite fruits separated by a single space. ").split(" ")

# while True:
#     fruit_list = list(user_favorite_fruits)
#     fruit = input("Choose a fruit! ")
#     if fruit in fruit_list:
#         print("You chose one of your favorite fruits. Enjoy!")
#         break
#     else:
#         print("You chose a new fruit. I hope you enjoy.")
# --------------------------------------------------------------------------------------------------------------------
# Exercise 10
# active = True

# list_of_toppings = []
# while active:
#     topping = input("What toppings do you want on your pizza? ")
#     if topping == "quit":
#         active = False
#         topping_costs = len(list_of_toppings) * 2.5
#         print(10 + topping_costs)

#     else:
#         list_of_toppings.append(topping)
#         print("Okay, what else do you want on your pizza? ")
# ---------------------------------------------------------------------------------------------------------------------
# Exercise 11
# prompt = "How old are you? "
# prompt += "\nEnter 'quit' when you are finished. "
#
# ticket_cost = 0
# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)
#
#     if age < 3:
#         print("You get in free!")
#         ticket_cost += 0
#     elif age < 13:
#         print("Your ticket is $10.")
#         ticket_cost += 10
#     else:
#         print("Your ticket is $15.")
#         ticket_cost += 15
#
#     print(f"Your total is {ticket_cost}")

# teenager = []
# while True:
#     name = input("What's your name? When you are finished, type 'quit'. ")
#     if name == "quit":
#         break
#     age = int(input("What's your age? "))
#     if age > 21:
#         teenager.append(name)
# print(f"You {teenager} can watch this movie. ")
# ---------------------------------------------------------------------------------------------------------------------
# Exercise 12
# names = ["Evelyn", "Angela", "Monica", "Diane"]

# for name in names:
#     age = int(input(f"Hello {name}, How old are you? "))
#     if (age <= 16):
#        names.remove(name)

# print(names)
# ---------------------------------------------------------------------------------------------------------------------
# Exercise 13
# sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'tuna']
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print("I'm working on your " + current_sandwich + " sandwich.")
#     finished_sandwiches.append(current_sandwich)

# print("\n")
# for sandwich in finished_sandwiches:
#     print("I made a " + sandwich + " sandwich.")
# --------------------------------------------------------------------------------------------------------------------
# Exercise 14
# sandwich_orders = [
#     'pastrami', 'veggie', 'grilled cheese', 'pastrami',
#     'turkey', 'tuna', 'pastrami']
# finished_sandwiches = []

# print("I'm sorry, we're all out of pastrami today.")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# print("\n")
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print("I'm working on your " + current_sandwich + " sandwich.")
#     finished_sandwiches.append(current_sandwich)

# print("\n")
# for sandwich in finished_sandwiches:
#     print("I made a " + sandwich + " sandwich.")
