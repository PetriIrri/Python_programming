from circle import Circle
from rectangle import Rectangle
from point import Point

def main():
    points = []
    points.append(Point(0,0))
    points.append(Point(0,5))
    points.append(Point(3,0))
    points.append(Point(3,5))
    rectangle1 = Rectangle(points)
    print("The width of the rectangle is:", rectangle1.width())
    print("The height of the rectangle is:", rectangle1.height())
    print(rectangle1.area(), "\n")
    points = []
    points.append(Point(0,0))
    points.append(Point(0,9))
    points.append(Point(6,0))
    points.append(Point(6,9))
    rectangle2 = Rectangle(points)
    print("The width of the rectangle is:", rectangle2.width())
    print("The height of the rectangle is:", rectangle2.height())
    print(rectangle2.area())

if __name__ == "__main__":
  main()