import math

h = float(input("Enter the house height: "))
a = float(input("Enter the ladder angle: "))

l = h / math.sin(math.radians(a))

print("Ladder length needed:", l)
