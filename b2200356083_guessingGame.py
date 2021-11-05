import random
machine = random.randint(0,101)
playerInt = int(input("Pick a number from 0 to 101. If you can guess the number that the machine picked, you win.\nEnter your number: "))
while (playerInt != machine):
    if (playerInt > machine):
        playerInt = int(input("Pick a smaller number: "))
    else:
        playerInt = int(input("Pick a greater number: "))
print("Congrats, you won")    

    

