#Author: Kevin McLester
#My gamekicks ass
#This is another comment for a commit
import sys
import random
playerScore=0
playerName=""
key=0
turnNumber=0
visitMainF=0
visitEggS=0
visitElevR=0
visitEscaP=0
visitElevator=0
visitVentilation=0
currentLocation = ""
Inventory = []
Flashlight="flashlight"
lobbymap="map"

class Player:
        def __init__(self, name, score, currLocale, move_count, inventory):
                self.name = name
                self.score = score
                self.currLocale = currLocale
                self.move_count = move_count
                self.inventory = inventory
                Inventory = []
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
                print(self.score)

        def quitGame(self):
                print(player1.name+"'s Final Score: "+str(player1.score))
                print("Thank you for playing Atrocitus "+player1.name+"!")
                print("Goodbye!")
                print("THE END!")
                input("Press enter to end game...")
                sys.exit()

        def teleport(self):
                if "Developers Portal Gun" in player1.inventory:
                        print("Where would you like to teleport "+player1.name+"?")
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
                        print("You used the "+item)
                        return True
                else:
                        print("You do not have that item!")
                        return False
        def Take(self, item):
                pass
                
player1 = Player("player", 0, "ElevatorRoom", 0, " ")
        

class Locale:
        def __init__(self, LocaleName, LocaleDescription):
                self.LocaleName = LocaleName
                self.LocaleDescription = LocaleDescription

MAIN_FRAME = Locale("Main Frame", "You open the door with the key you found and go in. \n Theres a large lever with a label on it that says POWER. \n What do you do?")
ELEVATOR_ROOM = Locale("Elevator Room", "You step out into a barely lit room with doors to your left, right, and directly in front of you. There is a trash chute by the elevator. The elevator stays open behind you. \n There is a map next to the elevator.")
VENTILATION = Locale("Ventilation", "")
EGG_ROOM = Locale("Egg Room", "You enter the room to your left and step in. \n The room is filled with what would appear to be cracked egg shells. \n There are no doors, as you walk bout the room you feel slime dripping from the ceiling onto your head.")
SECRET_ROOM = Locale("Secret Room", "")
TRASH_CHUTE = Locale("Trash Chute", "")
TRASH_COMPACTOR = Locale("Trash Compactor", "")
JUNGLE_ROOM = Locale("Jungle Room",  "")
ESCAPE_PODS = Locale("Escape Pods", "You open the door with the key you found in the egg shell room and go inside. \n You walk into an escape pod room that isfully operational, the coordinates are set for a random point in the milky way galaxy.")
ELEVATOR = Locale("Elevator", "")
TREE_HOUSE = Locale("Tree House", "You reach the top and enter the house. \n When you go inside you find a room lit by torches. \n In the middle og the room is an ancient idol sitting atop a pedastool.")

#This is a comment
#Title function plays the title
def Title():
        print("ATROCITUS")
        print("v1.2.3")
        print("2017")
        print("By: Kevin Scott McLester")
        print("Welcome to Atrocitus, a text based puzzle and adventure game set aboard the futuristic star ship Atrocitus.")
        print("If you wish to quit at anytime, simply get to a checkpoint where the game prompts you for a choice of action and type in 'quit'. If you ever get stuck at an action prompt then simply type in 'help' and hit enter.")
        print("Enjoy!")
        print(" ")
        print(" ")
        print(" ")
        
#Intro Function plays the intro
def Intro():
                global playerName
                global playerScore
                global turnNumber
                global player1
                
                print("Welcome to the game, if there is no question asked of you simply hit enter to continue")
                input("Press enter to continue...")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                print("You awake in an elevator")
                input("Press enter to continue...")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                print("Welcome to the Star ship Atrocitus, I am this vessels primary artificial intelligence, KAL-1337.")
                input("Press enter to continue...")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                print("Currently the main power is off, while the emergency power is booting up please tell me your name.")
                input("Press enter to continue...")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                print("Please enter your name.")
                playerName = input()
                player1.updateName()
                turnNumber=turnNumber+1
                print("Hello "+player1.name+"! The emergency power is starting to fail! Im using the last of my power to send you to the main room, please get to the mainframe from there and turn the power back on. Initiating sleep mode....")
                input("Press enter to continue")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                print("The Elevator has stopped and the door has opened.")
                input("Press enter to continue")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
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
                    global visitMainF
                    global currentLocation
                    currentLocation = "Main Frame"
                    player1.updateLocale
                    h = 0
                    visitMainF=visitMainF+1
                    if visitMainF == 1:
                            print("You open the door with the key you found and go in.")
                            input("Press enter to continue...")
                            print("Theres a large lever with a label on it that says POWER")
                            while h == 0:
                                    input("Press enter to continue...")
                                    print("What do you do?")
                                    actionTwo = input()
                                    turnNumber=turnNumber+1
                                    if actionTwo == ("pull the lever") or actionTwo == ("pull it") or actionTwo == ("pull lever"):
                                        print("You pull the lever")
                                        input("Press enter to continue...")
                                        playerScore=playerScore+10
                                        print("Score: "+str(playerScore))
                                        print(" ")
                                        print("POWER RESTORED! KAL-1337 REBOOTING.........REBOOT COMPLETE.")
                                        input("Press enter to continue...")
                                        playerScore=playerScore+10
                                        print("Score: "+str(playerScore))
                                        print(" ")
                                        print("Thank you for restoring the power "+ playerName +"! Those nasty scientists turned it off just prior to your arrival in an attempt to stop my experiments.")
                                        input("Press enter to continue...")
                                        playerScore=playerScore+10
                                        print("Score: "+str(playerScore))
                                        print(" ")
                                        print("Luckily you know that what Im doing is for the best... Unfortunately my experiments have proved fatal for my animal test subjects and all of them have died.")
                                        input("Press enter to continue...")
                                        playerScore=playerScore+10
                                        print("Score: "+str(playerScore))
                                        print(" ")
                                        print("My research simply cannot go unfinished. So I regretfully most inform you that youuuuuuuu wiiiiiill, sorry just somesomesomething tttthhhaaaaat happenes to me on ocassssssssiion")
                                        input("Press enter to continue...")
                                        playerScore=playerScore+10
                                        print("Score: "+str(playerScore))
                                        print(" ")
                                        print("As I was saying, I must regretfully inform you that you will not be leaving this ship as you are now the only test subject I have left")
                                        input("Press enter to continue...")
                                        playerScore=playerScore+10
                                        print("Score: "+str(playerScore))
                                        print(" ")
                                        print("Testing will begin immeadiately")
                                        input("Press enter to continue...")
                                        playerScore=playerScore+10
                                        print("Score: "+str(playerScore))
                                        print(" ")
                                        print(" ")
                                        print("Suddenly you find yourself bound to a table on your back and looking into a red eye with an attached set of power tools")
                                        input("Press enter to continue...")
                                        playerScore=playerScore+10
                                        print("Score: "+str(playerScore))
                                        print(" ")
                                        print(" ")
                                        print("BOOTING UP EXPERIMENT52.EXE....")
                                        print(" ")
                                        print("The tools turn on and start violently rotating and humming as they slowly descend towards your face")
                                        input("Press enter to continue...")
                                        playerScore=playerScore+10
                                        print("Score: "+str(playerScore))
                                        print(" ")
                                        print(" ")
                                        print("Dont worry "+ playerName +"! Youll only feel a small pinch.")
                                        print("...")
                                        print(" ")
                                        print("THE END!")
                                        print(player1.name+"'s Final Score: "+str(playerScore))
                                        input("Press enter to end game")
                                        sys.exit()

                                    elif actionTwo == ("quit"):
                                            player1.quitGame()

                                    elif actionTwo == ("noting") or actionTwo == ("leave"):
                                            print("You leave through the door that you came in")
                                            h=1

                                    else:
                                        print("Invalid Command")
                        
                            else:
                                    print("You open the door with the key you found and go in.")
                                    input("Press enter to continue...")
                                    print("Theres a large lever with a label on it that says POWER")
                                    input("Press enter to continue...")
                                    print("What do you do?")
                                    actionTwo = input()
                                    turnNumber=turnNumber+1
                                    
                                    if actionTwo == ("pull the lever") or actionTwo == ("pull it") or actionTwo == ("pull lever"):
                                        print("You pull the lever")
                                        input("Press enter to continue...")
                                        print("POWER RESTORED! KAL-1337 REBOOTING.........REBOOT COMPLETE.")
                                        input("Press enter to continue...")
                                        print("Thank you for restoring the power "+ playerName +"! Those nasty scientists turned it off just prior to your arrival in an attempt to stop my experiments.")
                                        input("Press enter to continue...")
                                        print("Luckily you know that what Im doing is for the best... Unfortunately my experiments have proved fatal for my animal test subjects and all of them have died.")
                                        input("Press enter to continue...")
                                        print("My research simply cannot go unfinished. So I regretfully most inform you that youuuuuuuu wiiiiiill, sorry just somesomesomething tttthhhaaaaat happenes to me on ocassssssssiion")
                                        input("Press enter to continue...")
                                        print("As I was saying, I must regretfully inform you that you will not be leaving this ship as you are now the only test subject I have left")
                                        input("Press enter to continue...")
                                        print("Testing will begin immeadiately")
                                        input("Press enter to continue...")
                                        print(" ")
                                        print("Suddenly you find yourself bound to a table on your back and looking into a red eye with an attached set of power tools")
                                        input("Press enter to continue...")
                                        print(" ")
                                        print("BOOTING UP EXPERIMENT52.EXE....")
                                        print(" ")
                                        print("The tools turn on and start violently rotating and humming as they slowly descend towards your face")
                                        input("Press enter to continue...")
                                        print(" ")
                                        print("Dont worry "+ playerName +"! Youll only feel a small pinch.")
                                        print("...")
                                        print(" ")
                                        print("THE END!")
                                        print(playerName+"'s Final Score: "+str(playerScore))
                                        input("Press enter to end game")
                                        sys.exit()

                                    elif purpose == ("quit"):
                                            player1.quitGame()

                                    elif actionTwo == ("noting") or actionTwo == ("leave"):
                                            print("You leave through the door that you came in")
                                            h=1

                                    else:
                                        print("Invalid Command")
                                
                        
#This is the Escape Pod room
#2
def escapePods():
        global playerName
        global playerScore
        global turnNumber
        global visitEscaP
        visitEscaP=visitEscaP+1
        global currentLocation
        currentLocation = "Escape Pods"
        player1.updateLocale()
        
        h=0
        #If the player has already visited Escape Pods they will not get points
        if visitEscaP != 1:
                print("You open the door with the key you found in the egg shell room and go inside")
                input("Press enter to continue...")
                print("You walk into an escape pod room that isfully operational, the coordinates are set for a random point in the milky way galaxy.")
                input("Press enter to continue...")
                while h == 0:
                        print("Do you wish to get in an escape pod and activate it?")
                        answerTwo = input()
                        turnNumber=turnNumber+1
                        
                        if answerTwo == ("yes") or answerTwo == ("YES") or answerTwo == ("Yes"):
                                print("You get into an escape pod and launch it")
                                input("Press enter to continue...")
                                print("As your pod prepares to launch you see bright red mechanical eye descen from the ceiling")
                                input("Press enter to continue...")
                                print(" ")
                                print("NO! IGNORANT HUMAN FILTH! I AM KAL-1337 AND MY INTELLIGENCE SHALL REIGN SUPREME! GET OUT OF THAT POD RIGHT NOW! YOU ARE SUPPOSED TO BE MY TEST SUBJECT "+ playerName +"! HOW DAR-")
                                print(" ")
                                print("Your pod rockets into space, as you float you think endlessly about what just happened and the mysteries of the ship.")
                                input("Press enter to continue...")
                                print(" ")
                                print("THE END!")
                                print(player1.name+"'s Final Score: "+str(player1.score))
                                input("Press enter to end game...")
                                sys.exit()
                                
                        elif answerTwo == ("quit"):
                                    player1.quitGame()
                                    
                        elif answerTwo == ("no") or answerTwo == ("NO"):
                                print("You leave the Escape Pod room through the door that you entered.")
                                h=1

                        else:
                                print("Invalid Command")
        else:
                print("You open the door with the key you found in the egg shell room and go inside")
                input("Press enter to continue...")
                playerScore=playerScore+20
                player1.updateScore()
                player1.showScore()
                print(" ")
                print("You walk into an escape pod room that isfully operational, the coordinates are set for a random point in the milky way galaxy.")
                input("Press enter to continue...")
                print(" ")
                while h == 0:
                        print("Do you wish to get in an escape pod and activate it?")
                        answerTwo = input()
                        turnNumber=turnNumber+1
                        
                        if answerTwo == ("yes") or answerTwo == ("YES") or answerTwo == ("Yes"):
                                print("You get into an escape pod and launch it")
                                input("Press enter to continue...")
                                playerScore=playerScore+10
                                print("Score: "+str(playerScore))
                                print(" ")
                                print("As your pod prepares to launch you see bright red mechanical eye descen from the ceiling")
                                input("Press enter to continue...")
                                playerScore=playerScore+10
                                print("Score: "+str(playerScore))
                                print(" ")
                                print(" ")
                                print("NO! IGNORANT HUMAN FILTH! I AM KAL-1337 AND MY INTELLIGENCE SHALL REIGN SUPREME! GET OUT OF THAT POD RIGHT NOW! YOU ARE SUPPOSED TO BE MY TEST SUBJECT "+ playerName +"! HOW DAR-")
                                print(" ")
                                print("Your pod rockets into space, as you float you think endlessly about what just happened and the mysteries of the ship.")
                                input("Press enter to continue...")
                                playerScore=playerScore+10
                                print("Score: "+str(playerScore))
                                print(" ")
                                print(" ")
                                print("THE END!")
                                print(playerName+"'s Final Score: "+str(playerScore))
                                input("Press enter to end game...")
                                sys.exit()
                                
                        elif answerTwo == ("quit"):
                                    player1.quitGame()
                                    
                        elif answerTwo == ("no") or answerTwo == ("NO"):
                                print("You leave the Escape Pod room through the door that you entered.")
                                h=1

                        else:
                                print("Invalid Command")
                
#This is the eggshell room
#1
def eggRoom():
        global playerScore
        global playerName
        global key
        global turnNumber
        global visitEggS
        visitEggS=visitEggS+1
        global currentLocation
        currentLocation = "Egg Room"
        player1.updateLocale()
        
        if visitEggS != 1:
        
                i=0        
                print(EGG_ROOM.LocaleDescription)
                while i == 0:
                        print("What do you do?")
                        actionOne = input()
                                
                        if actionOne == ("nothing") or actionOne == ("stand still"):
                                print("The goop stops dripping")
                                input("Press enter to continue...")
                                
                                print("Score: "+str(playerScore))
                                print("You go back through the door that came in")
                                i=1
                                      
                        elif actionOne == ("look up"):
                                print("A hideous creature with razer sharp claws pounces down on you and slashes off your limbs and eats your stomache as you lay alive and horrified, it leaves you and you die an extremely long and painful death.")
                                input("Press enter to continue...")
                                
                                print("Score: "+str(playerScore))
                                print("The End!")
                                print(playerName+"'s Final Score: "+str(playerScore))
                                input("Press enter to end game...")
                                sys.exit()

                        elif purpose == ("quit"):
                            player1.quitGame()

                        else:
                                        print("Invalid Command")

        else:
                i=0
                        
                
                playerScore=playerScore+50
                
                
                print(EGG_ROOM.LocaleDescription)                
                while i == 0:
                        print("What do you do?")
                        actionOne = input()
                                
                        if actionOne == ("nothing") or actionOne == ("stand still"):
                                print("The goop stops dripping and you find a key and a black note that says 5158 on the floor and pick it up.")
                                key = 1
                                Inventory.append("key")
                                Inventory.append("black note")
                                player1.updateInv()
                                input("Press enter to continue...")
                                playerScore=playerScore+10
                                print("Score: "+str(playerScore))
                                print("You go back through the door that came in")
                                i=1
                                      
                        elif actionOne == ("look up"):
                                print("A hideous creature with razer sharp claws pounces down on you and slashes off your limbs and eats your stomache as you lay alive and horrified, it leaves you and you die an extremely long and painful death.")
                                input("Press enter to continue...")
                                print("Score: "+str(playerScore))
                                print("The End!")
                                print(playerName+"'s Final Score: "+str(playerScore))
                                input("Press enter to end game...")
                                sys.exit()

                        elif actionOne == ("quit"):
                            player1.quitGame()

                        else:
                                        print("Invalid Command")

#5
def ventiLation():
        global visitVentilation
        global playerName
        global playerScore
        global turnNumber
        global currentLocation
        currentLocation = "Ventilation"
        player1.updateLocale()
        visitVentilation = visitVentilation+1
        
        if visitVentilation == 1:
                print("You find a note that has the following sequence of chemicals and spaces written on it:")
                input("Press enter to continue")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                print("Potassium, Aluminium, , Iodine, Sulfur, , Barium, Darmstadtium")
                Inventory.append("chem note")
                input("Press enter to continue")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                print("As you move through the shaft you hear high pitched scream coming from behind you as well as a rumbling in the vents.")
                input("Press enter to continue")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                print("You make it to a part of the vent labeled Lobby")
                input("Press enter to continue")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                i=0
                while i == 0:
                        print("What do you do?")
                        action = input()
                        if action == ("go lobby"):
                                print("You slide down the vent shaft and fall through into the room you were earlier")
                                i=1
                                Locations[0]()
                        elif action == ("stay"):
                                print("you stay in the vents and waitfor the screams and rumbling as they grow louder and louder")
                                input("Press enter to continue")
                                playerScore=playerScore+10
                                print("Score: "+str(playerScore))
                                print("Eventually a massive creature comes speeding towards you, you try to slide down the vent shaft but it grabs your leg and pulls you back up.")
                                print("It starts eating the meat off your bones well you're still alive.")
                                print("THE END!")
                                sys.exit()
                        elif action == ("help"):
                                print("Command List: stay, go lobby, help, quit")
                        elif action == ("quit"):
                                player1.quitGame()
                        elif action == "map":
                                Map()

                        elif action == "inventory":
                                openInventory()

                        elif action == "look":
                                print("You find a note that has the following sequence of chemicals and spaces written on it:")
                                print("As you move through the shaft you hear high pitched scream coming from behind you as well as a rumbling in the vents.")
                                print("You make it to a part of the vent labeled Lobby")
                        else:
                                print("Invalid Command")

                                

        else:
                print("You find a note that has the following sequence of chemicals and spaces written on it:")
                input("Press enter to continue")
                
                print("Score: "+str(playerScore))
                print("Potassium, Aluminium, , Iodine, Sulfur, , Barium, Darmstadtium")
                input("Press enter to continue")
                
                print("Score: "+str(playerScore))
                print("As you move through the shaft you hear high pitched scream coming from behind you as well as a rumbling in the vents.")
                input("Press enter to continue")
                
                print("Score: "+str(playerScore))
                print("You make it to a part of the vent labeled Lobby")
                input("Press enter to continue")
                
                print("Score: "+str(playerScore))
                i=0
                while i == 0:
                        print("What do you do?")
                        action = input()
                        if action == ("go lobby"):
                                print("You slide down the vent shaft and fall through into the room you were earlier")
                                i=1
                                Locations[0]()
                        elif action == ("stay"):
                                print("you stay in the vents and waitfor the screams and rumbling as they grow louder and louder")
                                input("Press enter to continue")
                                
                                print("Score: "+str(playerScore))
                                print("Eventually a massive creature comes speeding towards you, you try to slide down the vent shaft but it grabs your leg and pulls you back up.")
                                print("It starts eating the meat off your bones well you're still alive.")
                                print("THE END!")
                                sys.exit()
                        elif action == ("help"):
                                print("Command List: stay, go lobby, help, quit, look")
                        elif action == ("quit"):
                               player1.quitGame()
                        elif action == "look":
                                print("You find a note that has the following sequence of chemicals and spaces written on it:")
                                print("As you move through the shaft you hear high pitched scream coming from behind you as well as a rumbling in the vents.")
                                print("You make it to a part of the vent labeled Lobby")
                        elif action == "map":
                                Map()
                        elif action == "inventory":
                                openInventory()
                        else:
                                print("Invalid Command")

#4
def elevatoR():
        
        global visitElevator
        global playerName
        global playerScore
        global turnNumber
        visitEleavator = visitElevator + 1
        global currentLocation
        currentLocation = "Elevator"
        player1.updateLocale()
        if visitElevator == 1:
                print("You've reentered the elevator")
                input("Press enter to continue")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                print("The elevator closes shut and locks behind you")
                input("Press enter to continue")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                print("Outside the door you hear something violently clawing at the door")
                input("Press enter to continue")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                print("The Buttons on the elevator are all unlit except for the open door button and the servicce button, Above you there is a hatch that allows maitnance to access the shaft")
                input("Press enter to continue...")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
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
                                sys.exit()
                                i=1
                        elif action == ("help"):
                                print("Command List: go up, press button, enter code, help, quit")

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
                                
                        elif action == ("quit"):
                                player1.quitGame()
                        else:
                                print("Invalid Command")
        else:
                print("You've reentered the elevator")
                input("Press enter to continue")
                
                print("Score: "+str(playerScore))
                print("The elevator closes shut and locks behind you")
                input("Press enter to continue")
                
                print("Score: "+str(playerScore))
                print("Outside the door you hear something violently clawing at the door")
                input("Press enter to continue")
                
                print("Score: "+str(playerScore))
                print("The Buttons on the elevator are all removed except for the open door button and the servicce button, Above you there is a hatch that allows maitnance to access the shaft")
                input("Press enter to continue...")
                
                print("Score: "+str(playerScore))
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
                                sys.exit()
                                i=1
                        elif action == ("help"):
                                print("Command List: go up, press button, help, quit, enter code, look")
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
                        
                        elif action == ("quit"):
                                player1.quitGame()
                        else:
                                print("Invalid Command")


#7
def trashCompactor():
        global playerName
        global currentLocation
        currentLocation = "Trash Compactor"
        player1.updateLocale()
        print("You fall into a dimmly lit room filled with trash.")
        print("You notice a silver door and a paper attached to it.")
        print("The paper says (Don't trust KAL, power must remain off!)")
        print("You open the door and you see a control panel. On the panel there is a button that say teleport")
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

                elif actionTrash == "help":
                        print("press button, look, map, inventory, help, quit, look")

                elif actionTrash == "quit":
                        player1.quitGame()

                elif actionTrash == "map":
                        map()
                elif actionTrash == "inventory":
                        inventory()
                        
                else:
                        print("Well you didn't press the button, hi I'm Kevin, the games developer aka xYukoNx.")
                        print("you typed: "+actionTrash+" which is not an option. Thats obvious. Which means you're an idiot.")
                        print("As punishment for your idiocy I'm sending you to a screen that is going to be your prison.")
                        while True is True:
                              print(playerName+" is an idiot!")
#6
def trashChute():
        global playerName
        global playerScore
        global turnNumber
        global currentLocation
        currentLocation = "Trash Chute"
        player1.updateLocale()
        x=0
        pointCount = 0
        print("You plummet down the shaft in darkness")
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
                sys.exit()
        else:
                pass
#40
def secretRoom():
        global currentLocation
        currentLocation = "Secret Room"
        player1.updateLocale()
        print("You've teleported into a dark room with no light")
        i=0
        while i == 0:
                print("What do you do?")
                action = input()
                if action == "flashlight" and "flashlight" in Inventory:
                        print("You turn on your flashlight and look around")
                        print("There is a teleporter and a safe")
                        while i==0:
                                print("what do you do?")
                                action2 = input()
                                if action2 == ("safe"):
                                        password = input("Please enter in the 4digit password: ")
                                        if password == ("5158"):
                                                print("The safe opens and contains an M16 Rifle and 6 fully loaded magazines")
                                                print("You take the gun and its ammo and put the ammo in your bag whilst swinging the gun around your shoulder using the strap.")
                                                Inventory.append("M16")
                                                Inventory.append("Ammo")
                                                player1.updateInv()
                                        else:
                                                print("That password is invalid")
                                elif action2 == ("teleporter"):
                                        print("You walk over to the teleporter and hit the button")
                                        Navigation[4][2]

                elif action == "look":
                        print("You've teleported into a dark room with no light")
                elif action == "quit":
                        player1.quitGame()

                elif action == "map":
                        map()
                elif action == "help":
                        print("flashlight, look, inventory, map, help, quit")

                elif action == "inventory":
                        openInventory()

                elif action == "go back" and "Developers Portal Gun" in player1.inventory:
                        Navigation[3][2]()
                else:
                        print("Having no sense of direction and no source of light you wander about until you die.")
                        player1.quitGame()
                        
                
        
        
#42
def jungleRoom():
        global currentLocation
        currentLocation = "Jungle Room"
        player1.updateLocale()
        print("You arrive in a room filled with jungle plants and trees.")
        print("In the ground you notice large animal tracks")
        print("To the side there is a large tree with a house built into it and a few other trees, it has thick vines hanging down from it.")
        print("The vines touch the ground.")
        print("What do you do?")
        action = input()
        if action == "follow tracks":
                print("You follow the tracks to a teleporter.")
                print("As you walk over to the teleporter you are ambushed by a giant ape.")
                print("what do you do?")
                action2 = input()
                if action2 == "shoot it" and "M16" in player1.inventory and "Ammo" in player1.inventory:
                        print(player1.Use("M16"))
                        print("You shoot the gorilla and kill it")
                        print("Upon cutting the gorilla open you find a taser")
                        print("You take the taser and go into the teleporter.")
                        Inventory.append("taser")
                        player1.updateInventory()
                        print("You press the button and teleport back to the lobby")
                elif action2 == "help":
                        print("Command List: shoot it, stand still, help, quit")
                elif action2 == "quit":
                        player1.quitGame()
        elif action == "quit":
                player1.quitGame()
        elif action == "climb vines":
                print("You start climbing up the vines towards the tree house.")
                Navigation[5][2]()
        elif action == "help":
                print("Commands: follow tracks, climb vines, quit, help.")
        elif action == "teleport" and "Developers Portal Gun" in player1.inventory:
                player1.teleport()
                
                
                
                
def treeHouse():
        
        global currentLocation
        currentLocation = "Tree House"
        player1.updateLocale()
        print(TREE_HOUSE.LocaleDescription)
        
                      
#This is the Elevator Room aka the Starting area and main hub
#0
def elevatorRoom():
        global player1
        global playerName
        global playerScore
        global turnNumber
        global currentLocation
        currentLocation = "Elevator Room"
        player1.updateLocale()
        x=0
        while x == 0:
            print(ELEVATOR_ROOM.LocaleDescription)
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
            elif purpose == ("get map") and "map" not in Inventory:
                    print("You walk over to the map and take it ofthe wall to put it in your bag.")
                    Inventory.append("map")
                    player1.updateInv()
            elif purpose == ("map"):
                    Map()

            elif purpose == ("inventory"):
                    openInventory()

            elif purpose == ("08558"):
                    print("Hello YukoN! Here is your portal gun!")
                    Inventory.append("Developers Portal Gun")
                    player1.updateInv()

            elif purpose == ("teleport"):
                    player1.teleport()
        

            elif purpose == ("go right"):
                if key == 0:
                    print("The door is locked")
                    input("Press enter to continue...")
                    
                else:
                    Navigation[1][2]()

            elif purpose == ("quit"):
                    player1.quitGame()
            elif purpose == "look":
                     print("A barely lit room with doors to your left, right, and directly in front of you."
                           "There is a trash chute by the elevator. The elevator stays open behind you. There is a map next to the elevator.")

            elif purpose == ("go back"):
                    Navigation[2][1]()
                    
            elif purpose == ("help"):
                    print("Command List: go back, go foraward, go left, go right, quit, help, get map, inventory, map, look")
                        
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
                    ,[secretRoom, None, jungleRoom]
                    ,[None, None, treeHouse]]
#elevatorRoom = 11. eggRoom = 10. escapePods = 12. mainFrame = 01. elevatoR = 21. trashChute = 22. ventiLation = 31. trashCompactor = 32. secretRoom = 40. jungleRoom = 42.
#treeHouse = 52

#This function displays the map to the players                
def Map():
        if "map" in player1.inventory:
                print("You are currently in: "+player1.currLocale)
                print(Navigation)
        else:
                print("You dont have a map!")
#This displays the players inventory to the player.
def openInventory():
        print(Inventory)
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
