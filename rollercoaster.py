print("Welcome to Star rollercoaster!")
age = int(input("What is your age?\n"))
if age >= 18:
    bill = 12
    print("Youth tickets are 12.")
elif age <= 12:
    bill = 6
    print("Child tickets are 6.")

wants_photo = input("Do you want your photo taken? Y or N\n")
if wants_photo == "Y":
    bill += 3
print(f"Your final bill is ${bill}\n Have fun!!")