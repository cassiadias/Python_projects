#Create a program using maths and f-Strings that tell us how many days, weeks, months we have left if we live until 90 years old.
age = input("What is you current age? \n")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

menssage = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months"
print(menssage)