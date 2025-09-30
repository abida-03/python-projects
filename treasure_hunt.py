print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to the treasure island.\n"
      " Your mission is to find the treasure")
choice1 = input('You\'re are at a crossroad.'
                ' Where do you want to go?'
                ' Type "left" or "right".').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across the lake.').lower()
    if choice2 == "wait":
            choice3 = input('You\'ve arrive at the island unharmed. '
                            'There is a house with doors. '
                            'One red, one blue, one yellow. '
                            'Which color of door do you choose?').lower()
            if choice3 == "yellow":
                print('You found the treasure. You win!')
            elif choice3 == "red":
                print("It\'s a room full of fire. Game over.")
            elif choice3 == "blue":
                print("You enter a room of beasts. Game over.")
            else:
                print("You chose a door that doesn't exist. Game over.")
    else:
        print("You got eaten by an aligetor. Game Over.")

else:
    print("You fell in to a hole. Game Over.")

#the output flow can be of variety depending on the set of choices
