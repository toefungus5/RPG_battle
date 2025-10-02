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
    actchoice = #I'm going to put a list here
    
def fight():
    damage = random.randint(3,7)
    print(f"You punched {enemyname}!)
    enemydialoguenumber = random.randint(1,3)
    if enemydialoguenumber == 1:
        enemydialogue = "OWWW DUDE!!! Not cool!!!"
    elif enemydialoguenumber == 2:
        enemydialogue = "WHat the HELL man!!! I don't like that!"
    else:
        enemydialogue = "Oh you wanna GO buckaroo??? I punch metal for fun!"
    print(f"{enemyname}: {enemydialogue}")
    
def item():
    print("item")

