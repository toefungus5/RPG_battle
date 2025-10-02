import random
enemyname = "Seeger"

print(f"{enemyname} approaches you!")
enemydialogue = "Legos!"
enemyHP = 1000
enemyattack = 50
enemydefense = 50
enemyanger = 0

def playerturn():
    print(f"{enemydialogue}")
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

