#Finding area and circumference of a circle using radius.
class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
        self.area=Circle.pi*radius*radius
        self.circumference=2*Circle.pi*radius
        
circle1 = Circle(4)
print(circle1.area)
print(circle1.circumference)