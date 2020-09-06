# -*- coding: utf-8 -*-

import time

# from credits import send_credits

global name

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[97m'
    CYAN = '\033[0;36m'
    PURPLE = '\033[0;35m'
    RED = '\033[0;31m'

def send_cat():
    print(bcolors.CYAN + " ")
    print("       \`--.    ")
    print("        )  _`-. ")
    print("       ,  : `. \ ")
    print("      : _   '   \ ")
    print("      ; *` _.    `--._")
    print("       `-.-'          `-.")
    print("          |       `       `.")
    print("          :.       .        \ ")
    print("          | \  .   :   .-'   .")
    print("          :  )-.;  ;  /      :")
    print("          :  ;  | :  :       ;-.")
    print("          ; /   : |`-:     _ `- )")
    print("        ,-' /  ,-' ; .-`- .' `--'")
    print("        `--'   `---' `---'")
    print(bcolors.WHITE + " ")

def credits():
    print(bcolors.OKGREEN + " ")
    print("   _____              _ _ _       ")
    print("  / ____|            | (_) |      ")
    print(" | |     _ __ ___  __| |_| |_ ___ ")
    print(" | |    | '__/ _ \/ _` | | __/ __|")
    print(" | |____| | |  __/ (_| | | |_\__ \ ")
    print("  \_____|_|  \___|\__,_|_|\__|___/")
    print(bcolors.WHITE + " ")
    time.sleep(5)

    print(bcolors.PURPLE + " ")
    print("           _           ")
    print("     /\   | |          ")
    print("    /  \  | | _____  __")
    print("   / /\ \ | |/ _ \ \/ /")
    print("  / ____ \| |  __/>  < ")
    print(" /_/    \_\_|\___/_/\_\ ")
    time.sleep(5)
    print(bcolors.WHITE + " ")

    print(bcolors.RED + " ")
    print("       _               ")
    print("      | |              ")
    print("      | | ___  ___ ___ ")
    print("  _   | |/ _ \/ __/ __|")
    print(bcolors.WHITE + " | |__| |  __/\__ \__ \ ")
    print("  \____/ \___||___/___/ ")
    print(bcolors.WHITE + " ")
    time.sleep(5)

    print(bcolors.WARNING + " ")
    print("  ______     _             _     ")
    print(" |___  /    (_)           | |    ")
    print("    / / __ _ _ _ __   __ _| |__  ")
    print("   / / / _` | | '_ \ / _` | '_ \ ")
    print("  / /_| (_| | | | | | (_| | |_) |")
    print(" /_____\__,_|_|_| |_|\__,_|_.__/ ")
    time.sleep(5)
    print(bcolors.WHITE + "")

    print(bcolors.CYAN + " ")
    print("  _  __     _      ")
    print(" | |/ /    | |     ")
    print(" | ' /_   _| | ___ ")
    print(" |  <| | | | |/ _ \ ")
    print(" | . \ |_| | |  __/")
    print(" |_|\_\__, |_|\___|")
    print("       __/ |       ")
    print("      |___/        ")
    time.sleep(5)
    print(bcolors.WHITE + "")

    print("Credits")
    time.sleep(5)
    print("Alex Arditti")
    time.sleep(5)
    print("Jess Winteringham")
    time.sleep(5)
    print("Zainab Sheikh")
    time.sleep(5)
    print("Kyle Hicks")

def winner_level():
    print("Your family are waiting for you. Mum, dad and brother, Billy, welcome you home with open arms and give you a tin of Magic Tuna")
    #time.sleep(5)

    print("Congratulations on winning the game")
    user_choice6 = input("would you like to play again [yes / no] ")
    if user_choice6 == "Yes" or user_choice6 == "y" or user_choice6 == "yes":
        time.sleep(5)
        game_introduction()
    elif user_choice6 == "no" or user_choice6 == "n" or user_choice6 == "No":
        print("Thank you for playing")
        time.sleep(5)
        credits()
def level_five():
    print("You are nearly home!")
    time.sleep(5)
    print("Just one more obstacle to complete...")
    time.sleep(5)
    print("At Hyde Park Corner the Household Cavalry are making their way to the Changing of the Guard ceremony")
    time.sleep(5)
    print("Do you catch a lift on the back of one of the horses on your left?")
    time.sleep(5)
    print("Or...")
    time.sleep(5)
    print("look right and spot a dog walker with a band of dogs.")
    time.sleep(5)
    print("All of a sudden you recognise Max, the dog from next door...")

    user_choice5 = input("Do you turn [Left/Right] ")

    if user_choice5 == "right" or user_choice5 == "r" or user_choice5 == "Right" or user_choice5 == "R":
        print("Thankfully you and Max and great friends.")
        time.sleep(5)
        print("You jump on his back and get a lift all the way home!")
        time.sleep(5)
        winner_level()
    elif user_choice5 == "left" or user_choice5 == "l" or user_choice5 == "Left" or user_choice5 == "L":
        print("You catch a ride on the back of a horse.")
        time.sleep(5)
        print("Unfortunately, the horse is very snooty and doesn't take kindly to being used as a taxi")
        time.sleep(5)
        print("He bucks you off and you land back to Soho and level 2!")
        time.sleep(5)
        level_two()
    else:
        print("Sorry I didn't get that")
        user_choice_level_five = input("Do you turn [left/right]")
        if user_choice_level_five == "left" or user_choice_level_five == "l" or user_choice_level_five == "Left" or user_choice_level_five == "L":
            print("You catch a ride on the back of a horse.")
            time.sleep(5)
            print("Unfortunately, the horse is very snooty and doesn't take kindly to being used as a taxi")
            time.sleep(5)
            print("He bucks you off and you land back to Soho and level 2!")
            time.sleep(5)
            level_two()
        elif user_choice_level_five == "right" or user_choice_level_five == "r" or user_choice_level_five == "Right" or user_choice_level_five == "R":
            print("Thankfully you are great friends with the dog, called Max.")
            time.sleep(5)
            print("You jump on his back for a lift all the way home!")
            time.sleep(5)
            winner_level()


def level_four():
    print("It’s a beautiful sunny day and you see a family settling down to a picnic in Hyde park.")
    time.sleep(5)
    print("Suddenly you feel rather hungry – you haven't eaten for ages")
    time.sleep(5)
    print("The family produce a tin of yummy tuna and offer some to you.")
    time.sleep(5)
    print("In a nearby lime tree, a colony of noisy ring-necked parakeets are watching you.")
    time.sleep(5)
    print("Suddenly a cheeky parakeet swoops in and tries to steal the tuna...")
    time.sleep(5)
    print("Do you fight the parakeet?")
    time.sleep(5)
    print("Or...")
    time.sleep(5)
    print("Run away?")

    user_choice4 = input("Do you [fight the parakeet/run away?] ")

    if user_choice4 == "fight" or user_choice4 == "fight the parakeet" or user_choice4 == "f" or user_choice4 == "F":
        print("The magic tuna gives you super power and you take a giant swipe with your paw...")
        time.sleep(5)
        print("You miss...")
        time.sleep(5)
        print("The Parakeet pecks you back but you dodge it at the last minute")
        time.sleep(5)
        print("You take another swipe and this time you hit the parakeet square on the beak")
        time.sleep(5)
        print("It flies off as the tuna had given you the edge.")
        time.sleep(5)
        print("You continue on your way")
        time.sleep(5)
        level_five()

    elif user_choice4 == "run away" or user_choice4 == "r" or user_choice4 == "Run Away" or user_choice4 == "Run" or user_choice4 == "R":
        print("You run away but get lost in Hyde Park and run back towards Trafalgar Square")
        time.sleep(5)
        print("Back to Level Three")
        time.sleep(5)
        level_three()
    else:
        print("Sorry I didn't get that")
        user_choice_level_four = input(
            "Do you [Fight the parakeet/Run away?] ")
        if user_choice_level_four == "fight" or user_choice_level_four == "fight the parakeet" or user_choice_level_four == "f":
            print("Thanks to the magic tuna you take a giant swipe with your paw...")
            time.sleep(5)
            print("You miss...")
            print("The Parakeet pecks you back but you dodge it at the last minute")
            time.sleep(5)
            print("You take another swipe and this time you hit the parakeet square on the beak")
            time.sleep(5)
            print("It flies off as the tuna had given you the edge.")
            time.sleep(5)
            print("You continue on your way")
            time.sleep(5)
            level_five()
        elif user_choice_level_four == "run away" or user_choice_level_four == "r" or user_choice_level_four == "Run Away":
            print("You run away but get lost in Hyde Park and run back towards Trafalgar Square")
            time.sleep(5)
            print("Back to Level Three")
            time.sleep(5)
            level_three()
def level_three():
    print("You jump into a sarcophagus and are teleported to Trafalgar Square")
    time.sleep(5)
    print("You arrive at Trafalgar Square. The tourists are feeding the pigeons. The pigeons grow into an enormous flock.")
    time.sleep(5)
    print("Suddenly one of the birds swoops down and tries to peck your eyes. One of the four lion statues that guard Nelson’s Column comes to life and swipes the pigeons away with it’s gigantic paw.")
    time.sleep(5)
    print("To your right a magician produces a rabbit out of a hat. He puts the hat on the ground.")
    time.sleep(5)
    print("To your left a family with a baby in a pram are watching the spectacle.")
    time.sleep(5)
    print("Do you turn right and jump into the magicians hat?")
    time.sleep(5)
    print("Or...")
    time.sleep(5)
    print("Do you turn left and crawl underneath the baby’s pram?")

    user_choice3 = input("Do you turn [Left/Right?] ")

    if user_choice3 == "right" or user_choice3 == "r" or user_choice3 == "Right" or user_choice3 == "R":
        print("You are taken through a magic portal. You find yourself in a movie theatre in the West End, watching the film 'Cats'. The film sends you to sleep.")
        time.sleep(5)
        print("You wake up the next day and find yourself back in Trafalgar Square")
        level_three()
    elif user_choice3 == "left" or user_choice3 == "l" or user_choice3 == "Left" or user_choice3 == "L":
        print("You have escaped from the pigeons and sneak on to a London bus to Hyde Park")
        time.sleep(5)
        level_four()
    else:
        print("Sorry I didn't get that")
        user_choice_level_three = input("Do you turn [left / right]")
        if user_choice_level_three == "left" or user_choice_level_three == "l" or user_choice_level_three == "Left" or user_choice_level_three == "L":
            print(
                "You have escaped from the pigeons and sneak on to a London bus to Hyde Park")
            time.sleep(5)
            level_four()
        elif user_choice_level_three == "right" or user_choice_level_three == "r" or user_choice_level_three == "Right" or user_choice_level_three == "R":
            print("You are taken through a magic portal. You find yourself in a movie theatre in the West End, watching the film 'Cats'. The film sends you to sleep.")
            time.sleep(5)
            print("You wake up the next day are you are now back in Trafalgar Square")
            time.sleep(5)
            level_three()
def level_two():
    time.sleep(5)
    print("You escape and hitch a ride on the back of a passing bike ridden by a hipster courier")
    time.sleep(5)
    print("You are in a narrow alleyway in the heart of Soho’s red light district.")
    time.sleep(5)
    print("Many strange and wonderful sights are around you.")
    time.sleep(5)
    print("You come face to face with a swarm of ravenous rats....")
    time.sleep(5)
    print("There are too many of them to fight.")
    time.sleep(5)
    print("To your right you see an uncovered storm drain, which a group of workmen are fixing.")
    time.sleep(5)
    print("Do turn left and throw a fur ball to distract the rats?")
    time.sleep(5)
    print("Or...")
    time.sleep(5)
    print("Do you turn right and disappear into the sewer?")
    time.sleep(5)

    user_choice2 = input("Do you turn [Left/Right] ")

    if user_choice2 == "left" or user_choice2 == "l" or user_choice2 == "Left" or user_choice2 == "L":
        print("You continue on your way. You meet a group of Scientologists on Goodge Street. They try to convert you for the next 3 hours")
        time.sleep(5)
        print("back to level 1")
        level_one()
    elif user_choice2 == "right" or user_choice2 == "r" or user_choice2 == "Right" or user_choice2 == "R":
        print("The sewer takes you to the British Museum. You visit the sphinx collection and your ancient ancestors help you on your way.")
        time.sleep(5)
        level_three()
    else:
        print("Sorry I didn't get that")
        user_choice_level_two = input("Do you turn [Left/Right] ")
        if user_choice_level_two == "left" or user_choice_level_two == "l" or user_choice_level_two == "Left" or user_choice_level_two == "L":
            print("You continue on your way. You meet a group of Scientologists on Goodge Street. They try to convert you for the next 3 hours")
            print("back to level 1")
            time.sleep(5)
            level_one()
        elif user_choice_level_two == "right" or user_choice_level_two == "r" or user_choice_level_two == "Right" or user_choice_level_two == "R":
            print("The sewer takes you to the British Museum. You visit the sphinx collection and your ancient ancestors help you on your way.")
            time.sleep(5)
            level_two()

def game_introduction():
    time.sleep(5)
    print("A serial catnapper has been terrorising London")
    time.sleep(5)
    print("You, a Persian cat, have been stolen from your beloved family in West London and find yourself in a dingy townnhouse at a secret address in Spitalfields, 8 miles across town.")
    time.sleep(5)
    print("While Scotland Yard sleuths attempt to track him down, you must escape and navigate London’s streets to your home, before he catches you again.")
    time.sleep(5)

def level_one():
    print("You hear the lock begin to turn...")
    time.sleep(5)
    print("Your cat ears prick up!")
    time.sleep(5)
    print("Do you turn left and try to dart out onto the street below through the crack in the door and risk getting caught?")
    time.sleep(5)
    print("Or...")
    time.sleep(5)
    print("Do you turn right and look for an open window to escape through?")
    time.sleep(5)
    user_choice = input("Do you turn [Left/Right] ")
    if user_choice == "left" or user_choice == "l" or user_choice == "Left" or user_choice == "L":
        time.sleep(5)
        level_two()
    elif user_choice == "right" or user_choice == "r" or user_choice == "Right" or user_choice == "R":
        print("Did you really think a professional catnapper would leave a window open?! Hahaha")
        time.sleep(5)
        print("Try again")
        time.sleep(5)
        level_one()
    else:
        print("Sorry I didn't get that")
        user_choice_level_one = input("Do you turn [Left/Right] ")
        if user_choice_level_one == "left" or user_choice_level_one == "l" or user_choice_level_one == "Left" or user_choice_level_one == "L":
            time.sleep(5)
            level_two()
        elif user_choice_level_one == "right" or user_choice_level_one == "r" or user_choice_level_one == "Right" or user_choice_level_one == "R":
            print(
                "Did you really think a professional catnapper would leave a window open! Hahaha")
            time.sleep(5)
            print("Try again")
        time.sleep(5)
        level_one()

def start_game():
    # Don't edit, this works fine
    send_cat()
    print(bcolors.OKGREEN + " ")
    print("  _____      _      ____      _")
    print(" / ____|    | |    / __ \    | |")
    print("| |     __ _| |_  | |  | | __| |_   _ ___ ___  ___ _   _")
    print("| |    / _` | __| | |  | |/ _` | | | / __/ __|/ _ \ | | |")
    print("| |___| (_| | |_  | |__| | (_| | |_| \__ \__ \  __/ |_| |")
    print(" \_____\__,_|\__|  \____/ \__,_|\__, |___/___/\___| \__,|")
    print("                                __/ /              _ _/ /")
    print("                               |___/              |____/")
    print(bcolors.WHITE + " ")
    cat_name = input("Please enter your name: ")
    print(" ")
    #print("Welcome to Cat Odyssey, " + cat_name.capitalize() + ". We hope you have a fun journey!")

    if cat_name == "credits":
        credits()
        time.sleep(5)
        #send_cat()
        for i in range(20):
            print(" ")
        start_game()
    elif cat_name == "cheat":
        print("      _____ _                _      ____       _                          ")
        print("     / ____| |              | |    / __ \     | |                         ")
        print("    | |    | |__   ___  __ _| |_  | |  | | __ | |_    ___ ___  ___ _   _  ")
        print("    | |    | ‘_ \ / _ \/ _` | __| | |  | |/ _` | | | / __/ __|/ _ \ | | | ")
        print("    | |____| | | |  __/ (_| | |_  | |__| | (_| | |_| \__ \__ \  __/ |_| | ")
        print("     \_____|_| |_|\___|\__,_|\__|  \____/ \__,_|\__, |___/___/\___|\__, | ")
        print("                                                  _/ |              __/ | ")
        print("                                                 |___/              |___/  ")
        time.sleep(5)
        print("Welcome to Cheat Odyssey, We hope you have a fun time cheating!")
        print("Level 1 - Left")
        print("Level 2 - Right")
        print("Level 3 - Left")
        print("Level 4 - Fight")
        print("Level 5 - Right")
        time.sleep(5)
        send_cat()
        start_game()
        return
    is_ready = input("Are you ready? [Yes / No] ")
    if is_ready == "Yes" or is_ready == "yes" or is_ready == "Y" or is_ready == "y":
        name = cat_name
        print("Game loading...")
        time.sleep(5)
        print("Welcome to Cat Odyssey, " + name.capitalize())
        game_introduction()
        time.sleep(5)
        level_one()
        winner_level()
    elif is_ready == "No" or is_ready == "no" or is_ready == "N" or is_ready == "n":
        credits()
        time.sleep(5)
        send_cat()
        start_game()
start_game()







