a = int(input("Enter your grades for Maths : "))
b = int(input("Enter your grades for Science : "))
c = int(input("Enter your grades for English : "))
d = int(input("Enter your grades for Chemistry : "))
e = int(input("Enter your grades for Physics : "))
grade = (a+b+c+d+e)/5
if(grade>=90):
    print(f"Your grade is {grade} you got A")
elif(grade>=75):
    print(f"Your grade is {grade} you got B")
elif(grade>=60):
    print(f"Your grade is {grade} you got C")
elif(grade>=24):
    print(f"Your grade is {grade} you got D")
else:
    print("You Failed in your exam better luck next time")