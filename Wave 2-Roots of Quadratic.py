import math

# inputs

a = input("Enter your a value of the function: ")
a = int(a)
b = input("Enter your b value of the function: ")
b = int(b)
c = input("Enter your c value of the function: ")
c = int(c)

# check how many real root(s) the function have and calculate the value of the root(s)

if a == 0:
    print("The value for your a is invalid")
else:
    while b ** 2 - 4*a*c < 0:
        print("This function have no real root")
        break
    while b ** 2 - 4*a*c == 0:
        root = -b / (2*a)
        print("This function have 1 real root")
        print("The value of the root of this function is: " + str(root))
        break
    while b ** 2 - 4*a*c > 0:
        root_1 = (-b + math.sqrt(b ** 2 - 4*a*c)) / (2*a)
        root_2 = (-b - math.sqrt(b ** 2 - 4*a*c)) / (2*a)
        print("This function have 2 real roots")
        print("The value of the first root is: " + str(root_1))
        print("The value of the second root is: " + str(root_2))
        break
