# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        room = getattr(self.current_room, f"{direction}_to")

        if room != None:
            self.current_room = room
        else:
            print(
                "Cannot go that way! Pick another direction. [e] to go east, [w] to go west, [n] to go north, [s] to go south"
            )

    def __str__(self):
        return f"Player: {self.name}, {self.current_room}"

