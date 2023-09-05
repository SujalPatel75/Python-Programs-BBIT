h = float(input("Enter hours worked: "))
r = float(input("Enter hourly rate: "))

if h > 40:
    total_wages = 40 * r + (h - 40) * r * 1.5
else:
    total_wages = h * r

print("Total weekly wages: ", total_wages)
