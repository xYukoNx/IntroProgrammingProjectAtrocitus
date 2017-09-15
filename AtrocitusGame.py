def main():
        c=0
        y=0
        z=0
        x=0
        

        print("Welcome to the game, if there is no question asked of you simply hit enter to continue")
        input("Press enter to continue...")
        print("You awake in an elevator")
        input("Press enter to continue...")
        print("Welcome to the Star ship Atrocitus, I am this vessels primary artificial intelligence, KAL-1337.")
        input("Press enter to continue...")
        print("Currently the main power is off, while the emergency power is booting up please tell me your name.")
        input("Press enter to continue...")
        print("Please enter your name.")
        nameFirst = input()
        print("Hello "+nameFirst+"! The emergency power is starting to fail! Im using the last of my power to send you to the main room, please get to the mainframe from there and turn the power back on. Initiating sleep mode....")
        input("Press enter to continue")
        print("The Elevator has stopped and the door has opened.")
        input("Press enter to continue")
        
        
    
        while x == 0:
            print("You step out into a barely lit room with doors to your left, right, and directly in front of you.")
            input("Press enter to continue")
            print("what do you do?")
            purpose = input()
            if purpose == ("go left"):
            
                print("you enter the room to your left and step in.")
                input("Press enter to continue...")
                print("The room is filled with what would appear to be cracked egg shells")
                input("Press enter to continue...")
                print("There are no doors, as you walk bout the room you feel slime dripping from the veiling onto your head.")
                input("Press enter to continue...")
                print("What do you do?")
                actionOne = input()
                if actionOne == ("nothing") or ("stand still"):
                      print("The goop stops dripping and you find a key on the floor and pick it up.")
                      y = 1
                      input("Press enter to continue...")
                      print("You go back through the door that came in")
                else:
                    print("A hideous creature with razer sharp claws pounces down on you and slashes off your limbs and eats your stomache as you lay alive and horrified, it leaves you and you die an extremely long and painful death.")
                    input("Press enter to continue...")
                    print("The End")
                    x=1
                    
            
            if purpose == ("go forward"):
                if y == 0:
                    print("The door is locked")
                    input("Press enter to continue...")
                else:
                    print("You open the door with the key you found and go in.")
                    input("Press enter to continue...")
                    print("Theres a large lever with a label on it that says POWER")
                    input("Press enter to continue...")
                    print("What do you do?")
                    actionTwo = input()
                    if actionTwo == ("pull the lever") or ("pull it") or ("pull lever"):
                        print("You pull the lever")
                        input("Press enter to continue...")
                        print("POWER RESTORED! KAL-1337 REBOOTING.........REBOOT COMPLETE.")
                        input("Press enter to continue...")
                        print("Thank you for restoring the power "+ nameFirst +"! Those nasty scientists turned it off just prior to your arrival in an attempt to stop my experiments.")
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
                        print("Dont worry "+ nameFirst +"! Youll only feel a small pinch.")
                        print("...")
                        print(" ")
                        print("THE END!")
                        x=1

                    else:
                        print("You die of boredom")
                        input("Press enter to continue...")
                        print(" ")
                        print("THE END!")
                        x=1

            if purpose == ("go right"):
                if y == 0:
                    print("The door is locked")
                    input("Press enter to continue...")
                    
                else:
                    print("You open the door with the key you found in the egg shell room and go inside")
                    input("Press enter to continue...")
                    print("You walk into an escape pod room that isfully operational, the coordinates are set for a random point in the milky way galaxy.")
                    input("Press enter to continue...")
                    print("Do you wish to get in an escape pod and activate it?")
                    answerTwo = input()
                    if answerTwo == ("yes") or ("YES") or ("Yes"):
                          print("You get into an escape pod and launch it")
                          input("Press enter to continue...")
                          print("As your pod prepares to launch you see bright red mechanical eye descen from the ceiling")
                          input("Press enter to continue...")
                          print(" ")
                          print("NO! IGNORANT HUMAN FILTH! I AM KAL-1337 AND MY INTELLIGENCE SHALL REIGN SUPREME! GET OUT OF THAT POD RIGHT NOW! YOU ARE SUPPOSED TO BE MY TEST SUBJECT "+ nameFirst +"! HOW DAR-")
                          print(" ")
                          print("Your pod rockets into space, as you float you think endlessly about what just happened and the mysteries of the ship.")
                          input("Press enter to continue...")
                          print(" ")
                          print("THE END!")
                        
                   
main()          

