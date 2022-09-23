n=eval(input("Enter a number to specify height: "))

for i in range(n):
    print(" "*(n-i)+" *"*(i+1))

for j in range(n-1):
    print(" "*(j+2)+" *"*(n-1-j))