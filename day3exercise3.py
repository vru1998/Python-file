class Plate:
    def __init__(self):
        self.item_on_plate = []

    def add_to_plate(self, item):
        self.item_on_plate.append(item)

    def remove_from_plate(self, item):
        self.item_on_plate.remove(item)

    def display_items_on_plate(self):
        print(self.item_on_plate)


p = Plate()
p.add_to_plate("Mashroom-Masala")
p.add_to_plate("Paneer-masala")
p.remove_from_plate("Mashroom-Masala")
p.display_items_on_plate()