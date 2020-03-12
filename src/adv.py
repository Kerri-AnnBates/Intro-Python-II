from cmd import Cmd
from room import Room
from player import Player

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


# Main
playing = True

# Make a new player object that is currently in the 'outside' room.
p_name = "Yoshi"
c_room = room["outside"]

new_player = Player(p_name, c_room)
print(f"Hello {new_player.name}!")
print(
    "Pick your next destination. Please enter either of the following: [n] to go north, [s] to go south, [e] to go east, [w] to go west, or [q] to quit."
)


def playGame():
    global playing
    global new_player

    # * Prints the current room name
    print(f"Current room: {new_player.current_room.name}")

    # * Prints the current description (the textwrap module might be useful here).
    print(f"Room Description: {new_player.current_room.description}")

    # * Waits for user input and decides what to do.
    #
    user_input = input("Where do you want to go next: ")

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
    if user_input == "q":
        playing = False
    elif user_input == "n":
        new_player.move(user_input)
    elif user_input == "s":
        new_player.move(user_input)
    elif user_input == "e":
        new_player.move(user_input)
    elif user_input == "w":
        new_player.move(user_input)
    else:
        print(
            "Invalid input! Please enter either of the following: [n] to go north, [s] to go south, [e] to go east, [w] to go west, or [q] to quit."
        )


# Write a loop that:
while playing:
    playGame()
