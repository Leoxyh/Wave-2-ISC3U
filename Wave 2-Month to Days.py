import math

# Inputs

print("List for months: January, February, March, April, May, June, July, August, September, October, November, December")
print("Please capitalize your first letter")
month = input("Enter your month: ")
month = str(month)

# Check the month for days

if month in ("January", "March", "May", "July", "August", "October", "December"):
    print(str(month), "have 31 days")
elif month in ("April", "June", "September", "November"):
    print(str(month), "have 30 days")
elif month == "February":
    print(str(month), "have 28 or 29 days")
else:
    print("Undefined month name")
