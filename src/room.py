# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.room_items = []

    # Add item to room
    def add_item(self, item):
        self.room_items.append(item)

    # Remove item from room
    def remove_item(self, item):
        if item in self.room_items:
            self.room_items.remove(item)
        else:
            print(f"{item} is not in this room")

    # Print list of items in room
    def print_items(self):
        print("Items in room")
        print("--------------------")

        if len(self.room_items):
            for item in self.room_items:
                print(f"{item.name}")
        else:
            print("No items in this room")

        print("--------------------")

    def __str__(self):
        return f"Room: {self.name} Description: {self.description}"

