from ex0 import FlameFactory, AquaFactory


def test_factory(factory):
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())


def battle(factory1, factory2):
    c1 = factory1.create_base()
    c2 = factory2.create_base()

    print(f"{c1.describe()}\nvs.\n{c2.describe()}\nfight!")

    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    print("Testing factory")
    test_factory(FlameFactory())

    print("\nTesting factory")
    test_factory(AquaFactory())

    print("\nTesting battle")
    battle(FlameFactory(), AquaFactory())
