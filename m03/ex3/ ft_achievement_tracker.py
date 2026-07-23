from typing import Set
import random


def gen_player_achievements(all_achievements: Set[str]) -> Set[str]:
    achievements_list: list = list(all_achievements)
    num_achievements: int = random.randint(4, 10)
    return set(random.sample(achievements_list, num_achievements))


def main() -> None:
    all_possible_achievements: Set[str] = {
        'Crafting Genius', 'World Savior', 'Master Explorer',
        'Collector Supreme',
        'Untouchable', 'Boss Slayer', 'Strategist', 'Unstoppable',
        'Speed Runner',
        'Survivor', 'Treasure Hunter', 'First Steps', 'Sharp Mind',
        'Hidden Path Finder'
    }

    players: dict = {
        'Alice': gen_player_achievements(all_possible_achievements),
        'Bob': gen_player_achievements(all_possible_achievements),
        'Charlie': gen_player_achievements(all_possible_achievements),
        'Dylan': gen_player_achievements(all_possible_achievements)
    }

    print("=== Achievement Tracker System ===\n")
    for player, achievements in players.items():
        print(f"Player {player}: {achievements}")

    all_unique: Set[str] = set()
    for achievements in players.values():
        all_unique = all_unique.union(achievements)
    print(f"\nAll distinct achievements: {all_unique}")

    common: Set[str] = set(all_possible_achievements)
    for achievements in players.values():
        common = common.intersection(achievements)
    print(f"\nCommon achievements: {common}\n")

    for player, achievements in players.items():
        others_unique: Set[str] = set()
        for other_player, other_achievements in players.items():
            if other_player != player:
                others_unique = others_unique.union(other_achievements)
        only_this_player: Set[str] = achievements.difference(others_unique)
        print(f"Only {player} has: {only_this_player}")

    print()

    for player, achievements in players.items():
        others_all: Set[str] = set()
        for other_player, other_achievements in players.items():
            if other_player != player:
                others_all = others_all.union(other_achievements)
        missing: Set[str] = others_all.difference(achievements)
        print(f"{player} is missing: {missing}")


if __name__ == "__main__":
    main()
