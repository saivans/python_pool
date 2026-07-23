import sys


def main() -> None:
    args = sys.argv[1:]

    print("=== Player Score Analytics ===")

    if len(args) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return

    valid_scores = []
    invalid_params = []

    for arg in args:
        try:
            score: int = int(arg)
            valid_scores.append(score)
        except ValueError:
            invalid_params.append(arg)

    for invalid in invalid_params:
        print(f"Invalid parameter: '{invalid}'")

    if len(valid_scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return

    total_players: int = len(valid_scores)
    total_score: int = sum(valid_scores)
    average_score: float = total_score / total_players
    high_score: int = max(valid_scores)
    low_score: int = min(valid_scores)
    score_range: int = high_score - low_score

    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
