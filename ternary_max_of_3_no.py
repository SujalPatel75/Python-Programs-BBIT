a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))
c = float(input("Enter the value for c: "))

max = a if (a > b and a > c) else (b if b > c else c)

print("The maximum value is:", max)
