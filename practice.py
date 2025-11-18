
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def display_info(self):
        print(f"Width:", self.width) 
        print(f"Height:", self.height)

r1 = Rectangle(0, 0)
r2 = Rectangle(11, 12)

r1.display_info()
r2.display_info()

print("Width of r1:", r1.width)
print("Width of r2:", r2.height)


    



    
