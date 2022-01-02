class Family:
    def __init__(self, last_name: str):
        self.members = [{'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
                        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}]
        self.last_name = last_name

    def born(self, **kwargs):
        new_member = {}
        for key, value in kwargs.items():
            new_member[key] = value
        self.members.append(new_member)
        print("Congratulations on your new addition to the family!")

    def is_18(self, name):
        for member in self.members:
            if name in member['name'] and member['age'] >= 18:
                return True
            else:
                return False

    def print_members(self):
        for member in self.members:
            print(member['name'])


# family1 = Family("Pello")
# family1.print_members()
# family1.born(name="Adriel", age=0, gender="Male", is_child=True)
# family1.print_member()
# print(family1.is_18("Adriel"))
# -----------------------------------------------------------------------------------------------------------------
# Exercise 2
class TheIncredibles(Family):
    def __init__(self, last_name: str):
        self.last_name = last_name
        self.members = [{'name': 'Robert', 'age': 40, 'gender': 'Male', 'is_child': False, 'power':'Superhuman strength,stamina,durability', 'incredible_name':'Mr.Incredible'},
                        {'name': 'Helen', 'age': 38, 'gender': 'Female', 'is_child': False, 'power':'Elasticity', 'incredible_name':'Elastigirl'},
                        {'name': 'Violet', 'age': 14, 'gender': 'Female', 'is_child': True, 'power': 'Force field,Invisibility','incredible_name':'Violet'},
                        {'name': 'Dash', 'age': 10, 'gender': 'Male', 'is_child': True, 'power': 'Superspeed','incredible_name': 'Dash'}]


    def use_power(self):
       for member in self.members:
           if member['age']>=18:
               print(member['name'])
           raise Exception(f"{member['name']} is not 18 years old yet!")

    def incredible_presentation(self):
        for member in self.members:
            print(f"This is {member['incredible_name']} and their power is {member['power']}")


family2 = TheIncredibles("Parr")
family2.print_members()
family2.born(name = 'Jack',age = '1',gender = 'Male',is_child = True,power = 'unknown',incredible_name = 'Jack Jack')
family2.print_members()
family2.incredible_presentation()




