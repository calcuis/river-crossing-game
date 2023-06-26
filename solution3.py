# Initialize the game
left_bank = ['father', 'mother', 'girl', 'boy', 'oldman', 'dog']
right_bank = []
boat = []
right_boat = []
left = []

def display_state():
    print("Left Bank: ", left_bank)
    print("Left Pier (boat): ", boat)
    print("River")
    print("Right Pier (boat): ", right_boat)
    print("Right Bank: ", right_bank)
    print()

def validate_state():
    if 'father' in left_bank and 'boy' in left_bank and 'mother' not in left_bank:
        return False
    elif 'mother' in left_bank and 'girl' in left_bank and 'father' not in left_bank:
        return False
    elif 'boy' in left_bank and 'girl' in left_bank and 'father' not in left_bank and 'mother' not in left_bank and 'oldman' not in left_bank:
        return False
    elif 'dog' in left_bank and 'oldman' not in left_bank and ('father' in left_bank or 'mother' in left_bank or 'girl' in left_bank or 'boy' in left_bank):
        return False
    elif 'father' in right_bank and 'boy' in right_bank and 'mother' not in right_bank:
        return False
    elif 'mother' in right_bank and 'girl' in right_bank and 'father' not in right_bank:
        return False
    elif 'boy' in right_bank and 'girl' in right_bank and 'father' not in right_bank and 'mother' not in right_bank and 'oldman' not in right_bank:
        return False
    elif 'dog' in right_bank and 'oldman' not in right_bank and ('father' in right_bank or 'mother' in right_bank or 'girl' in right_bank or 'boy' in right_bank):
        return False
    else:
        return True

def check_win():
    if len(left_bank) == 0 and len(boat) == 0 and len(right_boat) == 0:
        print("Congratulations! You have successfully crossed the river!")
        return True
    return False

def move(item):
    if item in left_bank and len(left) == 0 and len(boat) < 2:
        left_bank.remove(item)
        boat.append(item)
    elif item in boat:
        boat.remove(item)
        left_bank.append(item)
    elif item in right_boat:
        right_boat.remove(item)
        right_bank.append(item)
    elif item in right_bank and len(left) > 0 and len(right_boat) < 2:
        right_bank.remove(item)
        right_boat.append(item)

def play_game():
    print("Welcome to the River Crossing Game!")
    print("Try to move all the items to the right bank.")
    print("Be careful: father beats boy without mother; mother beats girl without father; kids fight without adult; dog bites others without oldman.")
    print("Commands: 'f' for father, 'm' for mother, 'g' for girl, 'b' for boy, 'o' for oldman, 'd' for dog")
    print("To move an item, enter the corresponding command. To move the boat, simply press 'enter'.")
    print()

    while True:
        display_state()
        
        if not validate_state():
            print("You lost! Beating or Fighting or Biting issue occured.")
            break

        if check_win():
            break

        action = input("Enter your action: ")

        if action == 'f':
            move('father')
        elif action == 'm':
            move('mother')
        elif action == 'g':
            move('girl')
        elif action == 'b':
            move('boy')
        elif action == 'o':
            move('oldman')
        elif action == 'd':
            move('dog')
        elif action == '':
            if len(boat) > 0 or len(right_boat) > 0:
                if 'father' in boat or 'mother' in boat or 'oldman' in boat:
                    print("Rowed the boat to the other side.")
                    left.append('yes')
                    if 'father' in boat:
                        boat.remove('father')
                        right_boat.append('father')
                    if 'mother' in boat:
                        boat.remove('mother')
                        right_boat.append('mother')
                    if 'girl' in boat:
                        boat.remove('girl')
                        right_boat.append('girl')
                    if 'boy' in boat:
                        boat.remove('boy')
                        right_boat.append('boy')
                    if 'oldman' in boat:
                        boat.remove('oldman')
                        right_boat.append('oldman')
                    if 'dog' in boat:
                        boat.remove('dog')
                        right_boat.append('dog')
                elif 'father' in right_boat or 'mother' in right_boat or 'oldman' in right_boat:
                    print("Rowed the boat to the other side.")
                    left.remove('yes')
                    if 'father' in right_boat:
                        right_boat.remove('father')
                        boat.append('father')
                    if 'mother' in right_boat:
                        right_boat.remove('mother')
                        boat.append('mother')
                    if 'girl' in right_boat:
                        right_boat.remove('girl')
                        boat.append('girl')
                    if 'boy' in right_boat:
                        right_boat.remove('boy')
                        boat.append('boy')
                    if 'oldman' in right_boat:
                        right_boat.remove('oldman')
                        boat.append('oldman')
                    if 'dog' in right_boat:
                        right_boat.remove('dog')
                        boat.append('dog')
                else:
                    print("Adult must be in the boat to row it.")
            else:
                print("The boat is empty. You need to move at least one item.")
        else:
            print("Invalid command. Please try again.")
        print()

# Start the game
play_game()
