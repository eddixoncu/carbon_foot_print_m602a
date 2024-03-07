class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width) * 2


r = Rectangle(4, 2)
print(f'area is {r.area()} and perimeter is {r.perimeter()}')
