print("Welcome to the Treasure Island")
print("Your mission is to find the treasure.")
choice1 = input("Your're at a cross road. Where do you want to go ?\n Type 'left' or 'right' ").lower()
# choice3 = input("Your've come to a door. There is a Red, Blue and Yellow door.\n Type 'color of door' ")


if choice1 == "left":
    choice2 = input('Your\'ve come to a lake. There is an island in the middle of the lake. '
                 'Type "wait" to wait for a boat. Type "swim" to swim across ' ).lower()
    #Continue....
    if choice2 == "wait":
        choice3 = input('Your\'ve come to a door.'
                        'There is a Red, Blue and Yellow door.' 
                        'Type "color of door" ').lower()
        #Continue....
        if choice3 =="yellow":
            print("You have won!")
        else:
            print("Wrong color. Game Over")
    else: print("You got attacked by an angry trout. Game Over.")    

else:
    print("Wrong direction. Game Over")


#     if lake == "swim":
#         print("Game Over")
#     if color == "blue" or "red":
#         print("Game Over")
# else:
#     print("You win!")