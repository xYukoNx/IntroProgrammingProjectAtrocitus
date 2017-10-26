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
                turnNumber=turnNumber+1
                print("Hello "+playerName+"! The emergency power is starting to fail! Im using the last of my power to send you to the main room, please get to the mainframe from there and turn the power back on. Initiating sleep mode....")
                input("Press enter to continue")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                print("The Elevator has stopped and the door has opened.")
                input("Press enter to continue")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))

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
                                        print(playerName+"'s Final Score: "+str(playerScore))
                                        input("Press enter to end game")
                                        sys.exit()

                                    elif actionTwo == ("quit"):
                                            print(playerName+"'s Final Score: "+playerScore)
                                            print("Thank you for playing Atrocitus "+playerName+"!")
                                            print("Goodbye!")
                                            print("THE END!")
                                            input("Press enter to end game...")
                                            sys.exit()

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
                                            print(playerName+"'s Final Score: "+playerScore)
                                            print("Thank you for playing Atrocitus "+playerName+"!")
                                            print("Goodbye!")
                                            print("THE END!")
                                            input("Press enter to end game...")
                                            sys.exit()

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
                                print(playerName+"'s Final Score: "+str(playerScore))
                                input("Press enter to end game...")
                                sys.exit()
                                
                        elif answerTwo == ("quit"):
                                    print(playerName+"'s Final Score: "+playerScore)
                                    print("Thank you for playing Atrocitus "+playerName+"!")
                                    print("Goodbye!")
                                    print("THE END!")
                                    input("Press enter to end game...")
                                    sys.exit()
                                    
                        elif answerTwo == ("no") or answerTwo == ("NO"):
                                print("You leave the Escape Pod room through the door that you entered.")
                                h=1

                        else:
                                print("Invalid Command")
        else:
                print("You open the door with the key you found in the egg shell room and go inside")
                input("Press enter to continue...")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                print(" ")
                print("You walk into an escape pod room that isfully operational, the coordinates are set for a random point in the milky way galaxy.")
                input("Press enter to continue...")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
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
                                    print(playerName+"'s Final Score: "+playerScore)
                                    print("Thank you for playing Atrocitus "+playerName+"!")
                                    print("Goodbye!")
                                    print("THE END!")
                                    input("Press enter to end game...")
                                    sys.exit()
                                    
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
        if visitEggS != 1:
        
                i=0        
                print("you enter the room to your left and step in.")
                input("Press enter to continue...")
                
                print("Score: "+str(playerScore))
                print("The room is filled with what would appear to be cracked egg shells")
                input("Press enter to continue...")
                
                print("Score: "+str(playerScore))
                print("There are no doors, as you walk bout the room you feel slime dripping from the veiling onto your head.")
                input("Press enter to continue...")
                
                print("Score: "+str(playerScore))
                while i == 0:
                        print("What do you do?")
                        actionOne = input()
                                
                        if actionOne == ("nothing") or actionOne == ("stand still"):
                                print("The goop stops dripping and you find a key on the floor and pick it up.")
                                key = 1
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
                            print(playerName+"'s Final Score: "+playerScore)
                            print("Thank you for playing Atrocitus "+playerName+"!")
                            print("Goodbye!")
                            print("THE END!")
                            input("Press enter to end game...")
                            sys.exit()

                        else:
                                        print("Invalid Command")

        else:
                i=0
                        
                print("you enter the room to your left and step in.")
                input("Press enter to continue...")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                print("The room is filled with what would appear to be cracked egg shells")
                input("Press enter to continue...")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                print("There are no doors, as you walk bout the room you feel slime dripping from the veiling onto your head.")
                input("Press enter to continue...")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                while i == 0:
                        print("What do you do?")
                        actionOne = input()
                                
                        if actionOne == ("nothing") or actionOne == ("stand still"):
                                print("The goop stops dripping and you find a key on the floor and pick it up.")
                                key = 1
                                input("Press enter to continue...")
                                playerScore=playerScore+10
                                print("Score: "+str(playerScore))
                                print("You go back through the door that came in")
                                i=1
                                      
                        elif actionOne == ("look up"):
                                print("A hideous creature with razer sharp claws pounces down on you and slashes off your limbs and eats your stomache as you lay alive and horrified, it leaves you and you die an extremely long and painful death.")
                                input("Press enter to continue...")
                                playerScore=playerScore+10
                                print("Score: "+str(playerScore))
                                print("The End!")
                                print(playerName+"'s Final Score: "+str(playerScore))
                                input("Press enter to end game...")
                                sys.exit()

                        elif purpose == ("quit"):
                            print(playerName+"'s Final Score: "+playerScore)
                            print("Thank you for playing Atrocitus "+playerName+"!")
                            print("Goodbye!")
                            print("THE END!")
                            input("Press enter to end game...")
                            sys.exit()

                        else:
                                        print("Invalid Command")

#5
def ventiLation():
        global visitVentilation
        global playerName
        global playerScore
        global turnNumber
        visitVentilation = visitVentilation+1
        
        if visitVentilation == 1:
                print("You find a note that has the following sequence of chemicals and spaces written on it:")
                input("Press enter to continue")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                print("Potassium, Aluminium, , Iodine, Sulfur, , Barium, Darmstadtium")
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
                                print(playerName+"'s Final Score: "+playerScore)
                                print("Thank you for playing Atrocitus "+playerName+"!")
                                print("Goodbye!")
                                print("THE END!")
                                input("Press enter to end game...")
                                sys.exit()
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
                                print("Command List: stay, go lobby, help, quit")
                        elif action == ("quit"):
                                print(playerName+"'s Final Score: "+playerScore)
                                print("Thank you for playing Atrocitus "+playerName+"!")
                                print("Goodbye!")
                                print("THE END!")
                                input("Press enter to end game...")
                                sys.exit()
                        else:
                                print("Invalid Command")

#4
def elevatoR():
        
        global visitElevator
        global playerName
        global playerScore
        global turnNumber
        visitEleavator = visitElevator + 1
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
                print("The Buttons on the elevator are all removed except for the open door button and the servicce button, Above you there is a hatch that allows maitnance to access the shaft")
                input("Press enter to continue...")
                playerScore=playerScore+10
                print("Score: "+str(playerScore))
                i=0
                while i==0:
                        print("What do you do?")
                        action = input()
                        if action == ("go up"):
                                print("You climb up through the hatch and into the maitnance shaft, from there you see a ventilation shaft and go inside")
                                Locations[5]()
                        elif action == ("press button"):
                                print("The doors open and you're immeadiately set upon by a vicious Alien, it digs its claws through your eyes, puncturing your brain and killing you")
                                print("THE END")
                                sys.exit()
                                i=1
                        elif action == ("help"):
                                print("Command List: go up, press button, help, quit")
                        elif action == ("quit"):
                                print(playerName+"'s Final Score: "+playerScore)
                                print("Thank you for playing Atrocitus "+playerName+"!")
                                print("Goodbye!")
                                print("THE END!")
                                input("Press enter to end game...")
                                sys.exit()
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
                                Locations[5]()
                        elif action == ("press button"):
                                print("The doors open and you're immeadiately set upon by a vicious Alien, it digs its claws through your eyes, puncturing your brain and killing you")
                                print("THE END")
                                sys.exit()
                                i=1
                        elif action == ("help"):
                                print("Command List: go up, press button, help, quit")
                        elif action == ("quit"):
                                print(playerName+"'s Final Score: "+playerScore)
                                print("Thank you for playing Atrocitus "+playerName+"!")
                                print("Goodbye!")
                                print("THE END!")
                                input("Press enter to end game...")
                                sys.exit()
                        else:
                                print("Invalid Command")


#7
def trashCompactor():
        global playerName
        print("You fall into a dimmly lit room filled with trash.")
        print("You notice a silver door and a paper attached to it.")
        print("The paper says (Don't trust KAL, power must remain off!)")
        print("You open the door and you see a control panel. On the panel there is a button that say teleport")
        actionTrash = input("What do you do?")
        if actionTrash == "press button":
                print("A large grass tube falls over you and ametal rod hangs over you")
                print("TELEPORTING TO RANDOM LOCATION")
<<<<<<< HEAD
                Locations[random.randrange(0,7)]()
=======
                Location[random.randrange(0,7)]()
>>>>>>> 41fce3a88fa66b3963a499a47c98f0697cba8643
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
                        sys.exit()
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
                        sys.exit()
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
                        sys.exit()
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
                        sys.exit()
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
                        sys.exit()
                else:
                        print("invalid command try again")
        if pointCount >= 4:
<<<<<<< HEAD
                Locations[7]()
=======
                Location[7]()
>>>>>>> 41fce3a88fa66b3963a499a47c98f0697cba8643
        elif pointCount < 4:
                print("You hit a sharp part of the chute and get impaled upon it, you bleed out and die.")
                print("THE END!")
                sys.exit()
        else:
                pass
                      
#This is the Elevator Room aka the Starting area and main hub
#0
def elevatorRoom():
        global playerName
        global playerScore
        global turnNumber
        x=0
        while x == 0:
            print("You step out into a barely lit room with doors to your left, right, and directly in front of you. There is a trash chute by the elevator. The elevator stays open behind you.")
            input("Press enter to continue...")
            print("what do you do?")
            purpose = input()
            turnNumber=turnNumber+1
            
            if purpose == ("go left"):
               Locations[1]()
            
            elif purpose == ("go forward"):
                if key == 0:
                    print("The door is locked")
                    input("Press enter to continue...")
                else:
                        Locations[3]()
<<<<<<< HEAD
            elif purpose == ("go trash chute"):
                    print("You walk over to the trash chute and look down it, suddenly you slip and fall in the trash chute.")
                    Locations[6]()
=======
>>>>>>> 41fce3a88fa66b3963a499a47c98f0697cba8643
        

            elif purpose == ("go right"):
                if key == 0:
                    print("The door is locked")
                    input("Press enter to continue...")
                    
                else:
                    Locations[2]()

            elif purpose == ("quit"):
                    print(playerName+"'s Final Score: "+playerScore)
                    print("Thank you for playing Atrocitus "+nameFirst+"!")
                    print("Goodbye!")
                    print("THE END")
                    input("Press enter to end game...")
                    sys.exit()

            elif purpose == ("go back"):
                    Locations[4]()
                    
            elif purpose == ("help"):
                    print("Command List: go back, go foraward, go left, go right, quit, help")
                        
            else:
                print("Invalid Command")
                
#This is my list of the areas        
Locations = [elevatorRoom, eggRoom, escapePods, mainFrame, elevatoR, ventiLation, trashChute, trashCompactor]
        
#This is the main function that runs the other functions                          
def main():
        global playerName
        global playerScore
        global key
        global Locations
        c=0
        z=0
        
        
        
        inTritle()
        
        Locations[0]()
        

         
       
main()


