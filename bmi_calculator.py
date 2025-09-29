height = float(input("What's your height? "))
weight = float(input("What's your weight? "))
bmi = round(weight/height**2, 2)
print(f"Your bmi is {bmi}")
