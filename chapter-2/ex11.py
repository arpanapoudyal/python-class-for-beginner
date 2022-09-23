w=eval(input("Enter a number to specify width: "))
h=eval(input("Enter a number to specify height: "))

for rows in range(h):
    for column in range(w):
        if (rows == 0 or rows == h-1 or column == 0 or column == w-1):
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()