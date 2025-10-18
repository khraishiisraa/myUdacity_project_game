
# play_game()لعبة المغامرة بدون عشوائية اختيار السلاح

import time

# Global variables
treasures = []
weapons = []
defeated_monsters = []
required_treasures = ["gold coins", "diamond", "magic carpet"]


def tale(message):
    print(message)
    time.sleep(1)


def choose_weapon():
    if not weapons:
        print("You have no weapons.")
        return "nothing"
    print("Your weapons:", ", ".join(weapons))
    choice = input("Choose a weapon:\n").strip().lower()
    if choice in [w.lower() for w in weapons]:
        return choice
    else:
        print("Invalid weapon.")
        return choose_weapon()


def check_win():
    if set(treasures) == set(required_treasures):
        tale("you have all required treasures\n")
        tale("congratulation, you win\n")
        tale("you could leave the island,")
        tale("return to your home\n")
        win_choice()


def win_choice():
    choice = input("do you want 1.play again\n or\n 2.exit (1/2)\n")
    if choice == "1":
        treasures.clear()
        weapons.clear()
        defeated_monsters.clear()
        play_game()
    elif choice == "2":
        out_game()
    else:
        tale("Invalid choice, the game ends.")
        out_game()


def play_game():
    inter()
    player()
    choice_place()


def inter():
    tale("welcome to new Adventure\n")
    tale("you found yourself on an island after a shipwreck\n")
    tale("you must find 3 treasures to return home\n")
    tale("You see a temple, a lake, and a forest nearby.\n")


def player():
    tale("Choose your player\n1. Ali\n2. Yasmeena")
    choice = input("choose '1' or '2':\n")
    if choice == "1":
        name = "Ali"
    elif choice == "2":
        name = "Yasmeena"
    else:
        tale("Invalid choice")
        return player()
    tale(f"Welcome {name}, collect the treasures and defeat the guardians!\n")


def choice_place():
    tale("Where do you want to go?")
    print("1. Temple\n2. Lake\n3. Forest")
    choice = input("Choose: '1', '2', or '3':\n")
    if choice == "1":
        temple()
    elif choice == "2":
        lake()
    elif choice == "3":
        forest()
    else:
        tale("Invalid choice.")
        choice_place()


def scorpion():
    if "scorpion" in defeated_monsters:
        tale("You have already defeated the scorpion.")
        right_choice()
        return

    tale("You are facing a giant scorpion. Its weakness is 'magical fire'.")
    weapon = choose_weapon()
    if weapon == "magical fire":
        tale("You defeated the scorpion and gained a magical spear!")
        weapons.append("magical spear")
        defeated_monsters.append("scorpion")
        tale("The spear has scorpion venom.\n")
        right_choice()
    else:
        tale("GAME OVER!")
        start_exit()


def snake():
    if "snake" in defeated_monsters:
        tale("You already defeated the snake.")
        take_fire()
        return

    tale("You are facing a giant snake. Its weakness is 'magical mirror'.")
    weapon = choose_weapon()
    if weapon == "magical mirror":
        tale("You turned the snake into stone!")
        tale("The word 'HOME' appears magically.")
        defeated_monsters.append("snake")
        print("1. Go to the tower top\n2. Go back to choose place")
        choice = input("Choose '1' or '2': ")
        if choice == "1":
            take_fire()
        else:
            start_exit()
    else:
        tale("GAME OVER!")
        start_exit()


def forest():
    if "tiger" in defeated_monsters:
        tale("You already defeated the tiger.")
        enter_den()
        return

    tale("You encounter a tiger. Its weakness is 'magical spear'.")
    weapon = choose_weapon()
    if weapon == "magical spear":
        tale("You defeated the tiger!")
        defeated_monsters.append("tiger")
        enter_den()
    else:
        tale("You couldn't defeat the tiger. GAME OVER!")
        start_exit()


def enter_den():
    tale("Inside the den, there's a magical chest. Say the magic word.")
    choice = input("Say the magic word:\n").upper()
    if choice == "HOME":
        if "diamond" not in treasures:
            tale("The chest opens! You find a diamond.")
            treasures.append("diamond")
        check_win()
        start_exit()
    else:
        tale("Wrong word. You must defeat the snake first.")
        start_exit()


def temple():
    tale("The temple holds a chest of gold coins, but a scorpion guards it.")
    tale("You see two entrances (left and right) and a magical mirror.")
    take_mirror()


def take_mirror():
    if "magical mirror" not in weapons:
        choice = input("Do you want to take the mirror? (yes/no): ").lower()
        if choice == "yes":
            weapons.append("magical mirror")
            tale("You took the magical mirror.")
    left_right()


def left_right():
    choice = input("Go 'left' or 'right'?\n").lower()
    if choice == "left":
        scorpion()
    elif choice == "right":
        right_choice()
    else:
        tale("Invalid choice.")
        left_right()


def right_choice():
    if "gold coins" not in treasures:
            tale("You found a chest of gold coins!")
            treasures.append("gold coins")
            check_win()
            second_choice()
    else:
        tale("Invalid choice.")
        left_right()


def second_choice():
    tale("Do you want to go 'left' or 'out' of the temple?")
    choice = input("Choose 'left' or 'out':\n").lower()
    if choice == "left":
        scorpion()
    elif choice == "out":
        start_exit()
    else:
        second_choice()


def lake():
    tale("You see a boat and a path of stones leading to a tower.")
    tale("On top of the tower is a magic carpet.")
    tale("Beware of the snake in the lake.")
    print("1. Take the boat\n2. Walk on stones")
    choice = input("Choose '1' or '2':\n")
    if choice == "1":
        tale("You reach the tower. The boat sinks after use.")
        tale("At the tower entrance, you see a magical fire.")
        take_fire()
    elif choice == "2":
        snake()
    else:
        lake()


def take_fire():
    if "magical fire" not in weapons:
        choice = input("Do you want to take the magical fire? (yes/no): ").lower()
        if choice == "yes":
            weapons.append("magical fire")
            tale("You got the magical fire!")
    top_tower()


def top_tower():
    tale("You reach the top of the tower.")
    if "magic carpet" not in treasures:
        tale("You find a magic carpet!")
        treasures.append("magic carpet")
    check_win()
    out_tower()


def out_tower():
    tale("Do you want to leave by:")
    print("1. Flying carpet\n2. Walk back")
    choice = input("Choose '1' or '2':\n")
    if choice == "1":
        tale("You fly back to the beginning.")
        start_exit()
    elif choice == "2":
        snake()
    else:
        out_tower()


def start_exit():
    tale("Do you want to start again or exit?")
    choice = input("Choose 'start' or 'exit':\n").lower()
    if choice == "start":
        choice_place()
    elif choice == "exit":
        out_game()
    else:
        start_exit()


def out_game():
    tale("Thank you for playing. Goodbye!")
    exit()


# Start the game
play_game()
