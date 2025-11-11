def nameFormat(first, middle, last):
     
  first = first.title()
  middle = middle.title()
  last = last.title()

  middle_initial = middle[0] + "."

  print(f"{first} {middle_initial} {last}")



def main():

   nameFormat("john", "stu", "smith")
   nameFormat(last="kennedy", first="john", middle="fitzgerald")
   
main()