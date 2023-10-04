from rooms import *
import player
from parser import *
from room_prompts import *
from draw_ascii import *
import time

def print_room_description(room):
    '''
    prints the description of the current room and story if they are entering the room for the first time
    '''
    if not room["visited"]:
        print_slowly(room['story'])
        room["visited"] = True

    time.sleep(0.2)
    print("\n"+room['id'].upper(), Fore.WHITE)
    time.sleep(0.2)
    print(f"{Fore.YELLOW}{room['description']}{Style.RESET_ALL}\n")


def print_room_interactions(room):
    '''
    prints each of the interactable objects in the room 
    '''
    for interaction in room["interactions"]:
        time.sleep(0.2)
        print(room["interactions"][interaction]["name"])


def print_room_exits(room): 
    '''
    prints each of the exits in the current room
    '''
    for exit in room["exits"]:
        time.sleep(0.2)
        print(room["exits"][exit]["name"])


def print_room(room):
    print_room_description(room)
    time.sleep(0.2)
    print("In the room:")
    print(Fore.YELLOW, end='')
    print_room_exits(room)
    print_room_interactions(room)
    print(Style.RESET_ALL, end='')
    import msvcrt
    while msvcrt.kbhit():
            msvcrt.getch()


def print_inventory(items):
    time.sleep(0.2)
    print("\nInventory:")
    for item in items:
        time.sleep(0.2)
        print(f"{Fore.YELLOW}{item}{Style.RESET_ALL}")


def player_input():
    '''
    takes the players input, normalises it and runs the command
    '''
    time.sleep(0.2)
    command = input("\n>>")
    normalised_command = normalise_text(command)
    check_command(normalised_command)


def check_command(command):
    '''
    takes the players normalised command and attempts to run it 
    '''
    if len(command) > 1:
        match command[0]:
            case "inspect":
                #if inspecting an interaction then print the room description and run prompt if it has one
                if command[1] in player.current_room["interactions"]:
                    time.sleep(0.4)
                    print_slowly(player.current_room["interactions"][command[1]]["description"])
                    if player.current_room["interactions"][command[1]]["prompt"]:
                        time.sleep(0.4)
                        player.current_room["interactions"][command[1]]["prompt"]()
                #if inspecting exit print status of exit
                elif command[1] in player.current_room["exits"]:
                    time.sleep(0.4)
                    print_slowly(player.current_room["exits"][command[1]]["description"])
                #if inspecting item ...
                elif command[1] in player.inventory:
                    print(command[1] + " is an item")

            case "use":
                if len(command) > 2 and command[1] in player.inventory:
                    if command[2] in player.current_room["exits"]:
                        if player.current_room["exits"][command[2]]["prompt"]:
                            time.sleep(0.4)
                            player.current_room["exits"][command[2]]["prompt"](command[1])
                            return
                    if command[2] in player.current_room["interactions"]:
                        if player.current_room["interactions"][command[2]]["prompt"]:
                            time.sleep(0.4)
                            player.current_room["interactions"][command[2]]["prompt"](command[1])
                            return
                time.sleep(0.4)
                print("cannot be used in that way")

            case "go":
                if command[1] in player.current_room["exits"]:
                    if player.current_room["exits"][command[1]]["unlocked"]:
                        time.sleep(0.4)
                        player.current_room = rooms_list[command[1]]
                    else:
                        time.sleep(0.4)
                        print("The door is locked")
                else:
                    print("Cannot go there")

            case "help":
                print("The usable commands are:\nINSPECT\nUSE\nGO")

            case _:
                time.sleep(0.4)
                print("Command not understood")
    else:
        time.sleep(0.4)
        print("Command not understood")

def game_loop():
    '''
    main game loop
    '''
    while player.game_playing:
        print_room(player.current_room)
        print_inventory(player.inventory)
        player_input()

if  __name__ == "__main__":
    game_loop()
