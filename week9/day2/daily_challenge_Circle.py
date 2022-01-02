class Circle:
    circles = []

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return int(self.radius**2*3.14)

    def add_circles(self, other_cir):
        output = self.area() + other_cir.area()
        print(f"The sum of the two circles together is {output}")

    def if_bigger(self, other_cir):
        if self.area() > other_cir.area():
            print(f"{self.area()} is the area of the bigger circle.")
        else:
            print(f"{other_cir.area()} is the area of the bigger circle.")

    def if_equal(self, other_cir):
        if self.area() == other_cir.area():
            print(f"Both circles are equal.")
        else:
            print(f"The two circles are not equal.")

    def put_in_list(self):
        self.circles.append(self)
        self.circles.sort(key=Circle.area)
        for item in self.circles:
            print(item.area())


circle1 = Circle(12)
circle2 = Circle(7)
print(circle1.area())
print(circle2.area())
circle1.add_circles(circle2)
circle2.if_bigger(circle1)
circle1.if_equal(circle2)

circle3 = Circle(3)
circle4 = Circle(16)

circle1.put_in_list()
circle2.put_in_list()
circle3.put_in_list()
circle4.put_in_list()