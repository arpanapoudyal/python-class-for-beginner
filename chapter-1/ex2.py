# ---
print("\n<Method 1: Simple Method>\n")
# ---

print('*******************')
print('*                 *')
print('*                 *')
print("*******************")

# ---
print("\n<Method 2: Using 1 Loop>\n")
# ---

for x in range(4):
    if (x == 1 or x == 2):
        print('*                 *')
    else:
        print('*******************')

# ---
print("\n<Method 3: Using 2 Loop>\n")
# ---

for x in range(4):
    for y in range(19):
        if ((x == 1 or x == 2) and (y > 0 and y < 18)):
            print(' ', end='')
        else:
            print('*', end='')
    print()
