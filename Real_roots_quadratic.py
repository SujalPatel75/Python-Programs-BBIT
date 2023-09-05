import math

print("Enter coefficients a, b, and c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

d = b * b - 4 * a * c


r1 = (-b + math.sqrt(d)) / (2 * a)
r2 = (-b - math.sqrt(d)) / (2 * a)
print("Root 1:", r1)
print("Root 2:", r2)

# if a == 0:
#     print("Not a quadratic equation")
# elif d > 0:
#     print("Real and different roots")
#     r1 = (-b + math.sqrt(d)) / (2 * a)
#     r2 = (-b - math.sqrt(d)) / (2 * a)
#     print("Root 1:", r1)
#     print("Root 2:", r2)
# elif d == 0:
#     print("Real and same root")
#     r = -b / (2 * a)
#     print("Root:", r)
# else:
#     print("Complex roots")
#     rp = -b / (2 * a)
#     ip = math.sqrt(abs(d)) / (2 * a)
#     print("Root 1:", rp, "+", ip, "i")
#     print("Root 2:", rp, "-", ip, "i")
