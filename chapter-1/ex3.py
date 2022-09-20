# ---
print("\n<Method 1: Simple Method>\n")
# ---

print('*')
print('**')
print('***')
print("****")

# ---
print("\n<Method 2: Using 1 Loop>\n")
# ---

for x in range(4):
    if x == 0:
        print("*")
    elif x == 1:
        print("**")
    elif x == 2:
        print("***")
    elif x == 3:
        print("****")


# ---
print("\n<Method 3: Using 2 Loop>\n")
# ---

for x in range(1, 5):
    for y in range(x):
        print('*', end='')
    print()
