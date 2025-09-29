print("Welcome to the rollercoaster!")
height = int(input("What's your height (in cm)? "))
bill = 0
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What's your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5!")
    elif 12 <= age <= 18:
        bill = 7
        print("Please pay $7")
    else:
        bill = 12
        print("Please pay $12")

    wants_photo = str(input("Do you want to take photo? Type y for yes and n for no "))
    if wants_photo == "y":
        bill += 3

    print(f"Your total bill is ${bill}")
else:
    print("Sorry you need to grow taller to ride the rollercoaster!")
