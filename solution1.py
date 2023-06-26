# Initialize the game
left_bank = ['farmer', 'wolf', 'goat', 'cabbage']
right_bank = []
boat = []
right_boat = []

def display_state():
    print("Left Bank: ", left_bank)
    # print("Boat: ", boat)
    print("Boat (left pier): ", boat)
    print("Boat (right pier): ", right_boat)
    print("Right Bank: ", right_bank)
    print()

def validate_state():
    if 'wolf' in left_bank and 'goat' in left_bank and 'farmer' not in left_bank:
        return False
    elif 'goat' in left_bank and 'cabbage' in left_bank and 'farmer' not in left_bank:
        return False
    elif 'wolf' in right_bank and 'goat' in right_bank and 'farmer' not in right_bank:
        return False
    elif 'goat' in right_bank and 'cabbage' in right_bank and 'farmer' not in right_bank:
        return False
    else:
        return True

def check_win():
    if len(left_bank) == 0 and len(boat) == 0 and len(right_boat) == 0:
        print("Congratulations! You have successfully crossed the river!")
        return True
    return False

def move(item):
    if item in left_bank:
        left_bank.remove(item)
        boat.append(item)
    elif item in boat:
        boat.remove(item)
        left_bank.append(item)
    elif item in right_boat:
        right_boat.remove(item)
        right_bank.append(item)
    elif item in right_bank:
        right_bank.remove(item)
        right_boat.append(item)

def play_game():
    print("Welcome to the River Crossing Game!")
    print("Try to move all the items to the right bank.")
    print("Be careful not to leave the wolf alone with the goat, or the goat alone with the cabbage!")
    print("Commands: 'w' for wolf, 'g' for goat, 'c' for cabbage, 'f' for farmer")
    print("To move an item, enter the corresponding command. To move the boat, simply press 'enter'.")
    print()

    while True:
        display_state()
        
        if not validate_state():
            print("You lost! The wolf ate the goat or the goat ate the cabbage.")
            break

        if check_win():
            break

        action = input("Enter your action: ")

        if action == 'w':
            move('wolf')
        elif action == 'g':
            move('goat')
        elif action == 'c':
            move('cabbage')
        elif action == 'f':
            move('farmer')
        elif action == '':
            # if len(boat) > 0:
                if 'farmer' in boat:
                    print("The farmer rowed the boat to the other side.")
                    boat.remove('farmer')
                    right_boat.append('farmer')
                    if 'goat' in boat:
                        boat.remove('goat')
                        right_boat.append('goat')
                    if 'wolf' in boat:
                        boat.remove('wolf')
                        right_boat.append('wolf')
                    if 'cabbage' in boat:
                        boat.remove('cabbage')
                        right_boat.append('cabbage')
                elif 'farmer' in right_boat:
                    print("The farmer rowed the boat to the other side.")
                    right_boat.remove('farmer')
                    boat.append('farmer')
                    if 'goat' in right_boat:
                        right_boat.remove('goat')
                        boat.append('goat')
                    if 'wolf' in right_boat:
                        right_boat.remove('wolf')
                        boat.append('wolf')
                    if 'cabbage' in right_boat:
                        right_boat.remove('cabbage')
                        boat.append('cabbage')
                else:
                    print("The farmer must be in the boat to row it.")
            # else:
            #     print("The boat is empty. You need to move at least one item.")
        else:
            print("Invalid command. Please try again.")
        print()

# Start the game
play_game()
