x1 = float(input("Enter Principal Amount: "))
y1 = float(input("Enter Rate of Interest: "))
x2 = float(input("Enter Time Period (years): "))


y1 = y1 / 100

simple_interest = (x1 * y1 * x2)

print("Simple Interest: ", simple_interest)
