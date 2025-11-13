class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def display_info(self):
        print(f"Car: {self.make}, Year: {self.year}")

oldCar = Car("Mitsubishi", 2009)
newCar = Car("Honda", 2020)

oldCar.display_info()
newCar.display_info()

print("Year of Car 2:", newCar.year)
print("Year of Car 1:", oldCar.make)


    

