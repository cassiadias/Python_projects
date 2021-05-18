
#tip calculator that rounds 2 decimals places
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = round((bill * (tip/100) + bill) / people, 2)
message = f"Each person should pay: ${bill_with_tip}"
print(message)

