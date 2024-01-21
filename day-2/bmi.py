print("*************** Hello Welcome to the BMI App **************\n")

weight = int(input("Enter your Weight in kg: "))
height = int(input("Enter your height: "))

bmi_calc = weight // height * height
print(bmi_calc)