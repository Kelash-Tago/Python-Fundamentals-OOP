# class shape with area method subclasses rectangle,triangle and circle with overriden method area

class Shape:
    def area(self):
        print("Area printed")
class Triangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print("Area of triangle is: ",(self.width*self.length)/2)

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print(f"Area of rectangle is : {self.length*self.width}")


class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f"Area of circle is : {self.radius**2*3.14}")



triangle=Triangle(3,4)
triangle.area()
rectangle=Rectangle(3,4)
rectangle.area()
circle=Circle(3)
circle.area()