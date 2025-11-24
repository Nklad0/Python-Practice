NYCT = {"N": "Astoria-Ditmars Blvd to Coney Island", 
        "Q": "96 St-2 Av to Coney Island", 
        "R": "Forest Hills-71 Av to Bay Ridge-95 St", 
        "W": "Astoria-Ditmars Blvd to Whitehall St"}

print("Using items():")
for key, value in NYCT.items():
    print(key, ":", value)

NYCT.update({"N": "Astoria-Ditmars Blvd to Gravesend-86 St"})

print("\nUsing keys():")
for key in NYCT.keys():
    print(key, ":", NYCT[key])

NYCT["E"] = "Reroute - Jamaica Center to Whitehall St"

print("\nUsing values():")
for value in NYCT.values():
    print(value)

del NYCT["W"]
NYCT.pop("Q")

print(NYCT)

