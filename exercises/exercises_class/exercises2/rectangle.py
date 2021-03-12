from shape import Shape

class Rectangle(Shape):
    def __init__(self, points):
        self.points = points

    def area(self):
        area = self.width() * self.height()
        return f"The area of the rectangle is: {area}"

    def width(self):
        width = self.points[1].column - self.points[0].column
        return width

    def height(self):
        height = self.points[3].row - self.points[0].row
        return height