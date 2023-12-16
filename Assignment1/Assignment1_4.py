weight = float(input("Please enter your weight (kilogram):"))
height = float(input("Please enter your height (cm):"))

bmi = weight / height ** 2

if bmi < 18.5 :
    result = "Underweight"

elif bmi >= 18.5 and bmi < 25 :
    result = "Normal Weight"

elif bmi >= 25 and bmi < 30 :
    result = "Overweight"

elif bmi >= 30 and bmi < 35 :
    result = "Obesity"

elif bmi >= 35 and bmi < 40 :
    result = "Obesity"

print("Your BMI :" , bmi)
print("Your weight category : " , result)


