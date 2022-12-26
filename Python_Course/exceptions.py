import sys
try:
    x = int(input("x ="))
    y = int(input("y ="))
except ValueError:
    print("Invalid input")
    sys.exit(1)

try:
    print(f"{x}/{y} = {int(x/y)}")
except ZeroDivisionError:
    print("Cant divide by zero.")
    sys.exit(1)
