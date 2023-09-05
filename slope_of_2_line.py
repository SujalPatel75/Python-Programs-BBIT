x1 = float(input("Enter x-coordinate of the first point: "))
y1 = float(input("Enter y-coordinate of the first point: "))
x2 = float(input("Enter x-coordinate of the second point: "))
y2 = float(input("Enter y-coordinate of the second point: "))
     
slope = (y2 - y1) / (x2 - x1)

if x1 == x2:
    print("Error ")

else:
    print("Slope of given coordinates: ", slope)


