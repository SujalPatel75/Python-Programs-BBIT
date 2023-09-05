weight = float(input("Enter your weight(in kg): "))
height = float(input("Enter your height(in cm): "))

height_meter = height/100

bmi = weight/(height_meter**2)

if bmi >= 19 and bmi <= 25:
    print(f"You are healthy and your BMI is: {bmi:.3f}")
elif bmi < 19:
    print(f"You are underweight and your BMI is: {bmi:.3f}")
elif bmi > 25:        
    print(f"You are overweight and your BMI is: {bmi:.3f}")
else:
    print("You have entered wrong information")    
