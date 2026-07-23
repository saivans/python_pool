import random
from typing import Dict, List


def main() -> None:
    print("=== Game Data Alchemist ===")

    initial_players: List[str] = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Kamar', 'Gregory',
        'john', 'kevin', 'Liam'
    ]
    print(f"Initial list of players: {initial_players}")

    capitalized_all: List[str] = [name.capitalize() for name
                                  in initial_players]
    print(f"New list with all names capitalized: {capitalized_all}")

    capitalized_only: List[str] = [
        name for name in initial_players if name[0].isupper()
    ]
    print(f"New list of capitalized names only: {capitalized_only}")

    score_dict: Dict[str, int] = {
        name: random.randint(1, 1000) for name in capitalized_all
    }
    print(f"Score dict: {score_dict}")

    average_score: float = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {average_score:.2f}")

    high_scores: Dict[str, int] = {
        name: score for name, score in score_dict.items()
        if score > average_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
