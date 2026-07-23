from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex2.exception import InvalidCombination


def battle(opponents):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    n = len(opponents)

    for i in range(n):
        for j in range(i + 1, n):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print("\n* Battle *")
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")

            try:
                if not strategy1.is_valid(creature1):
                    raise InvalidCombination(
                        "Invalid Creature '{}' for this {} strategy".format(
                            creature1.name,
                            strategy1.__class__.__name__
                            .replace("Strategy", "")
                            .lower(),
                        )
                    )

                if not strategy2.is_valid(creature2):
                    raise InvalidCombination(
                        "Invalid Creature '{}' for this {} strategy".format(
                            creature2.name,
                            strategy2.__class__.__name__
                            .replace("Strategy", "")
                            .lower(),
                        )
                    )

                print(strategy1.act(creature1))
                print(strategy2.act(creature2))

            except InvalidCombination as error:
                print(f"Battle error, aborting tournament: {error}")
                return


def tournament_0():
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")

    opponents = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]

    battle(opponents)


def tournament_1():
    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")

    opponents = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]

    battle(opponents)


def tournament_2():
    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")

    opponents = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]

    battle(opponents)


if __name__ == "__main__":
    tournament_0()
    tournament_1()
    tournament_2()
