# River Crossing Game
# In this game, you have a farmer, a wolf, a goat, and a cabbage on the left bank of a river. The objective is to move all the items to the right bank without leaving the wolf alone with the goat or the goat alone with the cabbage. The player can choose to move one item at a time or move the boat (which requires the farmer to be in the boat). The game will display the state of the banks and the boat after each action, and it will check for win or lose conditions after each move.
# Initialize the game
left_bank = ['farmer', 'wolf', 'goat', 'cabbage']
right_bank = []
boat = []

def display_state():
    print("Left Bank: ", left_bank)
    print("Boat: ", boat)
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
    if len(left_bank) == 0 and len(boat) == 0:
        print("Congratulations! You have successfully crossed the river!")
        return True
    return False

def move(item):
    if item in left_bank:
        left_bank.remove(item)
        boat.append(item)
    elif item in boat:
        boat.remove(item)
        right_bank.append(item)

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
            if 'farmer' in boat:
                boat.remove('farmer')
                if len(boat) > 0:
                    print("You rowed the boat to the other side.")
                    print()
                    move('farmer')
                else:
                    print("The boat is empty. You need to move at least one item.")
            else:
                print("The farmer must be in the boat to row it.")
        else:
            print("Invalid command. Please try again.")
        print()

# Start the game
play_game()