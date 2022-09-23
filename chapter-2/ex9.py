
n = eval(input("How many Fibonacci numbers to print: "))

first_number = 0
second_number = 1
print(first_number, end=",")
print(second_number, end=",")
for i in range(2,n):

    next_number =first_number + second_number
    first_number = second_number
    second_number = next_number

    print(next_number, end=",")

print()