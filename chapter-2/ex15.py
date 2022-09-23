n=eval(input("Enter a number to specify height: "))

print(" "*n+" *")
for i in range(n):
    temp = 1
    if n-i-1 == n//2:
        print((n-i) * ' ' + 1 * '*' + 2*(temp+i) * '*' + 1 * '*')
    else:
        print((n-i) * ' ' + 1 * '*' + 2*(temp+i) * ' ' + 1 * '*')
