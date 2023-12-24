import random

def username():
    name = input("Enter your name:  ")
    return name

def welcome_message(name):
    print(f"Welcome {name}! Snake and Ladder Game is ready to play.")

def roll_dice():
    return random.randint(1, 6)

def snake_ladder(position):
    # Define snakes and ladders
    snakes_and_ladders = {3: 21, 30: 44, 12:87, 77: 99, 16: 6, 56: 13, 88: 63, 98: 9}

    # Check if the current position is on a snake or ladder
    if position in snakes_and_ladders:
        new_position = snakes_and_ladders[position]
        if new_position > position:
            print(f"Climbed a ladder! Moved from {position} to {new_position}")
        else:
            print(f"Oh no! Bit by a snake. Moved from {position} to {new_position}")
        return new_position
    else:
        return position

def play_game():
    player_position = 0

    while player_position < 100:
        input("Press Enter to roll the dice...")
        dice_roll = roll_dice()
        print(f"You rolled a {dice_roll}")
        
        if dice_roll != 6 and player_position == 0:
            print("You need to roll a 6 to start the game.")
            continue

        player_position += dice_roll
        player_position = snake_ladder(player_position)

        print(f"You are now at position {player_position}")

    print("Congratulations! You reached the final position.")

if __name__ == "__main__":
    name = username()
    welcome_message(name)
    play_game()