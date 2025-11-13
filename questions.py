rank = {1:"Freshman", 2:"Sophmore", 3:"Junior", 4:"Senior"}
while True:

   try: 
       x = int(input("Enter the # of years in the school (1-4): "))

       if x in rank:
          print(f"Year {x} = {rank[x]} ")
       else:
          print("Invalid year number, Please enter again.")
    

   except:
          print("Invalid input")