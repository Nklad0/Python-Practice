# Writing a text to a file called "example.txt"
try:
    with open("museums.txt", "w", encoding="utf-8") as f:
        f.write("AMNH\n")
        f.write("The Met")
except: IOError
print(f"Failed to read file:")


try:
    with open("planes.txt", "w", encoding="utf-8") as f:
        f.write("Boeing 737\n")
        f.write("Boeing 747\n")
except: IOError
print(f"Please try again")