for x in range(7,0,-1):
    for y in range(x):
        print(" ", end = " ")
    for z in range(1, 7 - x + 1):
        print(z, end = " ")
    for a in range(7 - x - 1, 0, -1):
        print(a, end = " ")
    print()
