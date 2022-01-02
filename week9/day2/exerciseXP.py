# Exercise 1
# Returns absolute value, meaning it removes the negative sign.
# float = -54.26 
# print(f"Absolute value of float is: {abs(float)}") 

# Converts the specified value into an integer(whole) number.
# print(f"int(225.25) is: {int(225.25)}")

# Allows user input
# num = input ("Enter number : ")
# print(num)
# name1 = input("Enter name : ")
# print(name1)

# __doc__ provides a documentation of the object.
# class Dog:
#     """Your best friend."""
#     def do_nothing(self):
#         pass
# print(Dog.__doc__)
# -----------------------------------------------------------------------------------------------------------
# Exercise 2

class Currency:
    def __init__(self, currency: str, value: int):
        self.currency = currency
        self.value = value
    
    def __str__(self):
        return f"{self.value} {self.currency}"
        
    def __int__(self):
        return self.value

    def __repr__(self):
        return f"{self.value} {self.currency}" 

    def __add__(self, other):
        if isinstance(other, int):
            return Currency(self.currency, (self.value + other))
        elif isinstance(other, Currency):
            if other.currency is not self.currency:
               raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
            else:
               return Currency(self.currency, (self.value + other.value))

c1 = Currency("dollar", 5)
c2 = Currency("dollar", 10)
c3 = Currency("shekel", 1)
c4 = Currency("shekel", 10)

print(str(c1))

print(int(c1))

print(repr(c1))

print(c1 + 5)

print(c1 + c2)

print(c1)

c1 += 5
print(c1)

c1 += c2
print(c1)

print(c1 + c3)