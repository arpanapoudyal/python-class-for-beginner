n=eval(input("Enter a number to specify height: "))

for rows in range (n,0,-1):
    for colums in range(rows):
        print("*", end=" ")
    print()