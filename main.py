class gadget:
    def __init__(self, name, typ, qty):
        self.name = name
        self.typ = typ
        self.qty = qty

    def __str__(self):
        return f"The gadget is {self.name}, of type : {self.typ}, and there are {self.qty} of them"
    
class Arsenal:
    def __init__(self):
        self.items = []

    def add_gadget(self, new_item):
        self.items.append(new_item)

    def show_inventory(self):
        for item in self.items:
            print(item)

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for item in self.items:
                file.write(str(item) + "\n")

    def load_from_file(self, filename):
        with open(filename , "r") as file:
            self.items = []
            for line in file:
                name, qty, typ = line.strip().split(", ")
                self.items.append(gadget(name, typ, int(qty)))

my_cave = Arsenal()

g1 = gadget("Batmobile", "Transport", 5) 
my_cave.add_gadget(g1)
g2 = gadget("Batarang", "weapon", 100)
my_cave.add_gadget(g2)

my_cave.show_inventory()
my_cave.save_to_file("inventory.txt")
my_cave.load_from_file("inventory.txt")
my_cave.show_inventory()
