'''Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.'''


class Circle:

    def __init__(self, r):
        self.radius = r

    def area(self):
        print(self.radius **2 *3.14)

circle= Circle(2)
circle.area()
