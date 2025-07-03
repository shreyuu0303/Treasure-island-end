print("Welcome to Treasure Island.")
print("Your mission is to find the treasure 🏴‍☠️")
choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()
if choice1=="left":
    choice2=input("You come to a lake. Type 'wait' to wait for a boat or 'swim' to swim across:").lower()
    if choice2=="wait":
        choice3=input("You arrive at the island unharmed. There is a house with 3 doors: red, yellow, and blue. Which do you choose?").lower()
        if choice3=="yellow":
            print("🎉 You found the treasure! You Win!")

        elif choice3=="red":
             print("🔥 It's a room full of fire. Game Over.")
            
        elif choice3=="bule":
             print("💀 You enter a room of beasts. Game Over.")
        else:
            print("🚪 That door doesn't exist. Game Over.")
    else:
        print("🦈 You were attacked by a trout. Game Over.")
else:
    print("😵 You fell into a hole. Game Over.")