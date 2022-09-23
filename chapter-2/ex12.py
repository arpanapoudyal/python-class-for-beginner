n=eval(input("Enter a number to specify height: "))

for rows in range (n):
    for colums in range(rows+1):
        print("*", end=" ")
    print()