def calculate_bmi(weight,height):
    BMI=weight/(height*height)
    return BMI
weight=float(input("Enter the weight(kg): "))
height=float(input("Enter the height(m): "))
BMI=calculate_bmi(weight,height)
print("The BMI is : ",BMI)





