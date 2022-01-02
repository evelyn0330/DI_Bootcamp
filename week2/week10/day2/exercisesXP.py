# Exercise 1
# import addition

# print(addition.add(345,445))
# ----------------------------------
# from addition import sub

# print(sub(65,30))
# ---------------------------------
# from addition import add as a

# print(a(23,56))
# ----------------------------------
# import addition as add

# print(add.sub(100,10))
# ------------------------------------------------------------------------------------------------

# Exercise 2
# import random

# def roll_random_num(num):
#     ran_num = random.randint(1,101)
#     if num == ran_num:
#         print("You got it!")
#     else:
#         print("Try again")

# roll_random_num(35)
# -----------------------------------------------------------------------------------------------

# Exercise 3
import random
import string

def Upper_lower_string(length):
    result = ''.join((random.choice(string.ascii_letters) for x in range(length)))
    print(result)
  
Upper_lower_string(5)