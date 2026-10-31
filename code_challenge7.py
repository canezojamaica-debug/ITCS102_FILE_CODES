#triangle

rows = int(input("Input the number of rows: "))
counter = 1

for x in range(0, rows, 1):
    for y in range(-1, x):
        print(counter, end=" ")
        counter = counter + 1
    print()
