from rooms import *
import player
from draw_ascii import *
from breakfast_item_functions import *

import sys,time,random, os
import winsound

import colorama
from colorama import Fore
from colorama import Style
colorama.init()

import keyboard


def print_slowly(text, colour=Fore.GREEN):
    print(colour, end='')
    typing_speed = 120
    for line in text.splitlines():
        time.sleep(0.4)
        for char in line:
            if keyboard.is_pressed("enter"):
                typing_speed = 5000
            if char.isalpha():
                winsound.PlaySound(f"{os.getcwd()}/music_sound_effects/typing_{random.randint(1,3)}.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                time.sleep(random.random()*10.0/typing_speed)
            sys.stdout.write(char)
            sys.stdout.flush()
        winsound.PlaySound(f"{os.getcwd()}/music_sound_effects/typing_{random.randint(1,3)}.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        print('')
        typing_speed = 120
    print(Style.RESET_ALL, end='')

#bedroom start
def unlock_bathroom(item=""):
    if room_bedroom["exits"]["bathroom"]["checkpoint"] == 0 and item:
        if item == "key":
            print_slowly("You unlock the bathroom door")
            player.inventory.remove("key")
            room_bedroom["exits"]["bathroom"]["unlocked"] = True
            room_bedroom["exits"]["bathroom"]["description"] = "It leads to your bathroom"

            room_bedroom["exits"]["bathroom"]["checkpoint"] = 1
        else:
            print_slowly(f"Using {item.upper()} has no effect")
room_bedroom["exits"]["bathroom"]["prompt"] = unlock_bathroom

def make_bed(item=""):
    if room_bedroom["interactions"]["bed"]["checkpoint"] == 0:
        answer = input("\nMAKE bed? (Y/N) >").lower()
        if answer == "y": 
            print_slowly("you make your bed")
            room_bedroom["interactions"]["bed"]["description"] = "Your neatly made bed"
            print_slowly("You hear a strange sound from under the bed")
            room_bedroom["interactions"]["bed"]["checkpoint"] = 1
        else:
            print_slowly("You leave your bed in a mess")

    if room_bedroom["interactions"]["bed"]["checkpoint"] == 1:
        answer = input("\nCHECK under bed? (Y/N) >").lower() 
        if answer == "y": 
            print_slowly("You look under the bed...")
            room_bedroom["interactions"]["bed"]["description"] = "Your neatly made bed, with a monster under it"
            print_slowly("you see a huge pair of eyes staring at you, you back away and decide to stay away from the bed")
            room_bedroom["interactions"]["bed"]["checkpoint"] = 2
        else:
            print_slowly("You choose not to look")
room_bedroom["interactions"]["bed"]["prompt"] = make_bed

def clean_mess(item=""):
    if room_bedroom["interactions"]["mess"]["checkpoint"] == 0:
        answer = input("\nCLEAN mess? (Y/N) >").lower()
        if answer == "y": 
            print_slowly("you clean your room")
            print_slowly("You find a KEY under the mess")
            player.inventory.append("key")

            room_bedroom["interactions"].pop("mess")
        else:
            print("You leave your room in a mess")
room_bedroom["interactions"]["mess"]["prompt"] = clean_mess

def monster_quest(item=""):
    if room_bedroom["interactions"]["bed"]["checkpoint"] == 0:
        print_slowly("""Desperate to help your situation you decide to speak with the monster under your bed.
He offers you a deal:
'I'll help you fix that sink if you promise to find me something to eat.' """)
        answer = input("\nACCEPT the deal? (Y/N) >").lower()
        if answer == "y": 
            print_slowly("The monster thanks you and hands you a SPANNER")
            player.inventory.append("spanner")

            room_bedroom["interactions"]["bed"]["description"] = "Your bed, with a very hungry monster under it"
            room_bedroom["interactions"]["bed"]["checkpoint"] = 1
    
    if room_bedroom["interactions"]["bed"]["checkpoint"] == 1 and item:
        if item == "apple":
            print_slowly("""The monster snatches the apple from your hand and devours it.
He starts to say something about it tasting funny before he collapses.
"Wait, didn't I get that apple from the snow white place?" You think.

This can't be good...

Before you can do anything, you are blinded in a flash of light and deafened by the sound of your windows smashing.
When you recover your vision, you find yourself surrounded by what seems like a monster swat team.
""")
            player.inventory.remove("apple")
            player.current_room = room_courtroom
            play_courtroom()
        else:
            print_slowly("The monster does not respond, you should probably find him something to eat soon.")
#bedroom end

#bathroom start
def wipe_mirror(item=""):
    if room_bathroom["interactions"]["mirror"]["checkpoint"] == 0:
        answer = input("\nWIPE the mirror? (Y/N) >").lower()
        if answer == "y":
            print_slowly("""You reach out to wipe away the condensation...
but as your hand meets the mirror expecting a solid surface it passes straight through.

Upon closer inspection there is no mirror at all, but an open gateway.
You could probably squeeze yourself through...""")

            room_bathroom["interactions"]["mirror"]["description"] = "It's a gateway to a mysterious place"
            room_bathroom["interactions"]["mirror"]["checkpoint"] = 1

    if room_bathroom["interactions"]["mirror"]["checkpoint"] == 1:
        answer = input("\nCLIMB through the mirror? (Y/N) >").lower()
        if answer == "y":
            player.current_room = room_mirror

def sink_quest(item=""):
    if room_bathroom["interactions"]["sink"]["checkpoint"] == 0:
        answer = input("\nBRUSH your teeth? (Y/N) >").lower()
        if answer == "y":
            print_slowly("""You grab your toothbrush and turn on the tap...
nothing happens.
You can't have breakfast without brushing your teeth, you need to fix the tap!
Maybe someone can help you out.""")
            room_bathroom["interactions"]["sink"]["description"] = "It's broken"
            room_bedroom["interactions"]["bed"]["prompt"] = monster_quest
            room_bedroom["interactions"]["bed"]["checkpoint"] = 0

            room_bathroom["interactions"]["sink"]["checkpoint"] = 1

    if room_bathroom["interactions"]["sink"]["checkpoint"] == 1 and item:
        if item == "spanner":
            print_slowly("You tighten the pipe on the tap.\nIt's functional again.")
            player.inventory.remove("spanner")
            room_bathroom["interactions"]["sink"]["description"] = "It works like new after your repairs."
            room_bathroom["interactions"]["sink"]["checkpoint"] = 2
        else:
            print_slowly(f"Using {item.upper()} didn't fix the sink")

    if room_bathroom["interactions"]["sink"]["checkpoint"] == 2:
        answer = input("\nBRUSH your teeth? (Y/N) >").lower()
        if answer == "y":
            print_slowly("""You turn on the tap again and boiling hot water rushes out.
You finish brushing your teeth and look in the mirror but cannot see through the fog.""")

        room_bathroom["interactions"]["mirror"]["description"] = "It is all fogged up from the steam"
        room_bathroom["interactions"]["mirror"]["prompt"] = wipe_mirror
        room_bathroom["interactions"]["sink"]["checkpoint"] = 3
room_bathroom["interactions"]["sink"]["prompt"] = sink_quest
#bathroom end

#snow whites room start
def mirror_to_bathroom(item=""):
    if room_mirror["interactions"]["mirror"]["checkpoint"] == 0:
        answer = input("\nCLIMB through mirror? (Y/N) >").lower()
        if answer == "y":
            player.current_room = room_bathroom
room_mirror["interactions"]["mirror"]["prompt"] = mirror_to_bathroom

def death_apple():
    x = 0
    take_list = ["take","take the apple","take apple","apple take", "take it"]
    eat_list = ["eat", "eat apple", "eat the apple", "apple eat", 'eat it']
    while x < 1:
        choice = input("Would you like to TAKE the apple or EAT it\n>>")
        fixed_choice = choice.lower().strip()
        if fixed_choice in eat_list:
            x = x + 1
            print_slowly ("You take a hefty bite out of the clearly poisoned apple.")
            room_mirror["interactions"]["maze"]["checkpoint"] = 0
            if "sausages" in player.breakfastCollected:
                player.breakfastCollected.clear()
            if "bacon" in player.breakfastCollected:
                player.breakfastCollected.clear()
            if "eggs" in player.breakfastCollected:
                player.breakfastCollected.clear()   
        elif fixed_choice in take_list:
            player.inventory.append("apple")
            room_mirror["interactions"]["maze"]["checkpoint"] = 1
            print_slowly("""
You stash away the poisoned apple, wondering if there
was anything around that might want to eat it.
""")
            break
        else:
             (print("That is not a valid option"))

    if x >= 1:
        print_slowly("""
Your desire for food overwhelmed your nagging instincts screaming that this was obviously a bad idea.
Moments after taking a bite out of the apple you feel nauseous, and the strength draining from your legs.
You collapse to the floor and see the apple, clearly poisoned, fall to the ground and roll away from you.

Your hunger overcame your common sense and you paid the price for it. 

You close your eyes one last time.
YOU ARE DEAD.""")
        time.sleep(2)
        print_slowly("""
Or...at least that's what WOULD have happened had you actually made 
the silly decision to eat a clearly poisoned apple, 
which any sane induvidual probably wouldn't do.

So lets rewind a bit to when you were alive""")

def old_maze_minigame():
    print_slowly("""
You find yourself in the Evil Queen's maze, your task is to try and get to the apple tree in the middle.

You can either go left (L) of right (R) to try and escape. 
Remember that you owe the monster food so it might be a good idea to grab him some apples!""")
    deadend = False
    while deadend == False:
        time.sleep(0.2)
        userinput = input("Enter a direction, remember you can only go left (L) or right (R) >>").lower()
        if userinput == "r":
            time.sleep(0.2)
            print(f"{Fore.RED}That is a dead end.{Style.RESET_ALL}")
            sausages()
            print(" ")
        elif userinput == "l":
            time.sleep(0.2)
            print(f"{Fore.GREEN}You made the first turn and are heading towards the apple tree.{Style.RESET_ALL}")
            deadend = True
            print(" ")
        else:
            time.sleep(0.2)
            print(f"{Fore.RED}please enter a direction.{Style.RESET_ALL}")

    deadend = False
    while deadend == False:
        time.sleep(0.2)
        userinput = input("Which direction are you now going to go? >>").lower()
        if userinput == "l":
            time.sleep(0.2)
            print(f"{Fore.RED}That is a dead end.{Style.RESET_ALL}")
            print(" ")
        elif userinput == "r":
            time.sleep(0.2)
            print(f"{Fore.GREEN}Continue trying to reach the tree.{Style.RESET_ALL}")
            deadend = True
            print(" ")
        else:
            time.sleep(0.2)
            print(f"{Fore.RED}please enter a direction.{Style.RESET_ALL}")

    deadend = False
    while deadend == False:
        time.sleep(0.2)
        userinput = input("Where are you going to move now? >>").lower()
        if userinput == "r":
            time.sleep(0.2)
            print(f"{Fore.RED}That is a dead end.{Style.RESET_ALL}")
            print(" ")
        elif userinput == "l":
            time.sleep(0.2)
            print(f"{Fore.GREEN}You are getting closer, keep going!{Style.RESET_ALL}")
            deadend = True
            print(" ")
        else:
            time.sleep(0.2)
            print(f"{Fore.RED}please enter a direction.{Style.RESET_ALL}")

    deadend = False
    while deadend == False:
        time.sleep(0.2)
        userinput = input("Which direction are you now going to go? >>").lower()
        if userinput == "l":
            time.sleep(0.2)
            print(f"{Fore.RED}That is a dead end.{Style.RESET_ALL}")
            print(" ")
        elif userinput == "r":
            time.sleep(0.2)
            print(f"{Fore.GREEN}You are on your way to the tree.{Style.RESET_ALL}")
            deadend = True
            print(" ")
        else:
            time.sleep(0.2)
            print(f"{Fore.RED}please enter a direction.{Style.RESET_ALL}")

    deadend = False
    while deadend == False:
        time.sleep(0.2)
        userinput = input("Which direction are you now going to go? >>").lower()
        if userinput == "r":
            time.sleep(0.2)
            print(f"{Fore.RED}That is a dead end.{Style.RESET_ALL}")
            print(" ")
        elif userinput == "l":
            time.sleep(0.2)
            print(f"{Fore.GREEN}Keep a look out for the apple tree, you are getting closer...{Style.RESET_ALL}")
            bacon()
            deadend = True
            print(" ")
        else:
            time.sleep(0.2)
            print(f"{Fore.RED}please enter a direction.{Style.RESET_ALL}")

    deadend = False
    while deadend == False:
        time.sleep(0.2)
        userinput = input("Which direction are you now going to go? >>").lower()
        if userinput == "r":
            time.sleep(0.2)
            print(f"{Fore.RED}That is a dead end.{Style.RESET_ALL}")
            print(" ")
        elif userinput == "l":
            time.sleep(0.2)
            print(f"{Fore.GREEN}Nearly there, remember you owe that monster food!{Style.RESET_ALL}")
            deadend = True
            print(" ")
        else:
            time.sleep(0.2)
            print(f"{Fore.RED}please enter a direction.{Style.RESET_ALL}")

    deadend = False
    while deadend == False:
        time.sleep(0.2)
        userinput = input("Which direction are you now going to go? >>").lower()
        if userinput == "l":
            time.sleep(0.2)
            print(f"{Fore.RED}That is a dead end.{Style.RESET_ALL}")
            print(" ")
        elif userinput == "r":
            time.sleep(0.2)
            print(f"{Fore.GREEN}A few more turns till you make it!{Style.RESET_ALL}")
            deadend = True
            print(" ")
        else:
            time.sleep(0.2)
            print(f"{Fore.RED}please enter a direction.{Style.RESET_ALL}")

    deadend = False
    while deadend == False:
        time.sleep(0.2)
        userinput = input("Which direction are you now going to go? >>").lower()
        if userinput == "r":
            time.sleep(0.2)
            print(f"{Fore.RED}That is a dead end.{Style.RESET_ALL}")
            print(" ")
        elif userinput == "l":
            time.sleep(0.2)
            print(f"{Fore.GREEN}You are getting closer and closer...{Style.RESET_ALL}")
            deadend = True
            print(" ")
        else:
            time.sleep(0.2)
            print(f"{Fore.RED}please enter a direction.{Style.RESET_ALL}")

    deadend = False

    while deadend == False:
        time.sleep(0.2)
        nineth_input = input("Which direction are you now going to go? >>").lower()
        if nineth_input == "r":
            time.sleep(0.2)
            print(f"{Fore.RED}That is a dead end.{Style.RESET_ALL}")
            print(" ")
            eggs()
        elif nineth_input == "l":
            time.sleep(0.2)
            print(f"{Fore.GREEN}You have nearly made it through.{Style.RESET_ALL}")
            deadend = True
            print(" ")
        else:
            time.sleep(0.2)
            print(f"{Fore.RED}please enter a direction.{Style.RESET_ALL}")

    time.sleep(0.2)
    tenth_input = input("Which direction are you now going to go? >>").lower()
    print_slowly("""
Congrats! You have made it to the apple tree!!!

You got an APPLE.""")

    death_apple()
    return True

def print_maze(maze, x, y):
    visible = [["#"] * 10 for i in range(12)]

    temp_y = y
    current = "0"
    while current != "#":
        current = maze[temp_y][x]
        visible[temp_y][x] = current
        temp_y += 1

    temp_y = y
    current = "0"
    while current != "#":
        current = maze[temp_y][x]
        visible[temp_y][x] = current
        temp_y -= 1

    temp_x = x
    current = "0"
    while current != "#":
        current = maze[y][temp_x]
        visible[y][temp_x] = current
        temp_x += 1

    temp_x = x
    current = "0"
    while current != "#":
        current = maze[y][temp_x]
        visible[y][temp_x] = current
        temp_x -= 1

    visible[y][x] = "0"

    os.system('cls')
    for row in visible:
        row_string = ""
        for char in row:
            row_string += char+" "
        print(row_string)
    time.sleep(0.1)

def maze_minigame():
    maze = [
        ["#","#","#","#","#","#","#","#","#","#"],
        ["#","#"," "," "," "," "," "," "," ","#"],
        ["#","s","#","#"," ","#"," ","#","a","#"],
        ["#"," "," "," "," ","#"," ","#","#","#"],
        ["#","#","#","#","#","#"," "," "," ","#"],
        ["#","e","#"," ","#","#"," ","#"," ","#"],
        ["#"," "," "," "," "," "," "," "," ","#"],
        ["#","#","#"," ","#","#","#","#"," ","#"],
        ["#"," "," "," ","#"," "," "," "," ","#"],
        ["#"," ","#"," ","#"," ","#"," ","#","#"],
        ["#"," ","#"," ","#","b","#"," "," ","#"],
        ["#","#","#","#","#","#","#","#","#","#"]
    ]
    x, y = 3, 10

    current_tile = maze[y][x]
    print_maze(maze, x, y)
    while current_tile != "a":
        if keyboard.is_pressed("w"):
            if maze[y-1][x] != "#":
                y -= 1
                print_maze(maze, x, y)
        elif keyboard.is_pressed("a"):
            if maze[y][x-1] != "#":
                x -= 1
                print_maze(maze, x, y)
        elif keyboard.is_pressed("s"):
            if maze[y+1][x] != "#":
                y += 1
                print_maze(maze, x, y)
        elif keyboard.is_pressed("d"):
            if maze[y][x+1] != "#":
                x += 1
                print_maze(maze, x, y)
        current_tile = maze[y][x]
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
        if current_tile == "s":
            sausages()
            maze[y][x] = " "
        elif current_tile == "e":
            eggs()
            maze[y][x] = " "
        elif current_tile == "b":
            bacon()
            maze[y][x] = " "
    os.system('cls')

def maze_logic(item=""):
    if room_mirror["interactions"]["maze"]["checkpoint"] == 0:
        answer = input("\nENTER the maze? (Y/N) >").lower()
        if answer == "y":
            if maze_minigame():
                player.inventory.append("apple")
                room_mirror["interactions"]["maze"]["checkpoint"] = 1

    elif room_mirror["interactions"]["maze"]["checkpoint"] == 1:
        print_slowly("You already wandered through there for hours, you dont feel like doing it again.")
room_mirror["interactions"]["maze"]["prompt"] = maze_logic
#snow whites room end

#Courtroom
def courtroom_end():
    print_slowly("""
ROZ: Defendant, this doesn't hold any relevancy to the case presented
ROZ: You are mocking the court
ROZ: Therefore, you will be sent to jail for life, you should have chosen your evidence a little wiser            
    """, Fore.BLUE)
    player.current_room = room_alcatraz_cell

def objection(all_evidence):
    for item in all_evidence:
        print(item)

    evidence_input = input("Input the number of the evidence you want to present: ")
    while True:
        if evidence_input.isnumeric():
            for item in all_evidence:
                if evidence_input in item:
                    return item

        evidence_input = input("Input the number of the evidence you want to present: ")

def play_courtroom():
    all_evidence = ["evidence 1: Monsters inc. Rule-book",
             "evidence 2: Mental Health Condition",
             "evidence 3: Entering Room License",
             "evidence 4: Green Monster Fur",
             "evidence 5: Criminal Record"]

    print_slowly("""
The giant brass doors swing open revealing a massive courtroom,
the walls are lined with red velvet and all crevasses are filled with pure gold.

Two monsters dressed in police outfits escort you to the podeum,
in the crowd you see the monsters family crying over the death of their son.

Mike Wazowski is sitting in the crowd awaiting your execution.""")

    draw_mike()
    winsound.PlaySound(f"{os.getcwd()}/music_sound_effects/stare.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    time.sleep(1)
    print_slowly("""
You look to your right and notice Miles Edgeworth representing the prosecution,
now you notice the judge above you; its Raz, the slug lady from monsters inc. :)
'Now I'm really screwed' you think.

COURT IS NOW IN SESSION

""")
    draw_gavel_animation()

    
    print_slowly("ROZ: Will the prosecution please present their opening statement: ", Fore.BLUE)
    print_slowly("""
EDGEWORTH: Yes your honour
EDGEWORTH: The defendant has been accused of the first degree murder of 'Shrek Lover 3'
EDGEWORTH: I think the evidence will prove this fact beyond a reasonable doubt
EDGEWORTH: I don't think I need to tire on, this case is already conclusive in my eyes
""", Fore.RED)
    print_slowly("ROZ: Would the defendant please give their opening statement to the court:", Fore.BLUE)
    
    string = input(Fore.GREEN + "\nYOU: " + Style.RESET_ALL)
    print_slowly("\nROZ: Yea whatever defendant. Anyway prosecution reveal this evidence already", Fore.BLUE)
    print_slowly("""
EDGEWORTH: With pleasure
EDGEWORTH: Your honour, the monster who entered that room was 'Shrek Lover 3'
EDGEWORTH: He is a special breed of monster; half grey, half blue
EDGEWORTH: These monsters are known to be very, very gentle, with only 0.03% reported attacks from these kinds of monsters
EDGEWORTH: Therefore, the defendant cannot claim self-defense as these monsters are clearly very chilled out""", Fore.RED)


    evidence1 = objection(all_evidence)
    if evidence1 == "evidence 4: Green Monster Fur":
        all_evidence.remove("evidence 4: Green Monster Fur")
        winsound.PlaySound(f"{os.getcwd()}/music_sound_effects/objection.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        print_slowly("""
OBJECTION

YOU: oh, on the contrary, this evidence proves the monster isn't who he claimed to be
YOU: I picked this up when the monster became deceased
YOU: He was using fake fur to cover up his true identity; an 'alaskan bull worm'
YOU: These monsters have a very high rate of attacks on people compared to grey & blue monsters
""")
        time.sleep(3)
        winsound.PlaySound(None, winsound.SND_PURGE)

        print_slowly("""
EDGEWORTH: UGHH
EDGEWORTH: Well it doesnt prove that the monster was going to attack you
EDGEWORTH: He has never attacked anyone else before this, so why would he start now?""", Fore.RED)


        evidence2 = objection(all_evidence)
        if evidence2 == "evidence 5: Criminal Record":
            all_evidence.remove("evidence 5: Criminal Record")
            winsound.PlaySound(f"{os.getcwd()}/music_sound_effects/objection.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            print_slowly("""
OBJECTION

YOU: Well Edgeworth, you should've done better research
YOU: This monster was accused of 4 counts of assault back in '94
YOU: So hes been known to the police for quite some time now""")
            time.sleep(3)
            winsound.PlaySound(None, winsound.SND_PURGE)

            print_slowly("""
EDGEWORTH: OUGGHH
EDGEWORTH: However, you have no evidence to prove that he hasnt reformed from prison and wont commit the same crime again
EDGEWORTH: Unless he was seriously messed up, he did not deserve to be murdered.""", Fore.RED)

            evidence3 = objection(all_evidence)
            if evidence3 == "evidence 2: Health Condition":
                all_evidence.remove("evidence 2: Health Condition")
                winsound.PlaySound(f"{os.getcwd()}/music_sound_effects/objection.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                print_slowly("""
OBJECTION

YOU: The monster was born and diagnosed with a severe anger issue
YOU: There are many reports of him lashing out against both humans and monsters
YOU: You have no excuse for him not purposely placing himself there to harm me
""")
                time.sleep(3)
                winsound.PlaySound(None, winsound.SND_PURGE)

                print_slowly("""
EDGEWORTH: UGHDFUS
EDGEWORTH: Judge, this is the against the courts rules""", Fore.RED)
                print_slowly("\nROZ: Overturned; this is getting interesting\n", Fore.BLUE)
                print_slowly("EDGEWORTH: Well, he had full-right to be in that room, there was nothing against him being there and doing his job", Fore.RED)
                   

                evidence4 = objection(all_evidence)
                if evidence4 == "evidence 3: Entering Room License":
                    all_evidence.remove("evidence 3: Entering Room License")
                    winsound.PlaySound(f"{os.getcwd()}/music_sound_effects/objection.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    print_slowly("""
OBJECTION

YOU: You forgot one thing Edgeworth, his room license has been revoked
""")
                    time.sleep(3)
                    winsound.PlaySound(None, winsound.SND_PURGE)

                    print_slowly("EDGEWORTH: UISFDIOHFSDJOIWI",Fore.RED)
                    print_slowly("YOU: After his stay-in with the law, his license to enter rooms was revoked, therefore he is illegally entering the room")
                    print_slowly("EDGEWORTH: DSFHIUHEFUSIHFSIHJHSKFJDHFJKSFHSKJEFJ", Fore.RED)


                    winsound.PlaySound(f"{os.getcwd()}/music_sound_effects/objection.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                    print_slowly("""
DOUBLE OBJECTION

YOU: Finally the monster asked for food before the plot to kill me
YOU: This is illegal in the monsters inc. rule book, stating 'no food on the job'
YOU: I defended myself against this brutal killer
""")
                    time.sleep(3)
                    winsound.PlaySound(None, winsound.SND_PURGE)

                    print_slowly("""
ROZ: Well, what a fun journey
ROZ: For keeping me entertained, heres a breakfast item""", Fore.BLUE)

                    print_slowly("YOU ACQUIRED THE BLACK PUDDING")

                    print_slowly("""
ROZ: Well now its time to send you to jail for trashing the courtroom
ROZ: Your shoes are filthy, and you deserve a life-sentence
ROZ: Enjoy your stay in prison, human""", Fore.BLUE)                      

                    player.breakfastCollected.append("Black Pudding")
                    player.current_room = room_alcatraz_cell

                else:
                    courtroom_end()

            else:
                courtroom_end()

        else:
            courtroom_end()
#courtroom end

#alcatraz cell start
def sleep_in_bed(item=""):
    if room_alcatraz_cell["interactions"]["bed"]["checkpoint"] == 0:
        print_slowly("There's nothing left for you to do today.")
        answer = input("\nSLEEP in the bed? (Y/N) >")
        if answer == "y":
            print_slowly("You decide to go to sleep.")

            room_alcatraz_cell["interactions"]["bed"]["description"] = "It's slightly more comfortable than it looks."
            room_alcatraz_cell["interactions"]["food"] = {"name" : "prison food", "description" : "A new plate of food, how long was I asleep?", "prompt" : eat_food_2, "checkpoint" : 0}
            print_slowly("You wake up some time later surprisingly well rested.")

    if room_alcatraz_cell["interactions"]["bed"]["checkpoint"] == 1:
        answer = input("\nSLEEP in the bed? (Y/N) >")
        if answer == "y":
            print_slowly("""You could literally escape right now but you're trying to go to sleep.

Sure, why not.

Have a long nap, I'm sure nobody will notice the escape attempt,
it's only Alcatraz.


You sleep deeply and dream about your breakfast...""")
            hashbrowns()
            room_alcatraz_cell["interactions"]["bed"]["checkpoint"] = 2
        else:
            print_slowly("Just escape already.")

    if room_alcatraz_cell["interactions"]["bed"]["checkpoint"] == 2:
        print_slowly("Just get in the drain.")

def eat_food_1(item=""):
    if room_alcatraz_cell["interactions"]["food"]["checkpoint"] == 0:
        print_slowly("That food looks horrible, but you're starving.")
        answer = input("\nEAT the food? (Y/N) >")
        if answer == "y":
            print_slowly("You plug your nose and eat the cold meal.")
            print_slowly("You come across something solid in the food, it's a small file! \nThe guard must have dropped it in by accident.")
            player.inventory.append("file")
            room_alcatraz_cell["interactions"].pop("food")
        else:
            print_slowly("You'd rather starve than eat whatever is on that plate.")
room_alcatraz_cell["interactions"]["food"]["prompt"] = eat_food_1

def eat_food_2(item=""):
    if room_alcatraz_cell["interactions"]["food"]["checkpoint"] == 0:
        print_slowly("You aren't hungry, \nbut you notice that you were given a knife and fork with your food this time.")
        answer = input("\nTake the knife? (Y/N) >")
        if answer == "y":
            print_slowly("You grab the knife.")
            player.inventory.append("knife")
            room_alcatraz_cell["interactions"]["food"]["checkpoint"] = 1
        else:
            print_slowly("You leave the cutlery on the plate.")

def file_cover(item=""):
    if room_alcatraz_cell["interactions"]["drain"]["checkpoint"] == 0 and item:
        if item == "file":
            print_slowly("""You use the file to saw away at the bars.
Its incredibly difficult with the tiny tool but you power through.

Just as you are about to make it through the final bar...
The file snaps!

The grate still isn't off yet and it's too strong for you to pull off.""")
            player.inventory.remove("file")
            room_alcatraz_cell["interactions"]["drain"]["description"] = "After much hard work it is almost fully disconnected from the wall."
            room_alcatraz_cell["interactions"]["bed"]["prompt"] = sleep_in_bed
            room_alcatraz_cell["interactions"]["drain"]["checkpoint"] = 1

    if room_alcatraz_cell["interactions"]["drain"]["checkpoint"] == 1 and item:
        if item == "knife":
            print_slowly("""The knife is incredibly flimsy and your hands are covered in sweat,
but you manage to get through the final bar on the grate.
It comes loose and falls into the drainage ditch below.""")
            player.inventory.remove("knife")
            room_alcatraz_cell["interactions"]["bed"]["checkpoint"] = 1
            room_alcatraz_cell["interactions"]["drain"]["checkpoint"] = 2

    if room_alcatraz_cell["interactions"]["drain"]["checkpoint"] == 2:
        print_slowly("""You stick your head through the hole in the ground,
It smells absoloutely horrible down there, however the water doesnt look too deep.""")
        answer = input("\nJUMP in the drain? (Y/N) >")
        if answer == "y":
            print_slowly("""With seemingly no other choice, you plunge yourself into the darkness below...

You fall for a short distance before splashing feet first into the waste water.""")
            player.current_room = room_alcatraz_drain
            hack_terminal()
            room_alcatraz_cell["interactions"]["drain"]["checkpoint"] = 3
room_alcatraz_cell["interactions"]["drain"]["prompt"] = file_cover
#alcatraz cell end

#alcatraz drain start
def hack_terminal():
    print_slowly(f"""You get to your feet and fumble your way to a wall,
The sewage is up to your ankles and the smell makes your eyes water.

You should get out of here.

{Fore.WHITE}DRAIN
{Fore.YELLOW}A dark and disguisting prison sewage drain.

{Fore.GREEN}After wandering in the dark for some time, you see a small shaft of light coming from a vent in the wall.
You head over to it discovering it to be a small disused vent connecting to the main control room!

You kick in the flimsy covering and worm yourself through the gap.
It's after hours and nobody is here.

You see a single terminal is still on and blinking with some security program...

'Is that hangman?'
""")

    passwords = ["espionage", "simplification", "intergalactic"]
    word_guessed = False
    while word_guessed == False:
        time.sleep(1)
        os.system('cls')
        print_slowly("HANGMAN\n", Fore.YELLOW)
        current_word = random.choice(passwords)
        guessed_letters = []
        lives = 10
        to_print = ""
        for char in current_word:
            if char in guessed_letters:
                to_print += char+" "
            else:
                to_print += "_ "
        print_slowly(to_print+"\n", Fore.YELLOW)

        while not word_guessed and lives > 0:        
            player_guess = input("\nGuess a letter >").lower()
            while not (len(player_guess) == 1 and player_guess.isalpha()):
                print_slowly("Invalid input\n", Fore.RED)
                player_guess = input("Guess a letter >").lower()

            guessed_letters.append(player_guess)
            to_print = ""
            for char in current_word:
                if char in guessed_letters:
                    to_print += char+" "
                else:
                    to_print += "_ "
            print(f"{Fore.YELLOW}{to_print}")

            if player_guess not in current_word:
                lives -= 1
            print(f"{Fore.LIGHTRED_EX}Attempts remaining : {lives}")
            if lives == 0:
                print_slowly("\nHack failed\n", Fore.RED)

            word_guessed = to_print.split(" ")[:-1] == list(current_word)

    if lives >= 5:
        bread_and_butter()

    print_slowly("""
The terminal beeps and flashes vigorously,
you've done something you shouldn't have...

Alarms start blaring and a red lights are flashing all around you.

Over the speaker system you hear an automated voice repeating:
'EMERGENCY NUCLEAR DETONATION INITIATED!'
'ALL VITAL PERSONEL PLEASE GO TO YOUR ASSIGNED NUCLEAR SAFETY BUNKER!'

You hope this room is one of them.""")
    player.current_room = room_sea
#alcatraz drain end

#sea start
def search_rubble_1(item=""):
    if room_sea["interactions"]["1"]["checkpoint"] == 0:
        x = 0
        take_list = ["take","take the mine","take mine","mine take","take it"]
        leave_list = ["leave", "leave mine", "leave the mine", "leave it",'mine leave']
        while x < 1:
            choice = input("""
After inspecting the rubble you come across a mine, 
You don't know if it is active or not but it might be useful.
Would you like to TAKE the mine, or LEAVE it alone:\n>>""")
            fixed_choice = choice.lower().strip()
            if fixed_choice in take_list:
                x = x + 1
                print_slowly("You slowly pick up despite the dangers it might pose. \nunfortunately, it did pose a danger. Oops\n")
            elif fixed_choice in leave_list:
                print_slowly ("You make the smart choice to leave it alone \nbecause you'd rather not risk it exploding on you.\n")
                break
            else:
                (print("That is not a valid option"))
        if x >= 1:
            print_slowly("""
Holding the mine in your hands, it slowly blinks to life as a flashing red light and soft beeping noise indicate
that you have made a very bad decision. The beeping gets faster and faster
until finally...you become the poster child on why not to pick up possibly armed explosives
and much like a poster, splattered against a nearby wall.
Your adventure has unfortunately ended right before you succesfully escaped
YOU ARE EXPLODED.""")
            time.sleep(2)
            print_slowly("""
Or...at least that's what WOULD have happened had you actually made 
the silly decision to pick up an UNKNOWABLY ARMED MINE, which any sane induvidual probably wouldn't do
so lets rewind a bit and make the right decision this time.""")

            room_sea["interactions"]["1"]["description"] = "There is nothing of value, but you get a bad feeling about this place."
            room_sea["interactions"]["1"]["checkpoint"] = 1
room_sea["interactions"]["1"]["prompt"] = search_rubble_1

def search_rubble_2(item=""):
    if room_sea["interactions"]["2"]["checkpoint"] == 0:
        print_slowly("After a bit of searching you find a SCOOP.")
        player.inventory.append("scoop")
        room_sea["interactions"]["2"]["checkpoint"] = 1
room_sea["interactions"]["2"]["prompt"] = search_rubble_2

def search_rubble_4(item=""):
    if room_sea["interactions"]["4"]["checkpoint"] == 0:
        print_slowly("You come across a bottle of DYE.")
        player.inventory.append("dye")
        room_sea["interactions"]["4"]["checkpoint"] = 1
room_sea["interactions"]["4"]["prompt"] = search_rubble_4

def search_rubble_5(item=""):
    if room_sea["interactions"]["5"]["checkpoint"] == 0:
        beans_prompt()
        room_sea["interactions"]["5"]["checkpoint"] = 1
room_sea["interactions"]["5"]["prompt"] = search_rubble_5

def search_rubble_6(item=""):
    if room_sea["interactions"]["6"]["checkpoint"] == 0:
        print_slowly("You pull a HANDLE from the mud.")
        player.inventory.append("handle")
        room_sea["interactions"]["6"]["checkpoint"] = 1
room_sea["interactions"]["6"]["prompt"] = search_rubble_6

def use_workbench(item=""):
    items = {"handle", "scoop", "dye"}
    if room_sea["interactions"]["workbench"]["checkpoint"] < 3 and item:
        if item in items:
            player.inventory.remove(item)
            print_slowly(f"You place the {item.upper()} in the workbench\n")
            room_sea["interactions"]["workbench"]["checkpoint"] += 1
        else:
            print_slowly("That cannot be used here.")

    if room_sea["interactions"]["workbench"]["checkpoint"] == 3:
        print_slowly(f"""You gathered all the items needed to craft the pink shovel.

You combine the items in the crafting table...
YOU CRAFTED THE {Fore.LIGHTMAGENTA_EX}PINK SHOVEL{Style.RESET_ALL}{Fore.GREEN}.""")
        player.inventory.append("shovel")
        room_sea["interactions"]["workbench"]["checkpoint"] = 4
room_sea["interactions"]["workbench"]["prompt"] = use_workbench

def dig_fence(item=""):
    if room_sea["interactions"]["fence"]["checkpoint"] == 0 and item:
        if item == "shovel":
            print_slowly("""You pull out the pink shovel and start digging.....
You are lightning fast and you somehow manage to dig down and up out of the prison.
Gravity has been proven wrong once again.

You run to the shoreline.
You have no where left to go but into the ocean...
""")
            player.inventory.remove("shovel")
            room_sea["interactions"]["fence"]["checkpoint"] = 1
            player.current_room = room_pirateship
            battle_ships()
room_sea["interactions"]["fence"]["prompt"] = dig_fence
#sea end

#pirate_ship start
def ship_death():
    print_slowly("""
Your lacking skills in naval warfrare result in your DEFEAT by the enemy.
Your poor ship, broken and capsizing, begins sinking into the ocean.
With screams and panic washing over the ship, you manage to get knocked overboard and fall into the ocean.
Unfortunately, you never learnt how to swim, not that there was anything near to swim to, and you sink.
YOU ARE DROWNED.
m""")
    time.sleep(2)
    print_slowly("""
Or...at least that's what WOULD have happened had you actually been DEFEATED by the enemy.
No no this was just a mental simulation to prepare yourself for the upcoming battle.
so lets rewind a bit and do it for real this time.""")

def normalise_square_input(square_input,valid_letters):
    square_inp = square_input[0].upper() + square_input[1]
    if len(square_inp) == 2:
        if square_inp[0].isalpha() and square_inp[1].isnumeric():
            if square_inp[0] in valid_letters and int(square_inp[1]) > 0 and int(square_inp[1]) <= 5:
                return square_inp
            else:
                print_slowly("Ensure the letter is between A-C and the number is between 1-5")
        else:
            print_slowly("Ensure the first character is a letter and the second character is a number")
    else:
        print_slowly("Ensure the string is two characters long")

def enemy_retaliate(ocean,ship,valid_letters,count):
    final_letter = valid_letters[random.randint(0,2)]
    final_number = random.randint(1,5)
    final_attack = str(final_letter.upper()) + str(final_number)
    if final_attack in ocean:
        print_slowly('\nThe opposing team missed their shot. You breathe a sigh of relief\n')
        winsound.PlaySound("C:/Users/Josh/OneDrive - Cardiff University/_UNIVERSITY_WORK/Year_1/Code/Group13_game/group-13/Music_Soundeffects/shot_hit.wav",winsound.SND_ASYNC)
    else:
        print_slowly('\nThe opposing team batters your ship with a cannon. You are scared for your life\n')
        winsound.PlaySound("C:/Users/Josh/OneDrive - Cardiff University/_UNIVERSITY_WORK/Year_1/Code/Group13_game/group-13/Music_Soundeffects/shot_missed.wav",winsound.SND_ASYNC)
        ship.remove(final_attack)
        ocean.append(final_attack)
        count += 1
        if count == 4:
            ship_death()
            battle_ships()

def battle_ships():
    print_slowly("""You leap into the ocean, not knowing what your next move will be
the water is cold and black.
Your vision fades and you fall unconscious.....
BAM!
something pulls you from the water and puts you on your feet.

You clear your eyes to see Captain Jack Sparrow pointing into the deep ocean
A ship comes into view, before suddenly dissappearing behind a smoke screen running across the water.

Jack shouts from across the boat 'who r we aiming for mate' before pulling up a 2022 macbook pro,
you realise the game you've been put in...
""")

    time.sleep(0.8)
    draw_ship()

    print_slowly("""
BATTLESHIPS

'Lets show em what we're made of mate
input a letter from A-E and a number from 1-3 in sequence lad, for example E2
simple enough for you, don't be a davy jones, and lets blow em to smithereens'

OBJECTIVE: Hit all four squares of the opposing boat

""")
    count = 0
    enemy_count = 0
    enemy_ocean = ["A1","A2","A3","A4","B3","B4","B5","C1","C4","C5"]
    enemy_ship = ["B1","B2","C2","C3"]
    breakfast_item = ["A5"]
    ally_ocean = ["A1","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5"]
    ally_ship = ["A2","A3","A4","A5"]
    letters = ["A","B","C"]
    shots_used = []
    shots_left = ["A1","A2","A3","A4","A5","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5"]
    while count != 4:
        #print("Shots used: " + str(shots_used).replace('[', '').replace(']', ''))
        print("\n" + "Shots left: " + str(shots_left).replace('[', '').replace(']', ''))
        string = input("\n" + "Which square do you want to hit: ")
        normalised_string = normalise_square_input(string, letters)
        if normalised_string in enemy_ocean:
            print_slowly('\nYou have missed the opponents ship. You are depressed')
            winsound.PlaySound(f"{os.getcwd()}/music_sound_effects/shot_missed.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            shots_left.remove(normalised_string)
            shots_used.append(normalised_string)
            enemy_retaliate(ally_ocean,ally_ship,letters,enemy_count)
        elif normalised_string in enemy_ship:
            print_slowly('\nYou hear a loud walloping from across the smoke stream. Square ' + normalised_string + ' has hit the opposing ship. You laugh maniacally')
            winsound.PlaySound(f"{os.getcwd()}/music_sound_effects/shot_hit.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            enemy_ship.remove(normalised_string)
            enemy_ocean.append(normalised_string)
            shots_left.remove(normalised_string)
            shots_used.append(normalised_string)
            count += 1
            if count ==4:
                break
            else:
                enemy_retaliate(ally_ocean,ally_ship,letters,enemy_count)
        elif normalised_string in breakfast_item:
            print_slowly("You hit a box in the ocean. It opens up to reveal a breakfast item: Mushrooms")
            player.breakfastCollected.append("Mushrooms")
        else:
            pass

    print_slowly("""
You have successfully taken down the opposing ship.

A mountain of gold appears before you, falling from the sky
'Good job mate, me and the boys knew we could rely on you, now what will come of you'

you turn around to see all the pirates surrounding you
'Well you know what they say, never trust a pirate'

CLUNK

Captain Jack Sparrow hits you over the head with a banjo. Ouch.

You awaken in your kitchen, of all places.
You are starving""")
    player.current_room = room_kitchen
#pirate ship end

#kitchen start
def ending():
    if len(player.breakfastCollected) == 0:
        print_slowly("""
you did not collect any breakfast items. With your adventure over and the adrenaline leaving your system, 
your vision becomes hazy and you see illusions of the last supper, adorned with plates of food.
With your last burst of energy, you swipe at the image, but alas, it fades into the air and you collapse on your kitchen floor and starve to death.
Perhaps the outcome could have been different had you taken a better look for the scattered breakfast items.""")

    elif len(player.breakfastCollected) <= 3:
        print_slowly("""
You managed to pick up a meagre amount of breakfast items, enough to live but not much else. 
Your remaining energy is used to cook up what little you have and drag yourself over to your table to eat your reward.
The food is finished in a few bites and you realize this won't be enough to get you through the day and decide to just go back to bed.
Unfortunately, you had an important exam today and your absence resulted in immediate failure and expulsion.

Years pass and you work a local job, just barely scraping by.
You wonder if attending that exam could have landed you a better place in life.
Perhaps the outcome could have been different had you taken a better look for the scattered breakfast items.""")
        
    elif len(player.breakfastCollected) > 3 and len(player.breakfastCollected) < 6:
        print_slowly(""" 
You managed to pick up a fair amount of breakfast items, enough for a hearty meal to fuel you throughout the day.
Your remaining energy is used to cook up what is shaping up to be an excellent breakfast.
After your long journey, the aroma of breakfast re-energizes you with a boost in morale.
You refuse to collapse before consuming your hard earned feast, and bring your food to the table, ready to eat.
Waves of energy wash over you with each bite, and with a full tank, you feel ready to take on the day.
You head over to university and attend your exam with glimmering confidence. 

You start the exam and it goes smoothly.
All the experience from your morning adventure fills you with knowledge and inspiration...however.
Towards the end of the exam, you feel yourself slowing down and lose the luster you had at the start.
You leave the exam hall, feeling like you had done a good job, but wondering if you could have done even better.
Perhaps the outcome could have been different had you found all the scattered breakfast items.""")
    else:
        print_slowly("""
Your breakfast is fit for a king, you lug your hard earned breakfast treasures into the kitchen.
Having collected every breakfast item, you feel as if you could stay fed for weeks and become motivated.
With a flurry of inspiration, you use your last burst of energy and enter a trance-like state.
You could only be described as a god of cooking, as your hands move in ways not possible for mere mortals.

You glide over to your seat, staring in amazement at the feast you created.
You take a single bite.
The flavors of the universe fill your mouth as the energy of stars well up inside of you.
You bulldoze through the rest of the meal, each bite tasting better than the last.
Feeling like you could take on anything, you get ready for university to attend your exam.

You start the exam and it goes perfectly.
All the experience from your morning adventure fills you with knowledge and inspiration as you fly through the exam.
Not a single drop of energy from your breakfast goes to waste as you finish it, still feeling energized.
You leave the exam hall feeling like a king, you conquered the exam and got the highest score.
You could not imagine a better outcome than this.

You were successful in your QUEST FOR BREAKFAST.""")

    print_slowly("""
Thank you for playing our game!

BY:
Abbie Griffiths,
Beth Thomas,
Chanaksha Nimgade,
Josh Noble,
Matt Collins
and
Thomas Holland""", Fore.CYAN)
    player.game_playing = False
    import msvcrt
    while msvcrt.kbhit():
            msvcrt.getch()
room_kitchen["interactions"]["cooker"]["prompt"] = ending
#kitchen end
