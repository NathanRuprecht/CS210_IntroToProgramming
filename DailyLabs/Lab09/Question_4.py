height = int(input("Give me your height in inches: "))
weight = int(input("Give me your weight in pounds: "))

BMI = (weight/ height ** 2) * 703

if (BMI < 18.5):
    print("underweight")
elif (BMI >= 18.5 and BMI <= 24.9):
    print("normal")
elif (BMI >= 25.0 and BMI <= 29.9):
    print("overweight")
else:
    print("obese")
