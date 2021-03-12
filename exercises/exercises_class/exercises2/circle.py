from shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        # store the circle objects radius
        self.radius = radius


    def area(self):
        # calculate area and return it
        area = math.pi * pow(self.radius, 2)
        return f"Circles area is: {area}!"

    def circumference(self):
        # calculate the circumference and return it
        circumference = 2 * math.pi * self.radius
        return f"Circumference of the circle is. {circumference}"
