answer = input ("Do you like to play a game? (yes/no)")
if answer.lower().strip() == "yes":
    answer = input ("You reached a crossroad, would you like to go left or ringht?").lower().strip()
    if answer == "left":
        answer = input("You encounter a monsture, would you like to run or attack?")

        if answer == "attack":
            print("That was not the goood idea, you lost!")
        else:
            print("Good choice, you have done well")
    
    elif answer == "right":
        print("You choose a wrong path, Game Over!!")
    else:
        print("Invalid choice, you lost!")

    