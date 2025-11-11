import math

try:
       
    numerator = float(input("Enter a numerator: "))
    denominator = float(input("Enter a denominator: "))

    if denominator == 0:
        raise ZeroDivisionError
    
    remainder = math.fmod(numerator, denominator)

    print(f"{int(numerator)} mod {int(denominator)} = {int(remainder)}")

except ZeroDivisionError:
    print("Denominator cannot be zero. Exiting the quiz")

except ValueError:
    print("Invalid value")