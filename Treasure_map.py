# Program that allows you to mark a square on the map using a two-digit system

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]

position = input("Where do you want to put the treasure? \n")

user_input = position.split(",")

# Replace 'str' to int to map index of user input to 'x'

map[int(user_input[1])-1][int(user_input[0])-1] = 'x'

print(f"{row1}\n{row2}\n{row3}")