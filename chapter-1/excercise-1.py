# 1. Print a box like the one below.
# *******************
# *******************
# *******************
# *******************

# Method 1: Simple Method
# print('*******************')
# print("*******************")
# print("*******************")
# print("*******************")

# Method 2: Using For Loop

# for x in range(4):
#     print('*******************')


# Method 3: Using 2 For Loop

for x in range(4):
    for i in range(19):
        print("*", end = '')
    print()    

# print("*", end = '')
# print("*")

# print("*")
# print("*")