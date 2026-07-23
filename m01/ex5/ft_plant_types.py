class Plant:
    def __init__(self, name, height=0, age=0):
        self.name = name
        self.height = round(height, 2)
        self.age = age

    def grow(self):
        self.height = round(self.height + 2.1, 2)

    def age_up(self):
        self.age += 1

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide"
        )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self):
        super().grow()
        self.nutritional_value += 1

    def age_up(self):
        super().age_up()

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


print("=== Garden Plant Types ===")

print("=== Flower")
rose = Flower("Rose", 15.0, 10, "red")
rose.show()
print("[asking the rose to bloom]")
rose.bloom()
rose.show()
print("")
print("=== Tree")
oak = Tree("Oak", 200.0, 365, 5.0)
oak.show()
print("[asking the oak to produce shade]")
oak.produce_shade()
print("")
print("=== Vegetable")
tomato = Vegetable("Tomato", 5.0, 10, "April")
tomato.show()
print("[make tomato grow and age for 20 days]")
for _ in range(20):
    tomato.grow()
    tomato.age_up()
tomato.show()
