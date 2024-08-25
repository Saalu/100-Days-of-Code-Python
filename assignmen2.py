print("Welcome to the Treasure Island")
print("Your mission is to find the treasure.")
road = input("Your're at a cross road. Where do you want to go ?\n Type 'left' or 'right' ")
lake = input("Your've come to a lake. There is an island in the middle of the lake.\n Type 'wait' to wait for a boat. Type 'swim' to swim across ")
color = input("Your've come to a door. There is a Red, Blue and Yellow door.\n Type 'color of door' ")


if road == "right":
    print("Game Over")
    if lake == "swim":
        print("Game Over")
    if color == "blue" or "red":
        print("Game Over")
else:
    print("You win!")