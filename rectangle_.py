class Rectangle:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle({self.x}, {self.y}, {self.width}, {self.height})'

f = Rectangle(1, 10, 50, 100)
print(f)
