# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def take_item(self, item):
        item_found = False

        # check if item is a match to an item in the current room.
        for itm in self.current_room.room_items:
            if itm.name == item:
                itm.on_take()
                self.current_room.room_items.remove(itm)
                self.inventory.append(itm)
                item_found = True
                break
            else:
                item_found = False

        if item_found is False:
            print(f"Oh no! {item} is not in this room. Pick another item to take.")

    def drop_item(self, item):
        item_found = False

        for itm in self.inventory:
            if itm.name == item:
                itm.on_drop()
                self.current_room.room_items.append(itm)
                self.inventory.remove(itm)
                item_found = True
                break
            else:
                item_found = False

        if item_found is False:
            print(f"Oh no! {item} is not in your inventory. Pick another item to drop.")

    def move(self, direction):
        room = getattr(self.current_room, f"{direction}_to")

        if room != None:
            self.current_room = room
        else:
            print(
                "Cannot go that way! Pick another direction. [e] to go east, [w] to go west, [n] to go north, [s] to go south"
            )

    def show_inventory(self):
        print(f"My Inventory")
        print("-------------------")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(item.name)
        else:
            print("No items in your inventory!")

    def __str__(self):
        return f"Player: {self.name}, {self.current_room}"

