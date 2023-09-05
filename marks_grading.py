
marks = int(input("Enter marks of the student: "))

if marks >= 90:
    print("Grade A")
elif marks >=80 and marks <=89:
    print("Grade B")     
elif marks >= 70 and marks <=79:
    print("Grade C")
elif marks >= 60 and marks <=69:
    print("Grade D")      
elif marks >= 50 and marks <=59:
    print("Grade E")    
elif  marks <50:
    print("Grade F")   
else:
    print("Wrong input")      


# marks = int(input("Enter marks of the student: "))

# grade = match marks:
#     case 90 <= marks <= 100:
#         "Grade A"
#     case 80 <= marks < 90:
#         "Grade B"
#     case 70 <= marks < 80:
#         "Grade C"
#     case 60 <= marks < 70:
#         "Grade D"
#     case 50 <= marks < 60:
#         "Grade E"
#     case marks < 50:
#         "Grade F"
#     case _:
#         "Wrong input"

# print(grade)


