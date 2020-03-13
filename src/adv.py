from cmd import Cmd
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

# Create items
rock = Item("rock", "This is a rock")
sword = Item("sword", "This is a sword")
food = Item("food", "Some food")
coin = Item("coin", "A coin")
medkit = Item("medkit", "50 points health")
gun = Item("gun", "KN Rifle")

# Add items to rooms
room["foyer"].add_item(rock)
room["foyer"].add_item(food)
room["foyer"].add_item(gun)
room["overlook"].add_item(sword)
room["overlook"].add_item(medkit)
room["narrow"].add_item(coin)
room["narrow"].add_item(food)

# Main
playing = True

# Make a new player object that is currently in the 'outside' room.
player = Player(input(">>>> Enter your name: "), room["outside"])

print(f"Hello {player.name}!")
print(
    "Pick your next destination. Please enter either of the following: [n] to go north, [s] to go south, [e] to go east, [w] to go west, or [q] to quit."
)


def playGame():
    global playing

    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    print(" ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Current room: {player.current_room.name}")
    print(f"Room Description: {player.current_room.description}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    player.current_room.print_items()
    print(" ")

    # * Waits for user input and decides what to do.
    user_input = input(">>>> Where do you want to go next: ")

    nouns = ("n", "s", "w", "e", "q", "i", "inventory")
    verbs = ("go", "take", "drop")

    if len(user_input.split()) == 1:
        if user_input == "q":
            playing = False
        elif user_input == "i" or user_input == "inventory":
            player.show_inventory()
        else:
            print("Invalid input!")
    elif len(user_input.split()) == 2:
        user_verb = user_input.split()[0]
        user_noun = user_input.split()[1]

        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.
        # If the user enters "q", quit the game.

        if user_verb in verbs:
            if user_verb == "go" and user_noun in nouns:
                player.move(user_noun)
            elif user_verb == "take":
                player.take_item(user_noun)
            elif user_verb == "drop":
                player.drop_item(user_noun)
            else:
                print("Invalid input")
        else:
            print(
                "Invalid input! Please enter either of the following: [n] to go north, [s] to go south, [e] to go east, [w] to go west, or [q] to quit."
            )
    else:
        print("Invalid Input!")


# Write a loop that:
while playing:
    playGame()
