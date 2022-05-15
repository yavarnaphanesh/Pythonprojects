height=float(input("Enter your height in m  : "))
weight=float(input("Enter your weight in Kgs: "))

BMI= weight/(height**2)

if BMI<18.5:
    print("your BMI is ", BMI, "You are are under weight")
elif BMI>18.5 and BMI<25:
    print("your BMI is ", BMI, "You are are normal  weight")
elif BMI> 25 and BMI <30:
    print("your BMI is ", BMI, "You are are over weight")
elif BMI>30 and BMI<35:
    print("your BMI is ", BMI, "You are are obese")
else:
    print("your BMI is ", BMI, "You are are clinically obese")
            
