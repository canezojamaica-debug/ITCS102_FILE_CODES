for x in range(7):
    for y in range(7 - x):
        print(" ", end=" ")
    for z in range(2 * x + 1):
        if z == 0 or z == 2 * x or x == 6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
