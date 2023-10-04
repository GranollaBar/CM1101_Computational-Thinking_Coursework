import player

def beans_prompt():
    user_input = input("\nYou see a shining tin in your room. Do you want to pick it up? (Y/N) >>").lower()
    while user_input != "y":
        print("You can't leave, for some reason you really feel like you should take this with you.")
        user_input = input("\nYou see a shining tin in your room. Do you want to pick it up? (Y/N) >>").lower()

    print("Congratulations you have found a tin of beans!")
    player.breakfastCollected.append("beans")
    print("You have collected", len(player.breakfastCollected), "breakfast items")

def blackpudding():
    user_input = input("\nYou see an orange bag in the corner of your eye. Do you want to pick it up? (Y/N) >>").lower()
    while user_input != "y":
        print("You can't leave, for some reason you really feel like you should take this with you.")
        user_input = input("\nYou see an orange bag in the corner of your eye. Do you want to pick it up? (Y/N) >>").lower()

    print("Congratulations you have found black pudding and a pair of goggles!")
    player.breakfastCollected.append("black pudding")
    print("You have collected", len(player.breakfastCollected), "breakfast items")

def bread_and_butter():
    user_input = input("\nYou register that there is a shopping bag in the room. Do you want to pick it up? (Y/N) >>").lower()
    while user_input != "y":
        print("You can't leave, for some reason you really feel like you should take this with you.")
        user_input = input("\nYou register that there is a shopping bag in the room. Do you want to pick it up? (Y/N) >>").lower()
    
    print("Congratulations you have found a loaf of bread and some butter!")
    player.breakfastCollected.append("bread")
    player.breakfastCollected.append("butter")
    print("You have collected", len(player.breakfastCollected), "breakfast items")

def eggs():
    user_input = input("\nYou see a Chicken who has just laid an egg. Do you want to pick it up? (Y/N) >>").lower()
    while user_input != "y":
        print("You can't leave, for some reason you really feel like you should take this with you.")
        user_input = input("\nYou see a Chicken who has just laid an egg. Do you want to pick it up? (Y/N) >>").lower()

    print("Congratulations you have found an egg!")
    player.breakfastCollected.append("egg")
    print("You have collected", len(player.breakfastCollected), "breakfast items")

def hashbrowns():
    user_input = input("\nYou see a green box. Do you want to pick it up? (Y/N) >>").lower()
    while user_input != "y":
        print("You can't leave, for some reason you really feel like you should take this with you.")
        user_input = input("\nYou see a green box. Do you want to pick it up? (Y/N) >>").lower()

    print("Congratulations you have found a bag of hash browns!")
    player.breakfastCollected.append("hash browns")
    print("You have collected", len(player.breakfastCollected), "breakfast items")

def sausages():
    user_input = input("\nYou register a pink packet in the room. Do you want to pick it up? (Y/N) >>").lower()
    while user_input != "y":
        print("You can't leave, for some reason you really feel like you should take this with you.")
        user_input = input("\nYou register a pink packet in the room. Do you want to pick it up? (Y/N) >>").lower()
    
    print("Congratulations you have found a pack of sausages!")
    player.breakfastCollected.append("sausages")
    print("You have collected", len(player.breakfastCollected), "breakfast items")

def bacon():
    user_input = input("\nYou see a red object. Do you want to pick it up? (Y/N) >>").lower()
    while user_input != "y":
        print("You can't leave, for some reason you really feel like you should take this with you.")
        user_input = input("\nYou see a red object. Do you want to pick it up? (Y/N) >>").lower()

    print("Congratulations you have found slices of bacon!")
    player.breakfastCollected.append("bacon")
    print("You have collected", len(player.breakfastCollected), "breakfast items")

def tomato():
    user_input = input("\nYou notice a plant. Do you want to pick it up? (Y/N) >>").lower()
    while user_input != "y":
        print("You can't leave, for some reason you really feel like you should take this with you.")
        user_input = input("\nYou notice a plant. Do you want to pick it up? (Y/N) >>").lower()

    print("Congratulations you have found Tomatoes growing on the plant!")
    player.breakfastCollected.append("Tomatoes")
    print("You have collected", len(player.breakfastCollected), "breakfast items")
