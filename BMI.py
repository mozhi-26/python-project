print("***BMI CALCULATOR***")
 
weight=float(input("Enter the weight: "))
height_cm=float(input("Enter the height: "))
height=height_cm/100
 
bmi=weight/(height**2)
print(f"BMI:{bmi}")

if bmi <18.5:
    print("You are under weight")
elif bmi <=bmi <24.9:
    print("You have normal weight")
elif 25<= bmi<29.9:
    print("You are overweight")
else:
    print("You are obese")