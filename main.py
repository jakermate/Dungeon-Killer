import time, random, pickle

"""This is where the player's location and stats are stored"""

class dungeon:

    # rowA={1: "room21",2:"room22",3:"room23",4:"room24",5:"room25"}
    # rowB = {1: 16, 2: 17, 3: 18, 4: 19, 5: 20}
    # rowC = {1: 11, 2: 12, 3: 13, 4: 14, 5: 15}
    # rowD = {1: 6, 2:7, 3: 8, 4: 9, 5: 10}
    # rowE = {1: "room1", 2: "room2", 3: "room3", 4: "room4", 5:"room5"}
    def __init__(self):
        self.ROOMS = {}

#save player object, room objects
def savegame():
    filename = input("Enter a filename for your gamesave: ")
    print("Saving...")
    savedata = {"player": player, "map": map}
    save = open(filename, "wb")
    pickle.dump(savedata,save)
    save.close()
    time.sleep(.5)
    saveindex = open("index", "a")
    saveindex.write(filename)
    saveindex.close()
    print("GAME SAVED!")

def loadgame():
    saveindex = open("index", "r")
    list = saveindex.read()
    print(list)
    filename = input("Select filename to load: ")
    load = open(filename, "rb")
    loadedsave = pickle.load(load)
    print("Loading....\n")
    time.sleep(1)
    load.close()
    global player, map
    player = loadedsave["player"]
    map = loadedsave["map"]
    print("Game Loaded!\n")


class room():

    def __init__(self, roomnum, ttl, description, ischest, enemies, lock, beenhere, itemtype, North, South, East, West):
        self.num = roomnum
        self.title = ttl
        self.description = description
        self.doorN = North
        self.doorS = South
        self.doorW = West
        self.doorE = East
        self.chest = ischest
        self.enemy = enemies
        self.been = beenhere
        self.item = itemtype
        self.lock = lock


def showmap():
    if player.map == True:
        print(" ______________________________________________________ ")
        print("|          |          |          |          |          |")
        print("|          |          |          |          |          |")
        if player.location == 21:
            print("|     X                                                |")
        if player.location == 22:
            print("|               X                                      |")
        if player.location == 23:
            print("|                          X                           |")
        if player.location == 24:
            print("|                                     X                |")
        if player.location == 25:
            print("|                                                X     |")
        if player.location < 21:
            print("|                                                      |")
        print("|          |          |          |          |          |")
        print("|__________|__________|__________|____  ____|____  ____|")
        print("|          |          |          |          |          |")
        print("|          |          |          |          |          |")
        if player.location == 16:
            print("|     X               |                                |")
        if player.location == 17:
            print("|               X     |                                |")
        if player.location == 18:
            print("|                     |    X                           |")
        if player.location == 19:
            print("|                     |               X                |")
        if player.location == 20:
            print("|                     |                          X     |")
        if player.location < 16 or player.location > 20:
            print("|                     |                                |")
        print("|          |          |          |          |          |")
        print("|____  ____|____  ____|____  ____|____  ____|__________|")
        print("|          |          |          |          |          |")
        print("|          |          |          |          |          |")
        if player.location ==11 :
            print("|     X    |                                           |")
        if player.location ==12 :
            print("|          |    X                                      |")
        if player.location ==13 :
            print("|          |               X                           |")
        if player.location ==14 :
            print("|          |                          X                |")
        if player.location ==15:
            print("|          |                                     X     |")
        if player.location < 11 or player.location > 15:
            print("|          |                                           |")
        print("|          |          |          |          |          |")
        print("|____  ____|__________|____  ____|__________|____  ____|")
        print("|          |          |          |          |          |")
        print("|          |          |          |          |          |")
        if player.location ==6 :
            print("|     X               |          |                     |")
        if player.location ==7 :
            print("|               X     |          |                     |")
        if player.location ==8 :
            print("|                     |    X     |                     |")
        if player.location ==9 :
            print("|                     |          |    X                |")
        if player.location ==10:
            print("|                     |          |               X     |")
        if player.location < 6 or player.location > 10:
            print("|                     |          |                     |")
        print("|          |          |          |          |          |")
        print("|__________|__________|____  ____|__________|____  ____|")
        print("|          |          |          |          |          |")
        print("|          |          |          |          |          |")
        if player.location == 1:
            print("|     X                                                |")
        if player.location == 2:
            print("|               X                                      |")
        if player.location == 3:
            print("|                          X                           |")
        if player.location == 4:
            print("|                                     X                |")
        if player.location == 5:
            print("|                                                X     |")
        if player.location > 5:
            print("|                                                      |")

        print("|          |          |          |          |          |")
        print("|__________|__________|____==____|__________|__________|")
        print("You are here: X")
    else:
        print("You do not hold a map...")

def openchest(choice):
    if map.ROOMS[player.location].chest == False:
        print("There is nothing to open.")
    if map.ROOMS[player.location].enemy == None:
        if map.ROOMS[player.location].chest == True:
            if player.location == 1:
                player.sword = "onehandedsword1"
                atk = items.onehandsword1["attack"]
                dfns = items.onehandsword1["defense"]
                player.attack = atk
                player.defense = dfns
                print("You open the chest and receive a RUSTY DAGGER!")
                print("Here are the stats: \nName:", items.onehandsword1["name"], "\nAttack: ", items.onehandsword1["attack"], "\nDefense:", items.onehandsword1["defense"])
            if player.location == 13:
                print("You reach atop the pedestal and receive a DUNGEON MAP!")
                player.map = True
            if player.location == 7:
                print("You open the chest and receive a GOLDEN KEY")
                player.keyG = True
            if player.location == 25:
                print("You open the chest and receive a SILVER KEY")
                player.keyS = True
            if player.location == 18:
                print("You open the chest and receive the SKELETON KEY")
                player.keySk = True
            if player.location == 12:
                print("You open the sealed chest and receive a STEEL BROADSWORD")
                player.sword = "onehandedsword2"
                atk = items.onehandsword2["attack"]
                dfns = items.onehandsword2["defense"]
                player.attack = atk
                player.defense = dfns
            if player.location == 20:
                print("You kick open the chest and receive an IRON SHIELD")
                print("Your DEFENSE RATING INCREASES!")
                player.shield = True
                player.defense += 20
            map.ROOMS[player.location].chest = False
    elif map.ROOMS[player.location].enemy != None:
        print("You cannot do that while facing an enemy!")
    else:
        print("There is nothing to open...")


class Player():

    def __init__(self):
        self.name = "New"
        self.incombat= False
        self.health = 100
        self.armor = 0
        self.attack = 5
        self.defense = 0
        self.location = 3
        self.lastlocation = 0
        self.items = ["compass", "lantern"]
        self.sword = "Rusty Dagger"
        self.shield = False
        self.map = False
        self.keyG=False
        self.keyS=False
        self.keySk=False
    def pickupsword(self, swordtype):
        self.sword = swordtype


class items():
    onehandsword1={"attack": 5, "defense": 5, "speed":1, "type": "one handed sword", "name":"Rusty Dagger"}
    onehandsword2={"attack": 15, "defense": 10, "speed": 1, "type": "one handed sword", "name":"Steel Sword"}
    shield={"attack": 2, "defense": 20,"speed":.5, "type": "shield", "name":"Wooden Shield"}

class skeleton:
    name="Skeleton"
    health=30
    attack=15
    speed=1
    def showstats(self):
        print("\n")
        print(self.name)
        print("Health: ", self.health)

class spider:
    name="Giant Spider"
    health=15
    attack=5
    speed=1
    def showstats(self):
        print("\n")
        print(self.name)
        print("Health: ", self.health)

class golem:
    name="Rock Golem"
    health:50
    attack:20
    speed:2
    def showstats():
        print("\n")
        print(self.name)
        print("Health: ", self.health)

def lastlocation():
    player.lastlocation = player.location

def istheredoor(path):
    if "north" in path:
        if map.ROOMS[player.location].doorN == True:
            changelocation(path)
        else:
            print("\nThere is no door in that direction...")
    if "south" in path:
        if map.ROOMS[player.location].doorS == True:
            changelocation(path)
        else:
            print("\nThere is no door to the south...")
    if "east" in path:
        if map.ROOMS[player.location].doorE == True:
            changelocation(path)
        else:
            print("\nYou cannot travel that way. There is no doorway.")
    if "west" in path:
        if map.ROOMS[player.location].doorW == True:
            changelocation(path)
        else:
            print("\nYou cannot travel west from here.")

def swing(enemy):
    print("\nYou swing", player.sword, "at the", enemy.name)
    chance = random.randint(1,4)
    if chance != 3:
        enemy.health -= player.attack
        print("You hit", enemy.name, "for", player.attack, "damage!\n")
    else:
        print("You missed!")
    if enemy.health > 0:
        print(enemy.name, "attacks you for", enemy.attack, "damage.")
        chance=random.randint(1,3)
        if chance == 2:
            enemyhit = enemy.attack - (player.defense)
            print(enemy.name,"hits you for", enemyhit, "damage! (Enemy attack minus your defense rating.)")
            player.health -= enemyhit
            print("Your health drops to",player.health)
        else:
            print(enemy.name, "missed!")

def changelocation(direction):
    if "north" in direction and player.location + 5 <= 25 :
        lastlocation()
        player.location += 5
    elif "south" in direction and player.location -5 >= 0:
        lastlocation()
        player.location -= 5
    elif "east" in direction and player.location + 1 != 6 and player.location + 1 != 11 and player.location + 1 != 16 and player.location + 1 != 21 and player.location + 1 != 26:
        if player.location + 1 == 7 and player.keySk == False:
            print("The large iron door leading into [=\=]The VAULT[=/=] is large and imposing.  You try to push it but it won't budge.  In the center you see a keyhole, surrounded by the engraved images of a species of spider.  You must need a key to unlock the door.")
        else:
            lastlocation()
            player.location += 1
    elif "west" in direction and player.location - 1 != 0 and player.location - 1 != 5 and player.location - 1 != 10 and player.location - 1 != 15 and player.location - 1 != 20 :
        if player.location - 1 == 21 and player.keyG == False:
            print("You do not have the required keys to enter this door...  You see two keyholes; one surrounded in a ring of gold, the other in silver.")
        elif player.location - 1 == 21 and player.keyS == False:
            print("You do not have the required keys to enter this door... You see two keyholes; one surrounded in a ring of gold, the other in silver.")
        else:
            lastlocation()
            player.location -= 1
    else:
        print("You must choose a valid path...")

def showinventory():
        print("INVENTORY:\n")
        print("   WEAPON-", player.sword)
        if player.shield == False:
            print("   SHIELD-     ---")
        else:
            print("   SHIELD-", player.shield)
        if player.map == False:
            print("    ---")
        else:
            print("   MAP-   Dungeon Map")
        if player.keySk != False:
            print("   KEYS-    Skeleton Key")
        else:
            print("   KEYS-    ---")
        if player.keyG != False:
            print("            Golden Key")
        if player.keyS != False:
            print("            Silver Key")


def showstats():
    print("You have",player.health,"health.")
    print("You have",player.armor,"armor.")

def combat(enemy):
    target= enemy
    while enemy.health > 0:
        target.showstats()
        decision=input("\nWill you attack?\n")
        if decision == "yes" or decision == "attack":
            swing(target)
        elif decision=="no" or decision=="flee":
            print("You flee back the way you came!")
            player.location = player.lastlocation
            fleeroom = map.ROOMS[player.location]
            print("\nYou enter ", fleeroom.title)
            print("\n",fleeroom.description)
            break
        else:
            print("Face your enemy or flee!")
            print("Do something... quickly!")
            combat(enemy)
    thisroom = map.ROOMS[player.location]
    thisroom.enemy = None

        #     thisroom = map.ROOMS[player.location]
        #     thisroom.enemy = False
        #     print("You may resume your adventure...")

def attack():
    if player.incombat == True:
        if player.sword != False:
            print("You attack for ", player.attack ," damage!")
        else:
            print("You punch for 5 damage!")


def doorlocks():
    #for deciding if you have correct keys (skeleton, silver, gold)


    """NAME CHECK"""
def choosename():
    try:
        print("Greetings, traveler.  What is your name?")
        name = input("name:")
        if not name:
            raise ValueError("I'm sorry, I couldn't quite hear that...")
    except:
        print("Welcome")

# All player input flows from here
def playerinput():
    while game == "running":
        lastroom = player.location
        d=random.randint(0,1)
        if d == 0:
            choice = input("\nDecide what to do now...\n-")
        elif d==1:
            choice = input("\nWhat now...\n-")
        if choice == "help":
            help()
        if "go" in choice or "walk" in choice:
            istheredoor(choice)
        if "open" in choice:
            openchest(choice)
        if "show" and "map" in choice:
            showmap()
        if choice == "attack":
            attack()
        if "inventory" in choice:
            showinventory()
        if choice == "save":
            savegame()
        if choice =="load":
            loadgame()
        currentroom = map.ROOMS[player.location]

        if lastroom == player.location:
            print("\nRoom", player.location, "\n",currentroom.title)
        else:
            # determines if youve been here already
            if currentroom.been == False:
                print("\n    -YOU ENTER->\n" + currentroom.title)
            if currentroom.been == True:
                print("\n      YOU RE-ENTER\n" + currentroom.title)
            print("\n",currentroom.description)
            currentroom.been = True
        if currentroom.enemy == "spider":
            print("\nThere is a GIANT SPIDER!")
            print("    / /    \ \    ")
            print("    \ \    / /    ")
            print("     \ \/\/ /     ")
            print("      >(><)<      ")
            print("     / /\/\ \     ")
            print("    / / ''/  \    ")
            print("    \        /    ")
            enemyspider = spider()
            combat(enemyspider)
        if currentroom.enemy == "skeleton":
            print("\nThere is a REANIMATED SKELETON!")
            print("            __            ")
            print("          [*  *]          ")
            print("          [||||]          ")
            print("           \==/           ")
            print("           =||=           ")
            print("        ----==----        ")
            print("       /  {=  =}  \       ")
            print("      /   {=  =}   \      ")
            print("     /\    {==}   /\     ")
            print("          [/  \]          ")
            print("         [|    |]         ")
            print("         ||    ||         ")
            print("       ==/      \==       ")
            enemyskeleton = skeleton()
            combat(enemyskeleton)
        if currentroom.enemy == "golem":
            print("\nThere is an EARTHEN GOLEM!")
            print("      OoooooooooO             ")
            print("    OooooooooooooooO          ")
            print("   Oooo( * )ooo( * )ooO       ")
            print("    OoooooooooooooooO         ")
            print("   Ooooooo|||||||oooooO       ")
            print("    Oooooo+++++++oooooO       ")
            print("   Ooooooo|||||||ooooooO      ")
            print("    OooooooooooooooooooO      ")
            print(" OoooooooooooooooooooooooO    ")
            print(" OoooooooooooooooooooooooO    ")
            print(" OooooooooooooooooooooooooooO ")
            print(" OooooooooooooooooooooooooooO ")
            enemygolem = golem()
            combat(enemygolem)




# help menu
def help():
    print("\n***This is the HELP MENU***")
    print("The following are all suitable inputs:")
    print("\n- 'help'.....if you get lost...")
    print("- 'go north'......to go north if the way is clear")
    print("- 'go south'......to go south if the way is clear")
    print("- 'go west'.......to go west if the way is clear")
    print("- 'go east'.....to go east if the way is clear")
    print("- 'open ____' (chest, lock, door).....to open an item in your way")
    print("- 'show map'......will display a map of the dungeon if you have found it")
    print("- 'show inventory'......to display your currently equipped gear")
    print("- 'save'...........to begin the file save process")
    print("- 'load'........to load a saved game")
    playerinput()

map = dungeon()
room1=room(1,"<-=-The Jail-=->","Rusted cages and bloodied chains hang from the ceiling and dot the walls...\nYou see a chest at the far end of the room. It appears to be unlocked.", True, "skeleton", None, False, "One Handed Sword", False, False, True, False)
map.ROOMS[1]=room1
room2=room(2,"%%%-The Catacombs-%%%","A narrow passage with shelves lining the sides.  Stored there are the skulls of a thousand long-dead humans...\nA door lies on the western wall.", None, None, None, False, None, False, False, True, True)
map.ROOMS[2]=room2
room3=room(3,"--=The Entryway=--","Barely lit from the archway leading outside; you see doors ahead and to both sides...", None, None, None, False, None, True, False, True, True)
map.ROOMS[3]=room3
room4=room(4,"The ~OvErGrOWth~","Vines creep in from the crack in the ceiling. Light splashes across the floor, a bridge in the dark.  The floor can't be seen under the growths of moss and grass.  A door lies on the eastern wall...", None, None, None, False, None, False, False, True, True)
map.ROOMS[4]=room4
room5=room(5,"( ~ )Reflection Pool( ~ )","Rusted cages and bloodied chains line the walls...", None, "spider", None, False, None, True, False, False, True)
map.ROOMS[5]=room5
room6=room(6,"[ ] Storage Room [ ]","Rusted cages and bloodied chains line the walls...", None, "skeleton", None, False, None, True, False, True, False)
map.ROOMS[6]=room6
room7=room(7,"[=\=]The VAULT[=/=]","Piles of gold and silver coins and artifacts lay on the floor.", True, "golem", None, False, "Golden Key", False, False, False, True)
map.ROOMS[7]=room7
room8=room(8,"-=##Reception Hall##=-","Rusted cages and bloodied chains line the walls...", None, "spider", None, False, None, True, True, False, False)
map.ROOMS[8]=room8
room9=room(9,"The Jail","Rusted cages and bloodied chains line the walls...", None, "skeleton", None, False, None, False, False, False, True)
map.ROOMS[9]=room9
room10=room(10,"The Jail","Rusted cages and bloodied chains line the walls...", None, "spider", None, False, None, True, True, False, True)
map.ROOMS[10]=room10
room11=room(11,"-^-'Servant's Quarters'-^-","Rusted cages and bloodied chains line the walls...", None, "spider", None, False, None, True, True, False, False)
map.ROOMS[11]=room11
room12=room(12,"The Jail","Rusted cages and bloodied chains line the walls...", None, "golem", None, False, None, True, False, True, False)
map.ROOMS[12]=room12
room13=room(13,"X+++The Central Hub+++X","Doors on all four sides.  In the center of the circular room is a stone pedestal.  A stone tablet lies ontop of it; you can make out a faint outline of a map from where you stand.", True, None, None, False, "Sword", True, True, True, True)
map.ROOMS[13]=room13
room14=room(14,"The Jail","Rusted cages and bloodied chains line the walls...", True, "skeleton", None, False, "Map", True, False, True, True)
map.ROOMS[14]=room14
room15=room(15,"($)=The Galley=($)","Rusted cages and bloodied chains line the walls...", None, None, None, False, None, False, True, False, True)
map.ROOMS[15]=room15
room16=room(16,"<-^^The Armory^^->","Rusted cages and bloodied chains line the walls...", None, "spider", None, False, None, False, True, True, False)
map.ROOMS[16]=room16
room17=room(17,"The Jail","Rusted cages and bloodied chains line the walls...", None, None, None, False, None, False, True, False, True)
map.ROOMS[17]=room17
room18=room(18,"The Jail","Rusted cages and bloodied chains line the walls...", None, None, None, False, None, False, True, True, False)
map.ROOMS[18]=room18
room19=room(19,"The Jail","Rusted cages and bloodied chains line the walls...", None, "skeleton", None, False, None, True, True, True, True)
map.ROOMS[19]=room19
room20=room(20,"|--|Living Quarters|--|","Rusted cages and bloodied chains line the walls...", True, None, None, False, "Shield", True, False, False, True)
map.ROOMS[20]=room20
room21=room(21,"-+-==||||-Butcher's Lair-||||==-+-","You step into the claustrophobic den of The Butcher.  Low ceilings.", None, None, None, False, None, False, False, True, False)
map.ROOMS[21]=room21
room22=room(22,"The Jail","Rusted cages and bloodied chains line the walls...", None, "golem", None, False, None, False, False, True, False)
map.ROOMS[22]=room22
room23=room(23,"The Jail","Rusted cages and bloodied chains line the walls...", None, None, None, False, None, False, False, True, False)
map.ROOMS[23]=room23
room24=room(24,"The Jail","Rusted cages and bloodied chains line the walls...", None, "golem", None, False, None, False, True, True, True)
map.ROOMS[24]=room24
room25=room(25,"~*~%The Apothecarium%~*~", "Vats of junk.  Shelves lined with books, jars of preserved specimens, and numerous regeants.  There are doors on the Southern and Western walls.  The wall to the east has a crack running down it, you can see some light shining through.", None, "spider", None, False, None, False, True, False, True)
map.ROOMS[25]=room25
room26=room(26, "???*HIDDEN CHAMBER*???", "Congratulations, you've found the secret room.",None,None,None,False,None,None, False, False,True)
map.ROOMS[26]=room26


# print("\n              ** ")
# print("              ** ")
# print("             ****")
# print("             ****")
# print("            ******")
# print("            ******")
# print("         -WELCOME TO- ")
# print("\n\n   -===||||||||||||||||===-")
# print(" -===|||DUNGEON KILLER|||===-")
# print("   -===||||||||||||||||===-")



# print("\n\n      Jake Miller, 2017")
#
# input("\n\n Press any key to begin")
#
# print(" |^------^^------^^-^-^^----^^^------^--^-^|")
# print(" |  *                           |          |")
# print(" |      |  *                    |          |")
# print(" |      |                       |       |  |")
# print(" |             *     |                  |  |")
# print(" |                        |        *       |")
# print(" |    \                    |               |")
# print(" |    /             -^-     *     \        |")
# print(" |    \            |***|          /        |")
# print(" |           |     |***|                   |")
# print(" |                 |***|       |        *  |")
# print(" |_________________|***|___________________|")
#
# print("\n\nYou approach a barren cliff face.  At its base lies a rectangular entryway. You can't make out anything inside...")
# time.sleep(2)
# print("\nYou step inside.")
# time.sleep(2)
# print("-YOU ENTER->)
# print("--=The Entryway=--")
# print("\nIt's pitch black... you see nothing...")
# time.sleep(1)
# print("\n...")
# time.sleep(1)
# print("\nWait!")
# time.sleep(.5)
# print("\nYou spot something")

# print("Well met, " +name+". If you seek to enter the mines, you must be careful to stay on this side of death...  Here, take this...")



game = "running"

player = Player()
player.map = True #temporary!

playerinput()
