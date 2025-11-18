
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Width: {self.width}, Height: {self.height}"

r1 = Rectangle()
r2 = Rectangle(11, 12)



print(r1)
print(r2)



    



    
