floors = {0: "Lower Level", 1:"First Floor - Lobby", 2:"Second Floor", 3:"Third Floor", 4:"Fourth Floor"}
while True:
      
        try:
             x = int(input("Please enter destination floor: "))
             

             if x in floors:
                print(f"Floor {x} = {floors[x]} ") 
             else:
                print("This is not a floor")


        except:
                   
                print("Invalid floor")