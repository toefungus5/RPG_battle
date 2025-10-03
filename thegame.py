import random

enemyname = "Seeger"
BattleIsHappening = True

print(f"{enemyname} approaches you!")
enemydialogue = "Legos!"
narratordialogue = f"{enemyname} is readying himself for battle."
enemyHP = 100
enemyattack = 5
enemydefense = 5
enemyanger = 0

choices = ['Compliment', 'Insult', 'Check']

def checkdialogue():
    if enemyHP <= 0:
        print(f"{enemyname} has been defeated!")
        BattleIsHappening = False
    elif 85 < enemyHP < 96:
        narratordialogue = f"Steam is coming out of {enemyname}'s ears in a comical fashion."
    elif 76 < enemyHP < 84:
        narratordialogue = f"{enemyname} is getting ready to whoop your keister."
    elif 70 < enemyHP < 75:
        narratordialogue = f"{enemyname} is writing your name in his book of favors."

def playerturn():
    global enemydialogue
    checkdialogue()
    print(narratordialogue)
    choice = input("What will you do? (1: Fight, 2: Act, 3: Use Item): ")
    try:
        choice = int(choice)
    except ValueError:
        print("That's not a valid number.")
        return

    if choice == 1:
        fight()
    elif choice == 2:
        act()
    elif choice == 3:
        item()
    else:
        print("That's not a valid number!")
        return


def act():
    print(choices[0], choices[1], choices[2])


def fight():
    global enemyHP, enemydialogue, BattleIsHappening
    damage = random.randint(3, 7)
    enemyHP -= damage
    print(f"You punched {enemyname} and did {damage} damage!")
    enemydialoguenumber = random.randint(1, 3)
    if enemydialoguenumber == 1:
        enemydialogue = "OWWW DUDE!!! Not cool!!!"
    elif enemydialoguenumber == 2:
        enemydialogue = "What the HELL man!!! I don't like that!"
    else:
        enemydialogue = "Oh you wanna GO buckaroo??? I punch metal for fun!"
    print(f"{enemyname}: {enemydialogue}")


def item():
    print("item")


while BattleIsHappening == True:
    playerturn()
    #seegerturn()
