print(''''
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************

Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a cross road. Where do you want to go? Type "left" or "right" ''')
lor=input()
if(lor=="right"):
    print("Game Over")
else:
    print("You chose Left")
    print("Do You Want To Choose The Boat or Would you like to swim? ")
    sob=input()
    if(sob=="swim"):
        print("Game Over")
    else:
        print("Your Boat is here")
        print("You've reached the island")
        print("You have 3 doors in front of you!")
        print("Which door would you like to open")
        print("1.Red")
        print("2.Blue")
        print("3.Yellow")
        rby=input().lower()
        if(rby=="red" or rby=="1" or rby=="2" or rby=="blue"):
            print("You Lose!")
        else:
            print("Congrats! You found the treasure!!")
    