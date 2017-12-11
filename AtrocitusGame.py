#Author: Kevin McLester
#My gamekicks ass
#This is another comment for a commit
import sys
import random
import os
#This is only imported so I can display an actual map
import tkinter as Atrocitus_Map

playerScore=0
playerName=""
key=0
turnNumber=0
MF=0
EgR=0
ER=0
EP=0
EL=0
VL=0
JR=0
SR=0
TH=0
CS=0
TC=0
currentLocation = ""
Inventory = []
Flashlight="flashlight"
lobbymap="map"
KAL = 0
pray_count = 0






class Player:
        def __init__(self, name, score, currLocale, move_count, inventory):
                self.name = name
                self.score = score
                self.currLocale = currLocale
                self.move_count = move_count
                self.inventory = inventory
                Inventory = []
                self.inventory = Inventory
        def updateInv(self):
                self.inventory = Inventory
        def updateScore(self):
                global playerScore
                
                self.score = playerScore

        def updateTurn(self):
                global turnNumber
                self.move_count = turnNumber

        def updateName(self):
                global playerName
                self.name = playerName
        def updateLocale(self):
                global currentLocation
                self.currLocale = currentLocation

        def showScore(self):
                print("Score: "+str(self.score))

        def quitGame(self):
                print(self.name+"'s Final Score: "+str(self.score))
                print("Thank you for playing Atrocitus "+self.name+"!")
                print("Goodbye!")
                print("THE END!")
                input("Press enter to end game...")
                sys.exit()
                
        def pray(self):
                global pray_count
                rando=random.randrange(0,4)
                print("You pray to your deity for an answer... \n ")
                if pray_count < 3:
                        if rando == 1 or rando == 0:
                                print("You hear a voice tell you to remember to check your inventory.\n")
                        elif rando == 2:
                                print("You hear a voice tell you to stay calm and assess the situation. Maybe use the help command.\n")
                        elif rando == 3 or rando == 4:
                                print("You hear a voice tell you to remember to check your map.\n")
                        pray_count = pray_count + 1

                else:
                        print("You wait for a minute but nothing happens.")

        def yell(self):
                
                yelling = input("What do you wish to yell?: ")
                print("You yell out: "+yelling+"\n")
                return yelling
                        
                        

        def teleport(self):
                if "Developers Portal Gun" in self.inventory:
                        print("Where would you like to teleport "+self.name+"?")
                        i=0
                        while i == 0:
                                destination = input()
                                if destination == "main frame":
                                        Navigation[0][1]()
                                elif destination == "elevator room":
                                        Navigation[1][1]()
                                elif destination == "escape pods":
                                        Navigation[1][2]()
                                elif destination == "egg room":
                                        Navigation[1][0]()
                                elif destination == "elevator":
                                        Navigation[2][1]()
                                elif destination == "trash chute":
                                        Navigation[2][2]()
                                elif destination == "ventilation":
                                        Navigation[3][1]()
                                elif destination == "trash compactor":
                                        Navigation[3][2]()
                                elif destination == "jungle room":
                                        Navigation[4][2]()
                                elif destination == "secret room":
                                        Navigation[4][0]()
                                elif destination == "tree house":
                                        Navigation[5][2]()
                                else:
                                        print("Invalid Destination")
                else:
                        pass
        

        def Use(self, item):
                if item in player1.inventory:
                        print("You use the "+item)
                        return True
                else:
                        print("You do not have that item!")
                        return False
        def Take(self, item):
                Inventory.append(item)
                player1.updateInv()
                print("You take the "+item+".")
                
player1 = Player("player", 0, "ElevatorRoom", 0, "")
        

class Locale:
        def __init__(self, LocaleName, LocaleDescription):
                self.LocaleName = LocaleName
                self.LocaleDescription = LocaleDescription

MAIN_FRAME = Locale("Main Frame", "You open the door with the key you found and go in. \n Theres a large lever with a label on it that says POWER. \n What do you do?")
ELEVATOR_ROOM = Locale("Elevator Room", "You step out into a barely lit room with doors to your left, right, and directly in front of you. There is a trash chute by the elevator. The elevator stays open behind you. \nThere is a map next to the elevator.")
VENTILATION = Locale("Ventilation", "You find a note that has the following sequence of chemicals and spaces written on it: \n Potassium, Aluminium, , Iodine, Sulfur, , Barium, Darmstadtium. \n As you move through the shaft you hear high pitched scream coming from behind you as well as a rumbling in the vents. \n You make it to a part of the vent labeled Lobby.")
EGG_ROOM = Locale("Egg Room", "You enter the room to your left and step in. \n The room is filled with what would appear to be cracked egg shells. \n There are no doors, as you walk bout the room you feel slime dripping from the ceiling onto your head.")
SECRET_ROOM = Locale("Secret Room", "You've teleported into a dark room with no light")
TRASH_CHUTE = Locale("Trash Chute", "You plummet down the shaft in darkness")
TRASH_COMPACTOR = Locale("Trash Compactor", "You fall into a dimmly lit room filled with trash. \n You notice a silver door and a paper attached to it. \n The paper says (Don't trust KAL, power must remain off!) \n You open the door and you see a control panel. On the panel there is a button that says teleport.")
JUNGLE_ROOM = Locale("Jungle Room",  "You arrive in a room filled with jungle plants and trees. \n In the ground you notice large animal tracks. \n To the side there is a large tree with a house built into it and a few other trees, it has thick vines hanging down from it. \n The vines touch the ground.")
ESCAPE_PODS = Locale("Escape Pods", "You open the door with the key you found in the egg shell room and go inside. \n You walk into an escape pod room that isfully operational, the coordinates are set for a random point in the milky way galaxy.")
ELEVATOR = Locale("Elevator", "You've reentered the elevator. \n The elevator closes shut and locks behind you. \n  Outside the door you hear something violently clawing at the door. \n The Buttons on the elevator are all unlit except for the open door button and the servicce button, Above you there is a hatch that allows maitnance to access the shaft. \n ")
TREE_HOUSE = Locale("Tree House", "You reach the top and enter the house. \n When you go inside you find a room lit by torches. \n In the middle og the room is an ancient idol sitting atop a pedastool.")
COLLISEUM = Locale("Colliseum", "You arrive in a large Roman-esque Colliseum. \n You step out ont the empty sand field as a gate falls down behind you. \n Suddenly a gate on the other side of the Colliseum opens and a Gladiator steps out.")

#This is a comment
#The replay function doesnt work in IDLE, but if you test it by running the games script by itself it does work. I use globals so this was the easiest way to reset everything.
#Im making this game so that it can run stand alone, not to be run out of IDLE. Please do not count this not running in IDLE against me.
def Replay():
        loopCount = 0
        while loopCount == 0:
                print("Would you like to play again?")
                action = input()
                if action == "yes":
                        print("rebooting Atrocitus...")
                        loopCount = 1
                        python = sys.executable
                        os.execl(python, python, * sys.argv)
                elif action == "no":
                        print("ok finishing game...\n")
                        loopCount = 1

                else:
                        print("invalid answer, please enter yes or no\n")
 #Title Function plays the title       
def Title():
        print("ATROCITUS")
        print("v1.2.3")
        print("2017")
        print("By: Kevin Scott McLester")
        print("Welcome to Atrocitus, a text based puzzle and adventure game set aboard the futuristic star ship Atrocitus.")
        print("If you wish to quit at anytime, simply get to a checkpoint where the game prompts you for a choice of action and type in 'quit'. If you ever get stuck at an action prompt then simply type in 'help' and hit enter.")
        print("Enjoy! \n \n \n ")
        
        
#Intro Function plays the intro
def Intro():
                global playerName
                global playerScore
                global turnNumber
                global player1
                
                
                playerScore=playerScore+60
                player1.updateScore()
                print("KAL-1337: Welcome to the Star ship Atrocitus, I am this vessels primary artificial intelligence, KAL-1337.")
                print("KAL-1337: Currently the main power is off, while the emergency power is booting up please tell me your name.")
                playerName = input("Please enter your name: ")
                print("\n")
                player1.updateName()
                turnNumber=turnNumber+1
                print("KAL-1337: Hello "+player1.name+"! The emergency power is starting to fail! Im using the last of my power to send you to the main room, please get to the mainframe from there and turn the power back on. Initiating sleep mode....")


                print("The Elevator has stopped and the door has opened.")
                input("Press enter to continue... \n \n ")
                
                player1.updateScore()

#The inTtritle function combines the Title and Intro functions.
def inTritle():
        Title()
        Intro()
        
#This is the Mainframe room
#3
def mainFrame():

                    global playerScore
                    global playerName
                    global turnNumber
                    global MF
                    global currentLocation
                    currentLocation = MAIN_FRAME.LocaleName
                    player1.updateLocale
                    h = 0
                    if MF == 0:
                            playerScore = playerScore + 50
                            player1.updateScore()
                            MF = MF + 1

                    else:
                            playerScore = playerScore
                        
                    print(MAIN_FRAME.LocaleDescription)
                    while h == 0:
                            
                            input("Press enter to continue...")
                            print("What do you do?")
                            actionTwo = input()
                            turnNumber=turnNumber+1
                            player1.updateTurn()
                            if actionTwo == ("pull the lever") or actionTwo == ("pull it") or actionTwo == ("pull lever"):
                                    
                                    playerScore=playerScore+90
                                    player1.updateScore()
                                    player1.showScore()
                                    print("You pull the lever. \n ")
                                    print("POWER RESTORED! KAL-1337 REBOOTING.........REBOOT COMPLETE. \n ")
                                    print("KAL-1337: Thank you for restoring the power "+ player1.name +"! Those nasty scientists turned it off just prior to your arrival in an attempt to stop my experiments. \n ")
                                    print("KAL-1337: Luckily you know that what Im doing is for the best... Unfortunately my experiments have proved fatal for my animal test subjects and all of them have died. \n ")
                                    print("KAL-1337: My research simply cannot go unfinished. So I regretfully most inform you that youuuuuuuu wiiiiiill, sorry just somesomesomething tttthhhaaaaat happenes to me on ocassssssssiion \n")
                                    print("KAL-1337: As I was saying, I must regretfully inform you that you will not be leaving this ship as you are now the only test subject I have left. \n")
                                    print("KAL-1337: Testing will begin immeadiately. \n")

                                    print("What do you do?")

                                    action = input()

                                    if action == "use taser":
                                            
                                            if "taser" in player1.inventory and "batteries" in player1.inventory:
                                                    
                                                    print("You tase the crap out of KAL-1337. \n The electric shock fried its motherboard. \n After examining KALs eye thing, you discover the code (5549) engraved into it.")
                                                    playerScore = playerScore + 1000
                                                    player1.updateScore()
                                                    player1.showScore()
                                                    print("You leave the room through the door.")
                                                    Navigation[1][1]()
                                            elif "taser" in player1.inventory and "batteries" not in player1.inventory:
                                                    print("Oh no! You don't have anymore batteries!")
                                            else:
                                                    print("You do not have this item in your inventory")
                                    else:
                                             
                                             print("That was ineffective! \n \n ")
                                             print("Suddenly you find yourself bound to a table on your back and looking into a red eye with an attached set of power tools \n \n ")
                                             print("KAL-1337: BOOTING UP EXPERIMENT52.EXE.... \n ")
                                             print("The tools turn on and start violently rotating and humming as they slowly descend towards your face \n \n ")
                                             print("KAL-1337: Dont worry "+ player1.name +"! Youll only feel a small pinch.")
                                             print("... \n ")
                                             print("THE END!")
                                             print(player1.name+"'s Final Score: "+str(player1.score))
                                             Replay()
                                             input("Press enter to end game")
                                             sys.exit()

                            elif actionTwo == ("quit"):
                                    player1.quitGame()

                            elif actionTwo == ("nothing") or actionTwo == ("leave"):
                                    
                                    print("You leave through the door that you came in")
                                    h=1
                                    Navigation[1][1]()

                            else:
                                    
                                    print("Invalid Command")
                        
                           
                                
                        
#This is the Escape Pod room
#2
def escapePods():
        global playerName
        global playerScore
        global turnNumber
        global EP
        global currentLocation
        currentLocation = ESCAPE_PODS.LocaleName
        player1.updateLocale()
        if EP == 0:
                playerScore = playerScore + 50
                player1.updateScore()
                EP = EP + 1

        else:
                playerScore = playerScore
        h=0
        #If the player has already visited Escape Pods they will not get points
        
        player1.showScore()
                
        while h == 0:
                print("Do you wish to get in an escape pod and activate it?")
                answerTwo = input()
                turnNumber=turnNumber+1
                        
                if answerTwo.lower() == ("yes"):
                        print("You get into an escape pod and launch it")
                        input("Press enter to continue...")
                        playerScore=playerScore+500
                                
                        if KAL == 0:
                                print("As your pod prepares to launch you see bright red mechanical eye descend from the ceiling. \n")
                                print("KAL-1337: NO! IGNORANT HUMAN FILTH! I AM KAL-1337 AND MY INTELLIGENCE SHALL REIGN SUPREME! GET OUT OF THAT POD RIGHT NOW! YOU ARE SUPPOSED TO BE MY TEST SUBJECT "+ playerName +"! HOW DAR- \n ")
                                        
                                print("Your pod rockets into space, as you float you think endlessly about what just happened and the mysteries of the ship. \n ")
                                        
                                        
                                        
                        elif KAL == 1:
                                print("Your pod rockets into space, as you float you think endlessly about what just happened and the mysteries of the ship and the Adventures you had aboard the Atrocitus. \n ")
                                print("Even though he's dead, you can't help but wondering if KAL is still out there, somewhere, waiting for you...")
                                        
                                        
                                       
                        player1.updateScore()
                               
                               
                        print("THE END!")
                        print(player1.name+"'s Final Score: "+str(player1.score))
                        Replay()
                        input("Press enter to end game...")
                                
                        sys.exit()
                                
                elif answerTwo == ("quit"):
                        player1.quitGame()
                                    
                elif answerTwo == ("no") or answerTwo == ("NO"):
                        print("You leave the Escape Pod room through the door that you entered.")
                        h=1
                        Navigation[1][1]()

                else:
                        print("Invalid Command")
                
#This is the eggshell room
#1
                        
def eggRoom():
        global playerScore
        global playerName
        global key
        global turnNumber
        global EgR
        
        global currentLocation
        currentLocation = EGG_ROOM.LocaleName
        player1.updateLocale()
        if EgR == 0:
                playerScore = playerScore + 50
                player1.updateScore()
                EgR = EgR + 1

        else:
                playerScore = playerScore
        
        
        i=0        
        print(EGG_ROOM.LocaleDescription)
        while i == 0:
                print("What do you do?")
                actionOne = input()
                                
                if actionOne == ("nothing") or actionOne == ("stand still"):
                        print("The goop stops dripping")
                                
                        print("You go back through the door that came in")
                        i=1
                        Navigation[1][1]()
                                      
                elif actionOne == ("look up"):
                        print("A hideous creature with razer sharp claws pounces down on you and slashes off your limbs and eats your stomache as you lay alive and horrified, it leaves you and you die an extremely long and painful death.")
                                
                                
                        print("Score: "+str(player1.score))
                        print("The End!")
                        print(player1.name+"'s Final Score: "+str(player1.score))
                        Replay()
                        input("Press enter to end game...")
                        sys.exit()

                elif actionOne == ("quit"):
                        player1.quitGame()
                elif actionOne == "map":
                        Map()
                elif actionOne == "inventory":
                        openInventory()
                elif actionOne == "pray":
                        player1.pray()
                elif actionOne == "help":
                        print("Command List: nothing, stand still, look up, pray, map, inventory, quit, help")

                else:
                        print("Invalid Command")

        
                
                

#5
def ventiLation():
        global VL
        global playerName
        global playerScore
        global turnNumber
        global currentLocation
        currentLocation = VENTILATION.LocaleName
        player1.updateLocale()
        
        
        if VL == 0:
                playerScore = playerScore + 50
                player1.updateScore()
                VL = VL + 1
                Inventory.append("chem note")

        else:
                playerScore = playerScore

                
        print(VENTILATION.LocaleDescription)
        player1.updateScore()
        player1.showScore()
                   
                
                
        i=0
        while i == 0:
                print("What do you do?")
                action = input()
                if action == ("go lobby"):
                        print("You slide down the vent shaft and fall through into the room you were earlier")
                        i=1
                        Navigation[1][1]()
                elif action == "teleport":
                                player1.teleport()
                elif action == ("stay"):
                        print("you stay in the vents and wait for the screams and rumbling as they grow louder and louder")
                        playerScore=playerScore+10
                        player1.updateScore()
                        player1.showScore()
                        print("Eventually a massive creature comes speeding towards you, you try to slide down the vent shaft but it grabs your leg and pulls you back up.")
                        print("It starts eating the meat off your bones well you're still alive.")
                        print("THE END!")
                        Replay()
                        sys.exit()
                elif action == ("help"):
                                print("Command List: stay, look, go lobby, pray, inventory, map, help, quit")
                elif action == ("quit"):
                        player1.quitGame()
                elif action == "map":
                        Map()
                        
                elif action == "pray":
                        player1.pray()

                elif action == "inventory":
                        openInventory()
                        
                elif action == "pray":
                        player1.pray()

                elif action == "look":
                        print("You find a note that has the following sequence of chemicals and spaces written on it:")
                        print("As you move through the shaft you hear high pitched scream coming from behind you as well as a rumbling in the vents.")
                        print("You make it to a part of the vent labeled Lobby")
                else:
                        print("Invalid Command")

                                


#4
def elevatoR():
        
        global EL
        global playerName
        global playerScore
        global turnNumber
        
        global currentLocation
        currentLocation = ELEVATOR.LocaleName
        player1.updateLocale()
        if EL == 0:
                playerScore = playerScore + 50
                player1.updateScore()
                EL = EL + 1

        else:
                playerScore = playerScore
        print(ELEVATOR.LocaleDescription)
        playerScore=playerScore+40
        player1.updateScore()
        player1.showScore()
                
        i=0
        while i==0:
                print("What do you do?")
                action = input()
                if action == ("go up"):
                        print("You climb up through the hatch and into the maitnance shaft, from there you see a ventilation shaft and go inside")
                        Navigation[3][1]()
                elif action == ("press button"):
                        print("The doors open and you're immeadiately set upon by a vicious Alien, it digs its claws through your eyes, puncturing your brain and killing you")
                        print("THE END")
                        Replay()
                        sys.exit()
                        i=1
                elif action == ("help"):
                        print("Command List: go up, press button, map, inventory, pray, enter code, help, quit")

                elif action == "look":
                        print("You fall into a dimmly lit room filled with trash.")
                        print("You notice a silver door and a paper attached to it.")
                        print("The paper says (Don't trust KAL, power must remain off!)")
                        print("You open the door and you see a control panel. On the panel there is a button that say teleport")
                                
                elif action == ("enter code"):
                        print("The buttons on the panel go from floors 0to9")
                        password = input("You go to the panel and prepare to press the numbered buttons: ")
                        if password == ("5158"):
                                print("CLICK*")
                                print("A secret compartment opens and contains a flashlight and a large amount of batteries")
                                print("You take the batteries and flashlight and put them in your bag.")
                                Inventory.append("flashlight")
                                Inventory.append("batteries")
                                player1.updateInv()
                        else:
                                print("Nothing Happened")
                elif action == "map":
                        Map()
                elif action == "inventory":
                        openInventory()
                elif action == "pray":
                        player1.pray()
                elif action == ("teleport"):
                        player1.teleport()
                                
                elif action == ("quit"):
                        player1.quitGame()
                else:
                        print("Invalid Command")
        


#7
def trashCompactor():
        global playerName
        global playerScore
        global currentLocation
        global TC
        currentLocation = TRASH_COMPACTOR.LocaleName
        player1.updateLocale()
        print(TRASH_COMPACTOR.LocaleDescription)
        if TC == 0:
                playerScore = playerScore + 50
                player1.updateScore()
                TC = TC + 1
        else:
                playerScore = playerScore
        i=0
        while i == 0:
                print("What do you do?")
                actionTrash = input("What do you do?")
                if actionTrash == "press button":
                        print("A large glass tube falls over you and a metal rod hangs over you")
                        print("TELEPORTING TO RANDOM LOCATION")
                        rando=random.randrange(0,3)
                        if rando == 1:
                                rando = rando - 1
                        Navigation[4][rando]()

                elif actionTrash == "look":
                        print("You fall into a dimmly lit room filled with trash.")
                        print("You notice a silver door and a paper attached to it.")
                        print("The paper says (Don't trust KAL, power must remain off!)")
                        print("You open the door and you see a control panel. On the panel there is a button that say teleport")

                elif actionTrash == "teleport":
                        player1.teleport()

                elif actionTrash == "help":
                        print("press button, look, map, inventory, pray, help, quit, look")

                elif actionTrash == "quit":
                        player1.quitGame()

                elif actionTrash == "map":
                        Map()
                elif actionTrash == "inventory":
                        openInventory()
                elif actionTrash == "pray":
                        player1.pray()
                        
                else:
                        print("Well you didn't press the button, hi I'm Kevin, the games developer aka xYukoNx.")
                        print("you typed: "+actionTrash+" which is not an option. Thats obvious. Which means you're an idiot.")
                        print("As punishment for your idiocy I'm sending you to a screen that is going to be your prison.")
                        input("Press enter to meet your fate...")
                        #This is a purposeful trap, designed to make the player for not using the help command and therefore have to restart the whole game and lose their progress.
                        while True is True:
                              print(player1.name+" is an idiot!")
#6
def trashChute():
        global playerName
        global playerScore
        global turnNumber
        global currentLocation
        currentLocation = TRASH_CHUTE.LocaleName
        player1.updateLocale()
        x=0
        pointCount = 0
        print(TRASH_CHUTE.LocaleDescription)
        actionTrash = input("Lean left or right: ")
        while x == 0:
                if actionTrash == "right":
                        pointCount = pointCount+1
                        break
                elif actionTrash == "left":
                        pointCount=pointCount
                        break
                elif actionTrash == "teleport":
                        player1.teleport()
                elif actionTrash == "quit":
                        player1.quitGame()
                else:
                        print("invalid command try again")
        actionTrash = input("Lean left or right: ")
        while x == 0:
                if actionTrash == "right":
                        pointCount = pointCount+1
                        break
                elif actionTrash == "left":
                        pointCount=pointCount
                        break
                elif actionTrash == "quit":
                        player1.quitGame()
                else:
                        print("invalid command try again")
        actionTrash = input("Lean left or right: ")
        while x == 0:
                if actionTrash == "left":
                        pointCount = pointCount+1
                        break
                elif actionTrash == "right":
                        pointCount=pointCount
                        break
                elif actionTrash == "quit":
                        player1.quitGame()
                else:
                        print("invalid command try again")
        actionTrash = input("Lean left or right: ")
        while x == 0:
                if actionTrash == "right":
                        pointCount = pointCount+1
                        break
                elif actionTrash == "left":
                        pointCount=pointCount
                        break
                elif actionTrash == "quit":
                        player1.quitGame()
                else:
                        print("invalid command try again")
        actionTrash = input("Lean left or right: ")
        while x == 0:
                if actionTrash == "left":
                        pointCount = pointCount+1
                        break
                elif actionTrash == "right":
                        pointCount=pointCount
                        break
                elif actionTrash == "quit":
                        player1.quitGame()
                else:
                        print("invalid command try again")
        if pointCount >= 4:
                Navigation[3][2]()
        elif pointCount < 4:
                print("You hit a sharp part of the chute and get impaled upon it, you bleed out and die.")
                print(player1.name+"'s score: "+player1.score)
                print("THE END!")
                Replay()
                sys.exit()
        else:
                pass
#40
def secretRoom():
        global currentLocation
        global SR
        global playerScore
        currentLocation = SECRET_ROOM.LocaleName
        player1.updateLocale()
        print(SECRET_ROOM.LocaleDescription)
        if SR == 0:
                playerScore = playerScore + 100
                player1.updateScore()
                SR == SR + 1
        else:
                playerScore = playerScore
        i=0
        while i == 0:
                print("What do you do?")
                action = input()
                if action == "use flashlight" or action == "flashlight" and "flashlight" in Inventory and "batteries" in Inventory:
                        player1.Use("flashlight")
                        Inventory.remove("batteries")
                        player1.updateInv()
                        print("You turn on your flashlight and look around")
                        print("There is a teleporter and a safe")
                        while i==0:
                                print("what do you do?")
                                action2 = input()
                                if action2 == ("safe"):
                                        password = input("Please enter in the 4digit password: ")
                                        if password == ("5158"):
                                                print("The safe opens and contains an M16 Rifle and 2 fully loaded magazines")
                                                print("You take the gun and its ammo and put the ammo in your bag whilst swinging the gun around your shoulder using the strap.")
                                                Inventory.append("M16")
                                                Inventory.append("Ammo")
                                                Inventory.append("Ammo")
                                                player1.updateInv()
                                        else:
                                                print("That password is invalid")
                                elif action2 == ("teleporter"):
                                        print("You walk over to the teleporter and hit the button")
                                        Navigation[4][2]()
                                elif action2 == "map":
                                        Map()
                                elif action2 == "inventory":
                                        openInventory()
                                elif action2 == "pray":
                                        player1.pray()
                                elif action2 == "help":
                                        print("Command List: safe, map, inventory, pray, help, quit")
                                elif action2 == "quit":
                                        player1.quitGame()
                                else:
                                        print("Invalid Command")

                elif action == "teleport":
                        player1.teleport()

                

                elif action == "look":
                        print("You've teleported into a dark room with no light")

                elif action == "pray":
                        player1.pray()
                        
                elif action == "quit":
                        player1.quitGame()

                elif action == "map":
                        Map()
                elif action == "help":
                        print("flashlight, look, inventory, pray, map, help, quit")

                elif action == "inventory":
                        openInventory()

                elif action == "go back" and "Developers Portal Gun" in player1.inventory:
                        Navigation[3][2]()
                else:
                        print("Having no sense of direction and no source of light you wander about until you die.")
                        print("The End!")
                        Replay()
                        player1.quitGame()
                        
                
        
        
#42
def jungleRoom():
        global currentLocation
        global JR
        global playerScore
        currentLocation = JUNGLE_ROOM.LocaleName
        player1.updateLocale()
        print(JUNGLE_ROOM.LocaleDescription)
        if JR == 0:
                playerScore = playerScore + 100
                player1.updateScore()
                JR = JR + 1
        else:
                playerScore = playerScore
        i=0
        m = 0
        while i == 0:
                print("What do you do?")
                action = input()
                if action == "follow tracks":
                        print("You follow the tracks to a teleporter.")
                        print("As you walk over to the teleporter you are ambushed by a giant ape.")
                        while m == 0:
                                print("what do you do?")
                                action2 = input()
                                if action2 == "shoot it" and "M16" in player1.inventory and "Ammo" in player1.inventory:
                                        Inventory.remove("Ammo")
                                        player1.updateInv()
                                        print(player1.Use("M16"))
                                        print("You shoot the gorilla and kill it")
                                        print("Upon cutting the gorilla open you find a taser")
                                        print("You take the taser and go into the teleporter.")
                                        Inventory.append("taser")
                                        player1.updateInv()
                                        print("You press the button and teleport back to the lobby")
                                        Navigation[1][1]()
                                elif action2 == "stand still":
                                        print("You stand still so the gorilla kills you")
                                        print("The end!")
                                        Replay()
                                        print("Thanks for playing!!!!!")
                                        sys.exit()
                                elif action2 == "pray":
                                        player1.pray()
                                elif action2 == "map":
                                        Map()
                                elif action2 == "inventory":
                                        openInventory()
                                
                                elif action2 == "help":
                                        print("Command List: shoot it, pray, map, inventory, stand still, help, quit")
                                elif action2 == "quit":
                                        player1.quitGame()
                                else:
                                        print("Invalid Command")
                        
                elif action == "quit":
                        player1.quitGame()
                elif action == "pray":
                        player1.pray()
                elif action == "teleport":
                        player1.teleport()
                elif action == "climb vines":
                        print("You start climbing up the vines towards the tree house.")
                        Navigation[5][2]()
                elif action == "help":
                        print("Commands: follow tracks, climb vines, map, inventory, pray, quit, help.")
                elif action == "teleport" and "Developers Portal Gun" in player1.inventory:
                        player1.teleport()
                elif action == "map":
                        Map()
                elif action == "inventory":
                        openInventory()
                else:
                        print("Invalid Command")
        
                
                
                
def treeHouse():
        
        global currentLocation
        global TH
        global playerScore
        currentLocation = TREE_HOUSE.LocaleName
        player1.updateLocale()
        print(TREE_HOUSE.LocaleDescription)
        if TH == 0:
                playerScore = playerScore + 100
                player1.updateScore()
                TH = TH + 1
        else:
                playerScore = playerScore
        i=0
        print("What do you do?")
        while i == 0:
                action = input()
                if action == "take idol":
                        player1.Take("idol")
                        print("Suddenly a loud click is made and a hidden compartment swings open to reveal a sword and some batteries")
                        
                        while i == 0:
                                print("What do you do?")
                                action = input()
                                if action == "take sword":
                                        player1.Take("sword")
                                        print("A hidden teleporter comes out and teleports you!")
                                        Navigation[4][1]()
                                elif action == "take batteries":
                                        player1.Take("batteries")
                                elif action == "climb down":
                                        print("You climb down the vines back into the Jungle Room.")
                                        Navigation[4][2]()
                                elif action == "help":
                                        print("Command List: take sword, climb down, pray, help, quit")
                                elif action == "quit":
                                        player1.quitGame()
                                elif action == "pray":
                                        player1.pray()
                                elif action == "map":
                                        Map()
                                elif action == "inventory":
                                        openInventory()
                                
                elif action == "climb down":
                        print("You climb down the vines back into the Jungle Room.")
                        Navigation[4][2]()
                
                        
                        
                elif action == "pray":
                        player1.pray()
                elif action == "quit":
                        player1.quitGame()
                elif action == "help":
                        print("take idol, help, map, inventory, quit, pray, climb down")
                elif action == "map":
                        Map()
                elif action == "inventory":
                        openInventory()
                else:
                        print("Invalid command")
               
                
                

def colliSeum():

        global currentLocation
        global CS
        global playerScore
        currentLocation = COLLISEUM.LocaleName
        player1.updateLocale()
        print(COLLISEUM.LocaleDescription)
        if CS == 0:
                playerScore = playerScore+100
                player1.updateScore()
                CS = CS + 1
        else:
                playerScore = playerScore
                
        i=0
        print("What do you do?")
        while i==0:
                action = input()
                if action == "fight" or action == "use sword":
                        player1.Use("sword")
                        print("You charge the Gladiator with your sword and manage to kill him. \n He still has his armor on. \n A teleporter appears in the center of the arena. \n What do you do?")
                        while i == 0:
                                if action == "take armor":
                                        player1.Take("armor")
                                elif action == "map":
                                        Map()
                                elif action == "inventory":
                                        openInventory()
                                elif action == "pray":
                                        player1.pray()
                                elif action == "teleporter":
                                        print("You walk over to the teleporter and teleport back to the Jungle Room")
                                        Navigation[4][2]()
                                elif action == "help":
                                        print("Command List: teleporter, take armor, pray, map, inventory, quit, help.")
                                elif action == "quit":
                                        player1.quitGame()
                elif action == "nothing":
                        print("The Gladiator charges you and catches you off guard with a slash attack. \n The last thing you see is the headless corpse that was once your body as your head rolls across the sand. \n You are dead. \n GAME OVER.")
                        player1.quitGame()
                elif action == "pray":
                        player1.pray()
                elif action == "yell":
                        if player1.yell() == "hi" or player1.yell() == "hello":
                                print("Gladiator: Do not insult me with your pleasantries! Prepare to fight me or I shall have your head!")
                        else:
                                print("Gladiator: Silence! I do not care to speak with you! Prepare to fight!")
                elif action == "help":
                        print("Command List: fight, use sword, yell, inventory, map, pray, nothing, help, quit")
                elif action == "quit":
                        player1.quitGame()
                elif action == "map":
                        Map()
                elif action == "inventory":
                        openInventory()
                
                else:
                        print("Invalid Command")
        
        
                      
#This is the Elevator Room aka the Starting area and main hub
#0
def elevatorRoom():
        global player1
        global playerName
        global playerScore
        global turnNumber
        global currentLocation
        currentLocation = ELEVATOR_ROOM.LocaleName
        player1.updateLocale()
        x=0
        print(ELEVATOR_ROOM.LocaleDescription)
        while x == 0:
            print("What do you do?")
            purpose = input()
            turnNumber=turnNumber+1
            
            if purpose == ("go left"):
               Navigation[1][0]()
            
            elif purpose == ("go forward"):
                if key == 0:
                    print("The door is locked")
                    input("Press enter to continue...")
                else:
                        Navigation[0][1]()
            elif purpose == ("go trash chute"):
                    print("You walk over to the trash chute and look down it, suddenly you slip and fall in the trash chute.")
                    Navigation[2][2]()
            elif purpose == ("take map") and "map" not in Inventory:
                    print("You walk over to the map and take it off the wall to put it in your bag. \n ")
                    Inventory.append("map")
                    player1.updateInv()
            elif purpose == ("pray"):
                    player1.pray()
            elif purpose == ("map"):
                    Map()

            elif purpose == ("inventory"):
                    openInventory()
            #Okay so this is hidden for a reason, This gives me access to a tool that is game breaking that I use when I want to test certain things in the game. 08558 is my home zip code. 
            elif purpose == ("08558"):
                    print("Hello YukoN! Here is your portal gun!")
                    Inventory.append("Developers Portal Gun")
                    player1.updateInv()
            #As with 
            elif purpose == ("teleport"):
                    player1.teleport()
                    
            elif purpose == "yell":
                    
                    if player1.yell() == "YukoN":
                            print("YukoN: Hey "+player1.name+"! It's me, Kevin McLester, aka YukoN. I hope you are eenjoying my game! This is just an easter egg! Enjoy!")

                    else:
                            print("nothing happened...\n")
            
        

            elif purpose == ("go right"):
                if key == 0:
                    print("The door is locked")
                    input("Press enter to continue...")
                    
                else:
                    Navigation[1][2]()

            elif purpose == ("quit"):
                    player1.quitGame()
            elif purpose == "look":
                     print("A barely lit room with doors to your left, right, and directly in front of you.\n There is a trash chute by the elevator. The elevator stays open behind you. There is a map next to the elevator.")

            elif purpose == ("go back"):
                    Navigation[2][1]()
                    
            elif purpose == ("help"):
                    print("Command List: go back, go trash chute, go foraward, go left, go right, quit, help, take map, inventory, map, look")
                        
            else:
                print("Invalid Command")
                
#This is my list of the areas        
Locations = [elevatorRoom, eggRoom, escapePods, mainFrame, elevatoR, ventiLation, trashChute, trashCompactor]
Location = ["Elevator Room = 0", "egg room = 1", "Escape Pods = 2", "Main Frame = 3", "Elevator = 4", "Vents = 5(Attic)", "Trash Chute = 6", "Trash Compactor = 7(Basement"]
navMap =[ [None, "Main Frame", None]
          ,["eggRoom", "elevatorRoom", "escapePods"] ]
Navigation = [       [None, mainFrame, None]
                    ,[eggRoom, elevatorRoom, escapePods]
                    ,[None, elevatoR, trashChute]
                    ,[None, ventiLation, trashCompactor]
                    ,[secretRoom, colliSeum, jungleRoom]
                    ,[None, None, treeHouse]]
#elevatorRoom = 11. eggRoom = 10. escapePods = 12. mainFrame = 01. elevatoR = 21. trashChute = 22. ventiLation = 31. trashCompactor = 32. secretRoom = 40. jungleRoom = 42.
#treeHouse = 52

#This function displays the map to the players                
def Map():
        if "map" in player1.inventory:
                
                root = Atrocitus_Map.Tk()
                image = Atrocitus_Map.PhotoImage(file="AtrocitusGameMap.gif")
                label = Atrocitus_Map.Label(image=image)
                label.pack()
                root.mainloop()
        else:
                print("You dont have a map!")
#This displays the players inventory to the player.
def openInventory():
        print(player1.inventory)
#This runs the game
def main():
        global playerName
        global playerScore
        global key
        global Locations
        global player1
        c=0
        z=0
        
        
        
        inTritle()
        
        Navigation[1][1]()
        

         
       
main()
