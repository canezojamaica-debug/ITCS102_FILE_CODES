n = 5

for x in range(n):
    for y in range(0, n - x - 1):
        print(" ", end="")
    for z in range(0, x+1):
        print("* ", end="")
    print()

    
