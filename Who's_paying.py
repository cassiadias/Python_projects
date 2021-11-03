# Program which will select a random name from a list of names
# The person selected will have to pay for everybody's food bill.

import random
names_string = input('Give me everybody\'s names separated by comma:\n')
names = names_string.split(",")

random_name = random.choice(names)

print(f"Who will pay for the meal today is {random_name.upper()}")
