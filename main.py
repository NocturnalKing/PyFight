# If you want to use my code in your game plz talk to me first on Discord with Apokolypx D. MerDragon#6734 
# I probably will let you I just wanna know who wants it
# Also something to remember is that the game is NOT case sensitive

import random
import time
import os 
import sys
from colorama import Fore, Back
from colorama import init as colorama_init
colorama_init(autoreset=True)

#Fore. [color] changes text color [color]
#Back. [color] changes background to [color]

#------------ Weapons --------------
sakura = {
    "Name" : "useless",
    "Dmg" : 0
}
starter_sword = {
    "Name" : "starter sword",
    "Dmg" : 16
}
starter_gun = {
    "Name" : "starter gun",
    "Dmg" : 18
}
new_sword = {
    "Name" : "new sword",
    "Dmg" : 22
}
best_sword = {
    "Name" : "best sword",
    "Dmg" : 35
}
randSword = {
    "Name" : "randSword",
    "Dmg" : random.randint(36,45)
}
weaponKeys = [
    starter_sword,
    starter_gun,
    new_sword,
    best_sword,
    randSword,
]
#------------ Potions --------------

health = {
    "Name" : "Health",
    "HP" : 20
}
kill = {
    "Name" : "Health",
    "HP" : -15
}

#------------- Player --------------
weapon = starter_sword
player1 = {
    #HP
    "playerHP" : 50,
    #Damage
    "playerDmg" : weapon["Dmg"]
}
#------------ Enemies --------------
easy = {
    #Easy HP
    "HP" : 40,
    #Damage
    "easyDmg" : random.randint(5,15),
    #Name
    "Name" : "Gravity"
}

moderate = {
    #Moderate HP
    "HP" : 100,
    #Damage
    "moderateDmg" : random.randint(1,8),
    #Name
    "Name" : "MrGimme"
}

hard = {
    #Hard HP
    "HP" : 111,
    #Damage
    "hardDmg" : random.randint(10,10),
    #Name
    "Name" : "DaSwegMafiaLord"
}
#-----------------------------------
#------------- STATS ---------------
plyr1_dmg = player1["playerDmg"]
easy_dmg = easy["easyDmg"]
moderate_dmg = moderate["moderateDmg"]
hard_dmg = hard["hardDmg"]
plyr1_LP = player1["playerHP"]
easy_LP = easy["HP"]
moderate_LP = moderate["HP"]
hard_LP = hard["HP"]
#------------------------------------
#----------- Declarations -----------

def slowPrint(str): #not my code
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.09)
    print()
    return(str)

#----

def weopon_change(lvl):
    global weapon
    global weaponKeys
    count = 0
    print(Fore.BLUE + "here is", Fore.CYAN + "starter sword\'s", Fore.BLUE + "stats: It does",starter_sword["Dmg"], Fore.RED + "Damage")
    print(Fore.BLUE + "here is", Fore.CYAN + "new sword's", Fore.BLUE + " stats: It does ", new_sword["Dmg"], Fore.RED + "Damage")
    if(lvl == "moderate" or lvl == "hard"):
        print(Fore.BLUE + "here is", Fore.CYAN + "best sword's", Fore.BLUE + " stats: It does ", best_sword["Dmg"], Fore.RED + "Damage")
        if(lvl == "hard"):
            print(Fore.BLUE + "here is", Fore.CYAN + "randSword's", Fore.BLUE + " stats: It does ", randSword["Dmg"], Fore.RED + "Damage")
    print(Fore.BLUE + "here is", Fore.CYAN + "starter gun's", Fore.BLUE + "stats: It does ", starter_gun["Dmg"], Fore.RED + "Damage")
    print("0ut of the above what do you want to make your", Fore.CYAN + " weapon ","to ?")
    weaponIn = str(input(">> "))
    for item in weaponKeys:
        if(item["Name"].lower() == weaponIn.lower()):
            weapon = item
            return weapon
        count = count + 1
    else:
        slowPrint("You must have typed something wrong! \nThe weapon you typed does not exist")
        slowPrint(("The code will default to starter sword!"))
        time.sleep(.8)
        return starter_sword

#----

def potion(plyr1_LP,enemyHP):
    print("The", Fore.LIGHTMAGENTA_EX + "health","potion. Success rate:", Fore.RED + "50%")
    print("The", Fore.LIGHTMAGENTA_EX + "kill","potion. Success rate:", Fore.RED + ".5%")
    print("The", Fore.LIGHTMAGENTA_EX + "damage","potion. Success rate:", Fore.RED + "53%")    
    print("0ut of the above which", Fore.LIGHTMAGENTA_EX + "potion ","do you want?")
    potion = str(input(">> "))
    potion = potion.lower()
    if(potion == "health"):
        a = random.randint(1,100)
        if a <= 50:
            plyr1_LP =+ 40
            slowPrint("You gained 40 HP!")
        else:
            slowPrint("that failed!")
    elif(potion == "kill"):
        a = random.randint(1,200)
        if a == 1:
            enemyHP = 0
            slowPrint("So lucky! \n you killed them in 1 shot!")
        else:
            slowPrint("that failed!")
    elif(potion == "damage"):
        a = random.randint(1,100)
        if a <= 53:
            enemyHP = enemyHP - 35
            print("You damaged your enemy by 35 HP!")
        else:
            slowPrint("that failed!")
    else:
        slowPrint("You must have typed something wrong! \nThe potion you typed does not exist")
        time.sleep(.8)
    
    
#----

def magic():
    return 0

#----

enemyDmg = 0
enemyHP = 0
name = ""

def intro():
    global enemyDmg
    global enemyHP
    global name

    enemyLvl = str(input("choose an opponent level: \n easy \n moderate \n hard \n"))
    if(enemyLvl == "easy"):
        print("Your opponent's name is Gravity")
        enemyDmg = easy_dmg
        enemyHP = easy_LP
        name = easy["Name"]
    elif(enemyLvl == "moderate"):
        print("Your opponent's name is MrGimme")
        enemyDmg = moderate_dmg
        enemyHP = moderate_LP
        name = moderate["Name"]
    elif(enemyLvl == "hard"):
        print("Your opponent's name is DaSwegMafiaLord")
        enemyDmg = hard_dmg
        enemyHP = hard_LP
        name = hard["Name"]
    else:
        enemyDmg = easy_dmg
        enemyHP = easy_LP
        name = easy["Name"]
        print(Fore.YELLOW + "You must have typed something ", Fore.RED + "wrong", Fore.YELLOW + "... \nthe code will default to easy mode")
        enemyLvl = "easy"
        time.sleep(1)
    return enemyLvl
#----
def mainFight(enemyDmg, enemyHP, plyr1_dmg, plyr1_LP,name, lvl):
    global weapon
    weapon = weopon_change(lvl)
    plyr1_dmg = weapon["Dmg"]
    slowPrint("What is your move?")
    slowPrint("You can use:\nattack - You attack \ndefend - You gain 10 HP\nstats - checks the stats of you and your opponent\nweapon? - checks your weapon stats \nchange - changes your weapon")
    slowPrint("theres also a quitX move to stop mid-game")
    slowPrint("(FYI you can only attack if you type attack)")
    while(plyr1_LP > 0 and enemyHP > 0):
        move = str(input(">> "))
        if(move == "quitX"):
            break
        move = move.lower()
        if(move == "attack" ):
            enemyHP = enemyHP - plyr1_dmg
            print("----------")
            print("You attacked")
            print(name," is at ",enemyHP," HP")
            print("You are at ",plyr1_LP," HP")
        elif(move == "defend"):
            plyr1_LP = plyr1_LP + enemyDmg
            print("----------")
            print("You gained enough HP to defend the next attack")
            print("You now have ",plyr1_LP," health")
        elif(move == "stats"):
            print(Fore.GREEN + "You have", plyr1_LP, Fore.GREEN + " HP and do ", plyr1_dmg, Fore.GREEN +" damage")
            print(Fore.GREEN + "Your opponent has", enemyHP, Fore.GREEN + " HP and does ", enemyDmg, Fore.GREEN + " damage")
        elif(move == "change"):
            weapon = weopon_change(lvl)
            plyr1_dmg = weapon["Dmg"]
            slowPrint(("Your weapon is now ", Fore.CYAN + weapon["Name"]))
        elif(move == "weapon?"):
            print(weapon)
        elif(move == "potion"):
            print("----------")
            potIn = str(input("There is a chance you may not get anything \ndo you want to risk it? \n [y/n] "))
            potIn = potIn.lower()
            if potIn == "y":
                potion(plyr1_LP,enemyHP)
            else:
                print("you just wasted your turn...")
        else:
            enemyHP = enemyHP - plyr1_dmg
            print("----------")
            print("You attacked by default")
            print("Your enemy is at ",enemyHP," HP")
            print("You are at ",plyr1_LP," HP")
        if(enemyHP <= 0):
            print("----------")
            print(" You won!")
            break
        plyr1_LP = plyr1_LP - enemyDmg
        print("----------")
        print(name, " attacked!")
        print(name," is at ",enemyHP," HP")
        print("You are at ",plyr1_LP," HP")
        print("----------")
        if(plyr1_LP <= 0):
            print("--------------")
            print(" You lost...")
            break
#----------------- Main ----------------------------

if __name__ == "__main__":
    repeat = True
    while repeat == True:
        os.system("cls")
        lvl = intro()
        mainFight(enemyDmg, enemyHP, plyr1_dmg, plyr1_LP,name, lvl)
        time.sleep(2)
        print("do you want to play again?")
        a = str(input("[y/n] \n>> "))
        a = a.lower()
        if a == "n":
            repeat = False
        elif a != "y":
            repeat = True
print("Thanks for playing!")
