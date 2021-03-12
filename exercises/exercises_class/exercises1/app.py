from circle import Circle

def main():
    # Create a circle and test it
    circle1 = Circle(5)
    print(circle1.area())
    print(circle1.circumference())
    circle2 = Circle(10)
    print(circle2.area())
    print(circle2.circumference())

if __name__ == "__main__":
  main()