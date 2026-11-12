#Task 3

for x in range (0,6):
    for y in range (0, 5):
        if x == 1 or x == 5 or x + y == 5:
            print("*", end = "")
        if x  == 2 or x == 3 or x == 4:
            print(" ", end = "")
    print()
