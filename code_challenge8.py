#diamond
rows = 7

for x in range (rows):
    for y in range (0, rows - x - 1):
        print(" ", end = "")
    for z in range (0, x+1):
        print("* ", end= "")
    print()

for x in range (rows):
    for y in range (0, x+1):
        print(" ", end= "")
    for z in range (0, rows - x - 1):
        print("* ", end = "")
    print()
