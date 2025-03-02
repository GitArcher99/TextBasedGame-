# TextBasedGame.py
# Author: Jeremiah Archer

# Function to display the game instructions
def show_instructions():
    print("Elden Ring Adventure Game")
    print("Collect all the items to win the game and defeat the villain.")
    print("Move commands: go North, go South, go East, go West")
    print("Collect items: get 'item name'")
    print("Avoid the villain until you're ready to win!")
    print("--------------------------------------------------")

# Function to display the player's current status
def show_status(current_room, inventory, item_in_room):
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    if item_in_room:
        print(f"You see a {item_in_room}")
    print("----------------------")

# Main function to run the game
def main():
    # Define the rooms, their connections, and items
    rooms = {
        'Great Hall': { 'South': 'Bedroom', 'North': 'Dungeon', 'East': 'Library', 'West': 'Garden', 'item': None },
        'Bedroom': { 'North': 'Great Hall', 'East': 'Cellar', 'item': 'Sword' },
        'Cellar': { 'West': 'Bedroom', 'item': 'Shield' },
        'Dungeon': { 'South': 'Great Hall', 'item': 'Potion' },
        'Library': { 'West': 'Great Hall', 'item': 'Key' },
        'Garden': { 'East': 'Great Hall', 'item': 'Map' },
        'Dragon Lair': { 'South': 'Dungeon', 'item': None }  # Villain's room
    }

    # Start the player in the Great Hall
    current_room = 'Great Hall'
    inventory = []

    # Game loop
    while True:
        # Show the player's current status
        show_status(current_room, inventory, rooms[current_room].get('item', None))

        # Check if the player has collected all items
        if len(inventory) == 5:  # Adjust to the number of items required
            print("Congratulations! You have collected all items and defeated the villain!")
            break

        # Ask the player for their next move
        move = input("Enter your move: ").strip().lower()

        # Handle movement commands
        if move.startswith('go '):
            direction = move[3:]
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way! Try again.")

        # Handle item collection commands
        elif move.startswith('get '):
            item = move[4:]
            if rooms[current_room].get('item') == item:
                inventory.append(item)
                rooms[current_room]['item'] = None  # Remove item from the room
                print(f"You have picked up: {item}")
            else:
                print(f"There is no {item} here!")

        # Handle invalid commands
        else:
            print("Invalid command! Use 'go [direction]' or 'get [item name]'.")

        # Check if the player enters the villain's room without all items
        if current_room == 'Dragon Lair' and len(inventory) < 5:
            print("NOM NOM...GAME OVER! The dragon has eaten you.")
            break

# Run the game
if __name__ == "__main__":
    show_instructions()
    main()

