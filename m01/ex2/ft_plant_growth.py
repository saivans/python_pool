class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

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


plant1 = Plant("Rose", 25, 30)
print("=== Garden Plant Growth ===")
print("=== Day 1 ===")
Plant.show(plant1)
i = 2
for i in range(2, 8):
    print(f"=== Day {i} ===")
    Plant.age(plant1)
    Plant.grow(plant1)
    Plant.show(plant1)
