import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file: IO[str] = open(filename, "r")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return

    print("---\n")

    try:
        content: str = file.read()
        print(content, end="")
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")

    print("\n\n---")

    file.close()
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
