print("Welcome to the treasure Island!!")
print('''      _____
            .-" .-. "-.
        _/ '=(0.0)=' \_
        /`   .='|m|'=.   `\
        \__________________/
      .--.__///`'-,__~\\\\~`
     / /6|__\// a (__)-\\\\
     \ \/--`((   ._\   ,)))
     /  \\  ))\  -==-  (O)(
    /    )\((((\   .  /)))))
   /  _.' /  __(`~~~~`)__
  //"\\,-'-"`   `~~~~\\~~`"-.
 //  /`"              `      `\
//
''')
print("Your mission is to find the treasure @^ ^@")
choice1 = input('You arrived in the Island treasure, where do you want to go? Type "left" or "right"?\n').lower()
if choice1 == "left":
    choice2 = input('You need wait for the boat to go to the next Island. Do you prefer "wait" or "swim?"\n').lower()
    if choice2 == "wait":
        print("Lazy people don't get treasure. Game over!!")
    elif choice2 == "swim":
        choice3 = input('You\'re close. Choose a key color: "red", "blue" or "purple?"\n').lower()
        if choice3 == "red":
            print("Game over!!")
        elif choice3 == "blue":
            print("Wrong choice. Game over!!")
        elif choice3 == "purple":
            print("Good choice. You win!!")
elif choice1 == "right":
    choice4 = input('Good choice, you will go venture into the forest. Do you prefer follow "footsteps" or "noise"?\n').lower()
    if choice4 == "footsteps":
        print("Bad choice. You become a good animal food")
    elif choice4 == "noise":
        print("Good job! you got to the treasure, just dig")
else:
    print("Game over!!")
