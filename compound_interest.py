p = float(input("Enter Principal Amount: "))
r = float(input("Enter Annual Interest Rate: "))
t = float(input("Enter Time Period (years): "))
n = float(input("Enter the Number of Times Interest is Compounded per Year: "))

compound_interest = p * (1 + r/n)**(n*t)

print("Compound Interest: ", compound_interest)
