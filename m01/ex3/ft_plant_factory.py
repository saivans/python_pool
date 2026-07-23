class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def age(self):
        self.age += 1

    def grow(self):
        n = count_letter(self.name)
        x = round(n / 10, 2)
        self.height = round(self.height + x, 2)


def count_letter(text):
    count = 0
    for _ in text:
        count += 1
    return count


print("=== Plant Factory Output ===")
plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Tulip", 18, 12)
plant3 = Plant("Sunflower", 40, 20)
plant4 = Plant("Lily", 15, 8)
plant5 = Plant("Orchid", 22, 16)

plants = [plant1, plant2, plant3, plant4, plant5]

for plant in plants:
    print(f"Created: {plant.show()}")
