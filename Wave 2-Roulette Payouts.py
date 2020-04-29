import random
number = random.randint(0, 37)
number = int(number)
red = [1, 2, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green = [0, 37]
if number in red:
    if number > 0 and number < 19:
        if number % 2 == 0:
            print("The spin resulted in " + str(number) + "...")
            print("Pay", number)
            print("Pay red")
            print("Pay even")
            print("Pay 1 to 18")
        else:
            print("The spin resulted in " + str(number) + "...")
            print("Pay", number)
            print("Pay red")
            print("Pay odd")
            print("Pay 1 to 18")
    if number < 37 and number > 18:
        if number % 2 == 0:
            print("The spin resulted in " + str(number) + "...")
            print("Pay", number)
            print("Pay red")
            print("Pay even")
            print("Pay 19 to 36")
        else:
            print("The spin resulted in " + str(number) + "...")
            print("Pay", number)
            print("Pay red")
            print("Pay odd")
            print("Pay 19 to 36")
elif number in black:
    if number > 0 and number < 19:
        if number % 2 == 0:
            print("The spin resulted in " + str(number) + "...")
            print("Pay", number)
            print("Pay black")
            print("Pay even")
            print("Pay 1 to 18")
        else:
            print("The spin resulted in " + str(number) + "...")
            print("Pay", number)
            print("Pay black")
            print("Pay odd")
            print("Pay 1 to 18")
    elif number < 37 and number > 18:
        if number % 2 == 0:
            print("The spin resulted in " + str(number) + "...")
            print("Pay", number)
            print("Pay black")
            print("Pay even")
            print("Pay 19 to 36")
        else:
            print("The spin resulted in " + str(number) + "...")
            print("Pay", number)
            print("Pay black")
            print("Pay odd")
            print("Pay 19 to 36")
elif number in green:
    if number == 0:
        print("the spin result in 0...")
        print("Pay 0")
    elif number == 37:
        print("the spin result in 00...")
        print("Pay 00")
