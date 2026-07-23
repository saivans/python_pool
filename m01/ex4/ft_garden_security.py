class Plant:
    def __init__(self, name, height=0, age=0):
        self._name = name
        if height >= 0:
            self._height = round(height, 2)
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            self._height = 0
        if age >= 0:
            self._age = round(age, 2)
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            self._age = 0
        if height >= 0 and age >= 0:
            print(f"Plant created: {name}: {height}cm, {age} days old")

    def set_height(self, height):
        if height >= 0:
            self._height = round(height, 2)
            print(f"Height updated: {height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age):
        if age >= 0:
            self._age = round(age, 2)
            print(f"Age updated: {age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self):
        return f"{self._height} cm"

    def get_age(self):
        return f"{self._age} days old"

    def show(self):
        print(
            f"Current state: {self._name}: "
            f"{self.get_height()}, {self.get_age()}"
        )


print("=== Garden Security System ===")
plant1 = Plant("Rose", 15.0, 10)
print("")
plant1.set_height(25)
plant1.set_age(30)
print("")
plant1.set_height(-1)
plant1.set_age(-1)
print("")
plant1.show()
