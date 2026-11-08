for x in range(5):
    for y in range(9):
        if x + y == 4 or x + y == 8 or (x == 0 and y >= 4) or (x == 4 and y <= 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
