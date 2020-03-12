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
        self.current_items = []

    def print_items(self):
        print("Items in room")
        print("--------------------")

        if len(self.current_items):
            for item in self.current_items:
                print(f"{item}")
        else:
            print("No items in this room")

        print("--------------------")

    def __str__(self):
        return f"Room: {self.name} Description: {self.description}"

