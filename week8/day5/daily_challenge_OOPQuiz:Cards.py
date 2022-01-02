# Part 1 : Quiz:

# Answer the following questions

# 1.What is a class?
#   A class is a blueprint for objects- one class for any number of objects of that type.

# 2.What is an instance?
#   An instance is an individual object of a certain class.

# 3.What is encapsulation?
#   Encapsulation is when access to methods and variables is restricted to prevent data from direct modification.

# 4.What is abstraction?
#   Abstraction hides the internal functionality of the function from users.

# 5.What is inheritance?
#   Inheritance is the process by which one class takes on the attributes and methods of another.

# 6.What is multiple inheritance?
#   Multiple inheritance is when a class can be derived from more than one base class.

# 7.What is polymorphism?
#   Polymorphism is when you define methods in the child class that have the same names as the methods in the parent class.

# 8.What is method resolution order or MRO?
# MRO is a concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy and is especially useful in Python because Python supports multiple inheritance.
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Part 2: Create A Deck Of Cards Class
import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r], = self.cards[r], self.cards[i]

    def deal(self):
        return self.cards.pop()


deck = Deck()
deck.shuffle()


card = deck.deal()
card.show()