import random

print("A Seeger approaches you!")
seegerdialogue = "Legos!"
seegerattack = 5
seegerdefense = 5
seegeranger = 0

def playerturn():
    print(f"{seegerdialogue}")
    choice = input(int("What will you do? (1: Fight, 2: Act, 3: Use Item): "))
    if choice == 1:
        fight()
    elif choice == 2:
        act()
    elif choice == 3:
        item()

def act():
    actchoice = input(int("Which act would you like to do? (1: Check, 2: Compliment, 3: Insult): "))
def fight():
    print("fight")
def item():
    print("item")

