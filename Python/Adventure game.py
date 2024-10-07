# Basic level system
# Attack and defense stats
# Option to either fight boss or go into arena to level
# Spend gold for equipment to increase stats

attack = 10
defense = 10
health = 100
skill_points = 3
level = 1
xp = 0
xp_to_next_level = 100
xp_multiplier = 1.5 # Adjust this to control how quickly the XP requirement grows

def health_up():
    global health, skill_points
    print("Each skill point adds +100 to your health.")
    while True:
        try:
            if skill_points > 0:
                points = int(input("How many skill points would you like to use?: "))
                if 0 < points <= skill_points:
                    skill_points -= points
                    health += 100 * points
                    print(f"Success. You now have {health} health!")
                    stat_menu()
                else:
                    print("You don't have enough skill points.")
            else:
                print("You have no skill points left.")
                stat_menu()
        except ValueError:
            print("Invalid input, please enter a number.")

def attack_up():
    global attack, skill_points
    print("Each skill point adds +10 to your attack.")
    while True:
        try:
            if skill_points > 0:
                points = int(input("How many skill points would you like to use?: "))
                if 0 < points <= skill_points:
                    skill_points -= points
                    attack += 10 * points
                    print(f"Success. You now have {attack} attack!")
                    stat_menu()
                else:
                    print("You don't have enough skill points.")
            else:
                print("You have no skill points left.")
                stat_menu()
        except ValueError:
            print("Invalid input, please enter a number.")

def defense_up():
    global defense, skill_points
    print("Each skill point adds +10 to your defense.")
    while True:
        try:
            if skill_points > 0:
                points = int(input("How many skill points would you like to use?: "))
                if 0 < points <= skill_points:
                    skill_points -= points
                    defense += 10 * points
                    print(f"Success. You now have {defense} defense!")
                    stat_menu()
                else:
                    print("You don't have enough skill points.")
            else:
                print("You have no skill points left.")
                stat_menu()
        except ValueError:
            print("Invalid input, please enter a number.")

def stat_menu():
    global skill_points, health, attack, defense
    print("Your current stats: ")
    print(f"1. Health: {health}")
    print(f"2. Attack: {attack}")
    print(f"3. Defense: {defense}")
    print(f"You currently have {skill_points} skill points.")
    
    while True:
        try:
            level_skill = int(input("Select the number of the skill you want to level (or 0 to exit): "))
            if level_skill == 0:
                return
            elif level_skill == 1:
                health_up()
            elif level_skill == 2:
                attack_up()
            elif level_skill == 3:
                defense_up()
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def gain_xp(amount):
    global xp, level, xp_to_next_level, skill_points
    xp += amount
    print(f"You gained {amount} XP!")

    while xp >= xp_to_next_level:
        xp -= xp_to_next_level
        level += 1
        skill_points += 1
        xp_to_next_level = int(xp_to_next_level * xp_multiplier)
        print(f"Level up! You are now level {level}.")
        print(f"XP needed for the next level: {xp_to_next_level}")
        print(f"You have {xp} XP left.")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Fight boss")
        print("2. Train")
        print("3. Stats")
        print("4. Shop")
        try:
            menu_select = int(input("> "))
            if menu_select == 1:
                continue
                # Add logic for fighting boss here
            elif menu_select == 2:
                continue
                # Add logic for training here
            elif menu_select == 3:
                stat_menu()
            elif menu_select == 4:
                continue
                # Add logic for shop here
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# To start the game
main_menu()
