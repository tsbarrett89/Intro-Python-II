from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     ['torch']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['bent shield', 'faded skull']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['50 foot rope', 'bow']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['rat droppings', 'torch']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['gleaming sword', 'polished helm', 'battleaxe', 'bag of diamonds']),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'], [])

# Write a loop that:
#
def run ():
    running = True
    while running == True:
# * Prints the current room name
        print("Your location -", player.current_room.name)
    
# * Prints the current description (the textwrap module might be useful here).
        print(player.current_room.description)
# * Waits for user input and decides what to do.
        user_input = input("Actions: Move - select a direction ('n', 'e', 's', 'w'), look around ('look'), look in you bag ('bag'), pick up item ('grab item'), or drop item ('drop item')")

        command = user_input.split()
#
# If the user enters a cardinal direction, attempt to move to the room there.
        if len(command) == 1:
            if user_input == 'n':
                if hasattr(player.current_room, "n_to"):
                    player.current_room = player.current_room.n_to
                else:
                    print('There is no room in that direction')
            elif user_input == 'e':
                if hasattr(player.current_room, "e_to"):
                    player.current_room = player.current_room.e_to
                else:
                    print("Ouch, that's a wall")
            elif user_input == 's':
                if hasattr(player.current_room, "s_to"):
                    player.current_room = player.current_room.s_to
                else:
                    print("There is no room in that direction")
            elif user_input == 'w':
                if hasattr(player.current_room, "w_to"):
                    player.current_room = player.current_room.w_to
                else:
                    print("You walked into a wall")
            elif user_input == 'q':
                running = False
            elif user_input == 'look':
                print(f"Looking around you see: {', '.join(player.current_room.items)}")
            elif user_input == 'bag':
                if len(player.items) == 0:
                    print("Your bag is empty")
                else:
                    print(f"In your bag you find: {', '.join(player.items)}")
        elif len(command) > 1:
            if command[0] == 'grab':
                item = ' '.join(command[1:])
                if item in player.current_room.items:
                    player.items.append(item)
                    player.current_room.items.remove(item)
                else:
                    print(f'There is no {item} in this room')
            elif command[0] == 'drop':
                item = ' '.join(command[1:])
                if item in player.items:
                    player.items.remove(item)
                    player.current_room.items.append(item)
                else:
                    print(f"You are not carrying {item}")
        else:
            print("Please input a valid action")
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

run()