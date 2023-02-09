import random
response = "y"
while response == "y":
    n=random.randint(1,6)
    if n == 1:
        print("Roll the Dice to 1")
    if n == 2:
        print("Roll the Dice to 2")
    if n == 3:
        print("Roll the Dice to 3")
    if n == 4:
        print("Roll the Dice to 4")
    if n == 5:
        print("Roll the Dice to 5")
    if n == 6:
        print("Roll the Dice to 6")
    response=input("press y to roll again and n to exit")

    print("\n")