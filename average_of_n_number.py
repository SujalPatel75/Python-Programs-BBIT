n = int(input("Enter the number of numbers: "))

sum = 0

for i in range(n):
    sum += int(input("Enter a number: "))
    
average = sum/n   

print("The average is", average)