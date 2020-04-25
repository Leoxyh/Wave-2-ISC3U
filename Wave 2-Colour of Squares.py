import math

# input the column number and the the row letter

row = input("Enter the row letter: ")
column = input("Enter the column number:")
row = int(row, 36)
column = int(column, 10)

# calculate the square is black or white

while row % 2 == 0:
    if column % 2 == 0:
        print("The colour of this square is white")
        break
    else:
        print("The colour of this square is black")
        break
while row % 2 == 1:
    if column % 2 == 1:
        print("The colour of this square is white")
        break
    else:
        print("The colour of this square is black")
        break
